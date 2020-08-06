import logging
import os
import json
from main.src.broker.connection import Connection
from main.src.logger.config import logger
from main.src.thread.runner import runnerTwitter
import time

log = logging.getLogger(__name__)
logger()


def checkIntegrity(commands):
    if type(commands) is not dict:
        return False
    if not all(k in commands for k in ('sentence', 'request_id')):
        log.error("Missing sentence or request_id parameter")
        return False
    return True


class Message:
    connection = Connection(os.getenv('BROKER_HOST'), os.getenv('BROKER_QUEUE'), os.getenv('BROKER_PORT'))

    def liveReceive(self):
        self.connection.channel.basic_consume(queue=self.connection.queue,
                                              on_message_callback=self.callbackMessage,
                                              auto_ack=True)
        log.info(' [*] Waiting for messages. To exit press CTRL+C')
        self.connection.channel.start_consuming()

    def callbackMessage(self, ch, method, properties, body):
        log.info(' [x] Received ')
        log.info(body)
        runner = json.loads(body)
        if not checkIntegrity(runner):
            log.error(' error: Invalid message')
            return
        time.sleep(5)  # demonstration purpose
        runnerTwitter(runner['sentence'], runner['request_id'])
