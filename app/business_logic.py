import requests

def get_crrent_rate():
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
		'CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
		'Accept': 'application/json'
	}
	response = requests.get(url=url, headers=headers)
	result, fail = _process_external_response(response)
	

def _process_external_response(response: dict) -> dict:
	res = {}
	 
