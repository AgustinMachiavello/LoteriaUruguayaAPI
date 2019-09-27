"""Period task for cinco de oro results update

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

# Models
from ..models.results import CincoDeOroResult
from ..models.games import Game

CINCO_DE_ORO_RESULTS_URL_1 = 'https://www3.labanca.com.uy/resultados/cincodeoro'
# Alternative:
CINCO_DE_ORO_RESULTS_URL_2 = 'https://www.nacionalloteria.com/uruguay/5deoro.php'


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
	html_text2 = html_text1[html_text1[len(index1_text):].find(index1_text):]  # second prize line (revancha)
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


def create_cinco_de_oro_prize(prize_list):
	new_result = CincoDeOroResult.objects.create(
		result_game_id = Game.objects.get(game_name='Cinco de oro'),
		first_ball=prize_list[0],
		second_ball=prize_list[1],
		third_ball=prize_list[2],
		fourth_ball=prize_list[3],
		fifth_ball=prize_list[4],
		sixth_ball=prize_list[5],
	)
	return new_result
