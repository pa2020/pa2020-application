import pika
import os


class Connection:
    def __init__(self, host, queue, port):
        self.queue = queue
        credentials = pika.PlainCredentials(os.getenv('BROKER_USER'), os.getenv('BROKER_PASSWORD'))
        params = pika.ConnectionParameters(host, port, os.getenv('BROKER_VHOST'), credentials=credentials)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=True)

    def close(self):
        self.connection.close()
