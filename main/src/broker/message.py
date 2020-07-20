import logging
import os
import json
from main.src.broker.connection import Connection
from main.src.logger.config import logger
from main.src.thread.runner import runnerTwitter

log = logging.getLogger(__name__)
logger()


def checkIntegrity(commands):
    if not all(k in commands for k in ('sentence', 'request_id')):
        log.error("Missing sentence or request_id parameter")
        return False
    return True


class Message:
    connection = Connection(os.getenv('BROKER_HOST'), os.getenv('BROKER_QUEUE'), 2001)

    def liveReceive(self):
        self.connection.channel.basic_consume(queue=self.connection.queue,
                                              on_message_callback=self.callbackMessage,
                                              auto_ack=True)
        log.info(' [*] Waiting for messages. To exit press CTRL+C')
        self.connection.channel.start_consuming()

    def callbackMessage(self, ch, method, properties, body):
        log.info(' [x] Received ', body)
        runner = json.loads(body)
        if not checkIntegrity(runner):
            log.error(' error: Invalid message')
            return
        runnerTwitter(runner['sentence'], runner['request_id'])
