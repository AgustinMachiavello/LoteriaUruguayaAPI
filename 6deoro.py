import requests
from datetime import date
from requests_html import HTMLSession
import threading



CINCO_DE_ORO_RESULTS_URL_1 = 'https://www3.labanca.com.uy/resultados/cincodeoro'
# Alternative:
CINCO_DE_ORO_RESULTS_URL_2 = 'https://www.nacionalloteria.com/uruguay/5deoro.php'

QUINIELA_RESULTS_URL_1 = 'https://www.nacionalloteria.com/uruguay/quiniela.php?del-dia={0}-{1}-{2}#listapubli'
# Alternative:
QUINIELA_RESULTS_URL_2 = 'http://servicios.lanacion.com.ar/loterias/quiniela-montevideo'

TOMBOLA_RESULTS_URL = 'https://www.nacionalloteria.com/uruguay/tombola.php?del-dia={0}-{1}-{2}#listapubli'

def crop_after(text, start=0, end=-1):
    """Returns a string cropped between the two indexes but only containing coincidences after the first one
    Example:
    str = 'abc def abc'
    crop_after(str, 'def', 'abc') = ' ' = 'abc def(this space)abc'
    """
    index1 = text.find(start)
    if index1 == -1:
        print("First index not found")
        return None
    text = text[index1+len(start):] # text cropped to start from first_index
    index2 = text.find(end)
    if index2 == -1:
        print("Second index not found")
        return None
    text = text[:index2]
    return text

def get_decoded_url_content(url, decode_format='utf8'):
    """Returns the decoded HTML (including javascript) by a given url"""
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    return response.content.decode(decode_format)

def get_today_date():
    today = date.today()
    # dd/mm/YY
    #d1 = today.strftime("%d/%m/%Y")
    d1 = today.strftime("%Y/%m/%d")
    d1 = d1.split("/")
    return (d1[0], d1[1], d1[2])

def extract_results_cinco_de_oro_2():
    """
    Second option
    Returns a list with two lists containing the main & the second prize
    """
    response = requests.get(CINCO_DE_ORO_RESULTS_URL_1)
    index1_text = '<ul class="bolillas small-block-grid-7">'
    index2_text = '</ul>'
    index1_text_inline = 'alt="'
    index2_text_inline = '" src="'
    text = response.text
    html_text1 = text[text.find(index1_text):]  # main prize line
    html_text2 = html_text1[html_text1[len(index1_text):].find(index1_text):] # second prize line (revancha)
    html_text1 = html_text1[:html_text1.find(index2_text)].split('\n')
    html_text2 = html_text2[:html_text2.find(index2_text)].split('\n')
    html_texts_list = [html_text1, html_text2]
    main_prize = []
    second_prize = []
    i = 0
    for t in html_texts_list:
        i += 1
        for line in t:
            index1 = line.find(index1_text_inline)
            if index1 == -1:
                continue
            line = line[index1:]
            index2 = line.find(index2_text_inline)
            if index2 == -1:
                continue
            line = line[len(index1_text_inline):index2]
            if i == 1:
                main_prize.append(int(line))
            else:
                second_prize.append(int(line))
    return [main_prize, second_prize]

def extract_results_quiniela_2():
    """
    Second option
    Returns a list with two lists containing the nocturne and matutine prize
    """
    response = requests.get(QUINIELA_RESULTS_URL_1)
    index1_text = '<div class="quiniela tabla floatFix">'
    index2_text = '<div class="datafactory">'
    sub_index1 = '<tbody>'
    sub_index2 = '</tbody>'
    text = response.text
    html_text1 = text[text.find(index1_text):]
    html_text1 = html_text1[:html_text1.find(index2_text)]
    html_text1 = html_text1[html_text1.find(sub_index1):]  # first table
    index0 = html_text1.find(sub_index2)
    html_text2 = html_text1[index0+len(sub_index2):]
    html_text2 = html_text2[html_text2.find(sub_index1):]
    html_text1 = html_text1[:index0]
    html_text2 = html_text2[:html_text2.find(sub_index2)]

    html_text1 = html_text1.split('<td>')
    html_text1.pop(0)
    html_text2 = html_text2.split('<td>')
    html_text2.pop(0)
    nocturne_prize = []
    matutine_prize = []
    for i in html_text1:
        nocturne_prize.append(int(i[:3]))
    for i in html_text2:
        matutine_prize.append(int(i[:3]))
    return [nocturne_prize, matutine_prize]

