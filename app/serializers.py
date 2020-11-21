from rest_framework.serializers import ModelSerializer

from .models import Rate


class RateSerializer(ModelSerializer):
	class Meta:
		model = Rate
		fields = ['rate', 'checked_at', 'method', 'last_updated']
