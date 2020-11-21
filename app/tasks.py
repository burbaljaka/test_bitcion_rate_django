from datetime import timedelta

from celery.task import periodic_task

from .business_logic import get_current_rate


@periodic_task(run_every=timedelta(minutes=1), name='get_current_rate_automatically')
def get_current_rate_automatically():

    res = get_current_rate()
    if not res:
        return
