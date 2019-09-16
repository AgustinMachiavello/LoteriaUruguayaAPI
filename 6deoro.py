import requests


FIVE_DE_ORO_RESULTS_URL = 'https://www3.labanca.com.uy/resultados/cincodeoro'
QUINIELA_RESULTS_URL = 'http://servicios.lanacion.com.ar/loterias/quiniela-montevideo'
TOMBOLA_RESULTS_URL = 'https://www3.labanca.com.uy/resultados/tombola'




def extract_results_five_de_oro():
    """
    Returns a list with two lists containing the main & the second prize
    """
    response = requests.get(FIVE_DE_ORO_RESULTS_URL)
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


def extract_results_quiniela():
    """
    Returns a list with two lists containing the main prize
    """
    response = requests.get(QUINIELA_RESULTS_URL)
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
    
    for i in html_text1: 
        print(i[:4])
    print("-------------------------")
    for i in html_text2:
        print(i[:4])
    return 

class FiveDeOroPrizeChecker():

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

extract_results_quiniela()
#checker = FiveDeOroPrizeChecker(16, 26, 35, 39, 40, extract_results_five_de_oro())
#print("REVANCHA WIN:", checker.check_revancha())