def extract_results_tombola_1(year, month, day):
    """
    First option
    Returns a list with two lists containing the nocturne and matutine prize
    """
    #html_response = get_decoded_url_content(TOMBOLA_RESULTS_URL.format(year, month, day))
    html_response = """<a id="premios"></a><div class="panel panel-default"><div class="panel-heading"><h3>Tombola Vespertina del Lunes 16 de Septiembre de 2019</h3></div><table class="table table-condensed"><tr><td>  <table class="table table-bordered table-condensed">  <tbody><tr class=""><td class="res-sm text-center">02</td></tr><tr class=""><td class="res-sm text-center">07</td></tr><tr class=""><td class="res-sm text-center">10</td></tr><tr class=""><td class="res-sm text-center">13</td></tr><tr class=""><td class="res-sm text-center">16</td></tr></tbody></table></td><td>  <table class="table table-bordered table-condensed">  <tbody><tr class="info"><td class="res-sm text-center">23</td></tr><tr class="info"><td class="res-sm text-center">26</td></tr><tr class="info"><td class="res-sm text-center">27</td></tr><tr class="info"><td class="res-sm text-center">31</td></tr><tr class="info"><td class="res-sm text-center">35</td></tr></tbody></table></td><td>  <table class="table table-bordered table-condensed">  <tbody><tr class=""><td class="res-sm text-center">37</td></tr><tr class=""><td class="res-sm text-center">39</td></tr><tr class=""><td class="res-sm text-center">41</td></tr><tr class=""><td class="res-sm text-center">44</td></tr><tr class=""><td class="res-sm text-center">46</td></tr></tbody></table></td><td>  <table class="table table-bordered table-condensed">  <tbody><tr class="info"><td class="res-sm text-center">53</td></tr><tr class="info"><td class="res-sm text-center">56</td></tr><tr class="info"><td class="res-sm text-center">64</td></tr><tr class="info"><td class="res-sm text-center">87</td></tr><tr class="info"><td class="res-sm text-center">96</td></tr></tbody></table></td></tr></table></div>"""
    first_index= '<a id="premios">'
    last_index = '</td></tr></tbody></table></td></tr></table></div>'
    cropped_text = crop_after(html_response, first_index, last_index)
    list_text = cropped_text.split('<td class="res-sm text-center">')
    list_text.pop(0)
    matutine_prize = []
    for item in list_text:
        matutine_prize.append(int(item[:2]))
    print(matutine_prize)
    #return html1
    return

def extract_results_quiniela_1(year, month, day):
    """
    First option
    Returns a list with two lists containing the nocturne and matutine prize
    """
    html_response = get_decoded_url_content(QUINIELA_RESULTS_URL_2.format(year, month, day))
    first_index= '<a id="premios">'
    last_index = '</td></tr></tbody></table></td></tr></table></div>'
    index1 = html_response.find(first_index)
    if index1 == -1:
        print("First index not found")
        return None
    html1 = html_response[index1:] # html1 cropped to start from first_index
    index2 = html1.find(last_index)
    if index2 == -1:
        print("Second index not found")
        return None
    html1 = html1[:index2]
    return html1

def extract_results_cinco_de_oro_1(year, month, day):
    """
    First option
    Returns a list with two lists containing the nocturne and matutine prize
    """
    html_response = get_decoded_url_content(CINCO_DE_ORO_RESULTS_URL_2)
    first_index= '<section id="listaResultados">'
    last_index = '</section>'
    index1 = html_response.find(first_index)
    if index1 == -1:
        print("First index not found")
        return None
    html1 = html_response[index1:] # html1 cropped to start from first_index
    index2 = html1.find(last_index)
    if index2 == -1:
        print("Second index not found")
        return None
    html1 = html1[:index2]
    return html1

class FiveDeOroPrizeChecker():
    """Checks different prizes"""
    def __init__(self, a, b, c, d, e, results_list):
        self.choices = [a, b, c, d, e]
        self.results_list = results_list

    def check_all(self):
        return
    def check_revancha(self):
        success = 0
        for choice in self.choices:
            if choice in self.results_list[1]:
                success += 1
        return success == 5

class ThreadFunction(threading.Thread):
    """Runs a function with arguments as a thread.

    Recives: (function: def, arguments: list, delay: int (optional))

    Usage:
    t1 = ThreadFunction(someOtherFunc, [1,2], 6)
    t1.start()
    t1.join()  # check if the
    """
    def __init__(self, target, args):
        self.target = target
        self.args = args
        threading.Thread.__init__(self)

    def run(self):
        print(self.target)
        print(self.args)
        self.target(self.args[0], self.args[1], self.args[2])

today = get_today_date()
tombola = extract_results_tombola_1(today[0], today[1], '16')
# quiniela = extract_results_quiniela_1(today[0], today[1], '16')
# cincodeoro = extract_results_cinco_de_oro_1(today[0], today[1], '16')
# print(tombola, quiniela, cincodeoro)
"""
thread1 = ThreadFunction(extract_results_tombola_1, [today[0], today[1], '16'])
thread2 = ThreadFunction(extract_results_quiniela_1, [today[0], today[1], '16'])
thread3 = ThreadFunction(extract_results_cinco_de_oro_1, [today[0], today[1], '16'])
thread1.start()
thread2.start()
thread3.start()
print(thread1.join())
print(thread2.join())
print(thread3.join())
"""
#checker = FiveDeOroPrizeChecker(16, 26, 35, 39, 40, extract_results_five_de_oro())
#print("REVANCHA WIN:", checker.check_revancha())
