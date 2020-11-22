from datetime import timedelta

from django.conf import settings
from celery.task import periodic_task
from loguru import logger

from .business_logic import get_current_rate


@periodic_task(run_every=timedelta(minutes=settings.CRONTAB_MINUTES), name='get_current_rate_automatically')
def get_current_rate_automatically():
    logger.info("Got automatic request to get current rate")
    res = get_current_rate()
    if not res:
        return
    res.save()
