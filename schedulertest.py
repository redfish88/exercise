# -*- coding:utf-8 -*-

from apscheduler.scheduler import Scheduler
from datetime import datetime

sched = Scheduler()

def some_job():
	print 'hello world'

job = sched.add_date_job(some_job,'2013-01-22 18:32:50')
sched.start()

