# HTTP requests functions to retrieve BGS data frol CoR and LOSP factions
# Using EliteBGS API

import requests

def cor_request():
	link = 'https://elitebgs.kodeblox.com/api/eddb/v3/populatedsystems?factionname=Children%20of%20Raxxla'
	r = requests.get(link)
	content = str(r.text)
	return content

def losp_request():
	link = 'https://elitebgs.kodeblox.com/api/eddb/v3/populatedsystems?factionname=The%20L.O.S.P.'
	r = requests.get(link)
	content = str(r.text)
	return content