"""Utilities functions"""

# Requests
from requests_html import HTMLSession

# Datetime
from datetime import date


def get_decoded_url_content(url, decode_format='utf8'):
    """Returns a string with the decoded HTML (including javascript) by a given url"""
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