import os
from time import sleep
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    logger.info(f"event: {event}")

    seconds = int(os.environ.get("TIMER"))
    sleep(seconds)

    return {"message": "らーめんが ゆであがりました はやく たべないと のびて しまいます"}
