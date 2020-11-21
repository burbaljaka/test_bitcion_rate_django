from typing import Tuple, Union
from loguru import logger
import requests
from .models import Rate
from .serializers import RateSerializer


def get_current_rate() -> Union[Rate, None]:
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	headers = {
		'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
		'Accept': 'application/json'
	}
	params = {"id": 1}
	response = requests.get(url=url, headers=headers, params=params)
	result, fail = _process_external_response(response.json())
	if fail:
		return None
	serializer = RateSerializer(data=result)
	serializer.is_valid(raise_exception=True)
	new_rate = Rate(**serializer.data)
	return new_rate

def _process_external_response(response: dict) -> Tuple[dict, bool]:
	res = {}
	try:
		res['rate'] = response['data']['1']['quote']['USD']['price']
		res['last_updated'] = response['data']['1']['quote']['USD']['last_updated']
		fail = False
		logger.info(f"Got rate as {res['rate']} and last_updated {res['last_updated']}")
	except KeyError as e:
		logger.error(f"Got error {e} from response {response}")
		res['rate'] = None
		fail= True
	return res, fail
