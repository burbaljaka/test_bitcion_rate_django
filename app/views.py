from loguru import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .business_logic import get_current_rate
from .models import Rate
from .serializers import RateSerializer


class GetLastRate(APIView):
	def get(self, request, *_, **__):
		queryset = Rate.objects.last()
		return Response(RateSerializer(queryset).data)

class GetCurrentRate(APIView):
	def get(self, request, *_, **__):
		logger.info("Got manual request to get current rate. Timer will be delayed")
		res = get_current_rate()
		if not res:
			return Response({'error': 'Something went wrong, please try again later'}, status.HTTP_400_BAD_REQUEST)
		# update_celery_task_timer()
		res.method = 'manual'
		res.save()
		return Response(RateSerializer(res).data)
