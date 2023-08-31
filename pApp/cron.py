
import logging
logger = logging.getLogger(__name__)


def my_cron_job():
    # your functionality goes here
    print("Hello")
    logger.info("Cron Job called")
