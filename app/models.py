from django.db import models

# Create your models here.
class SourceEnum(models.TextChoices):
	manual = 'manual'
	automat = 'automat'


class Rate(models.Model):
	rate = models.FloatField()
	checked_at = models.DateTimeField(auto_now_add=True)
	method = models.CharField(max_length=10, choices=SourceEnum.choices, default=SourceEnum.automat)
	last_updated = models.DateTimeField()
	
	def __str__(self):
		return str(self.rate) + " at " + self.checked_at.strftime("%d-%m-%Y %H:%M:%S")
