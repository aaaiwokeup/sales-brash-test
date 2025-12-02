import time

from apscheduler.schedulers.background import BackgroundScheduler

from run import main

scheduler = BackgroundScheduler()

api_limit = 100
minute_frequency = 1440 / (api_limit * 0.8)

scheduler.add_job(
    main,
    'cron',
    minute=f'*/{int(minute_frequency)}',
    )

scheduler.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
