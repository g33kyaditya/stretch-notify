#!/bin/python

from apscheduler.schedulers.background import BlockingScheduler
import notify2
import time
import subprocess
import logging

def stretch():
    notify2.init('Stretch')
    n = notify2.Notification('Get Up !', 'Time to stretch a bit ')
    n.show()
    subprocess.call(['espeak', '-g', '5', 'Get Up. Time to Stretch' ])
    time.sleep(600)
    n = notify2.Notification('Enough Rest', 'Get back to work ')
    n.show();
    subprocess.call(['espeak', '-g', '5', 'Get back to work' ])



logging.basicConfig()
scheduler = BlockingScheduler()
scheduler.add_job(stretch, 'interval', hours = 1)
scheduler.start()
