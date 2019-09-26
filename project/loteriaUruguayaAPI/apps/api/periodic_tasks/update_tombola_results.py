"""Period task for tombola results update

Every 12345 time it makes a request and updates the results"""

# Requests
import requests
from requests_html import HTMLSession

# Datetime
from datetime import date

# Threading
import threading

# lxml scrapping
from lxml import html

def extract_results_tombola_1(year, month, day):
    """
    First option
    Returns a list with two lists containing the nocturne and matutine prize
    """
    html_response = get_decoded_url_content(TOMBOLA_RESULTS_URL.format(year, month, day))
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