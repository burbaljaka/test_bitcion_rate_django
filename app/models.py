from django.db import models

# Create your models here.
class SourceEnum(models.TextChoices):
	manual = 'manual'
	automat = 'automat'


class Rate(models.Model):
	rate = models.FloatField()
	checked_at = models.DateTimeField(auto_now_add=True)
	source = models.CharField(choices=SourceEnum.choices, default=SourceEnum.automat)
	
	def __str__(self):
		return str(rate) + " at " + checked_at.strftime("%d %m %y %H:%m:%s) 
