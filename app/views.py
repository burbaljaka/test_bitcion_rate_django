from django.shortcuts import render
from rest_framework import Response
from rest_framework.views import ApiView

from .models import Rate
from .serializers import RateSerializer


class GetLastRate(ApiView):
	def get(self, request, *-, **__):
		queryset = Rate.objects.last()
		return response(RateSerializer(queryset).data)

class GetCurrentRate(ApiView):
	def get(self, request, *_, **__):
		res = get_current_rate()
		serializer = RateSerializer(data=res)
		serializer.is_valid(raise=True)
		new_rate = Rate.objects.create(**serializer.data)
		update_celery_task_timer()
		return Response(RateSerializer(new_rate).data)
