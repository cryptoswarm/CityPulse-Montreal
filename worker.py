import logging
import zoneinfo
from time import timezone
from inf5190_projet_src.controllers.data_requester import *
# from inf5190_projet_src import application
from config import JOB_STORES, JOB_DEFAULTS



# def setting_job_1():
#     with application.app_context():
#         persist_patinoir_data()

# def setting_job_2():
#     with application.app_context():
#         persist_aqua_data() 

# def setting_job_3():
#     with application.app_context():
#         persist_glissade_data()


# def setting_job_4():
#     with application.app_context():
#         persist_glissade_data()

# def run_jobs():
#     with application.app_context():
#         scheduler = BackgroundScheduler(jobstores=JOB_STORES, job_defaults=JOB_DEFAULTS)
#         scheduler.add_job(func=setting_job_1, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
#         scheduler.add_job(func=setting_job_2, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
#         scheduler.add_job(func=setting_job_3, trigger='interval', hours=24, timezone=pytz.timezone('CANADA/EASTERN'))
#         scheduler.start()


# if __name__ == "__main__":
#     logging.info('Detected a job to be run at {}'.format(datetime.now()))
#     run_jobs()




