from library.message.adapter.adapter import Adapter
import pika
import json

class rmq(Adapter):
    def __init__(self):
        print('rmq::__init__')

    def connect(self):
        print('rmq::connect')
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def get_contents(self):
        print('rmq::get_contents')
        with self.conn as connection:
            with connection.channel() as channel:
                channel.queue_declare(self.config['queue_name'], False, True)
                # channel.basic.qos(10)
                channel.basic_consume(self.config['queue_name'], on_message_callback=self.on_message, auto_ack=True)
                try:
                    print(' [*] Waiting for messages. To exit press CTRL+C')
                    channel.start_consuming()
                except KeyboardInterrupt:
                    channel.close()

    def on_message(self, ch, method, properties, body):
        print('rmq::on_message')
        # to_blockchain(json.loads(body)['test'])

    def return_status(self):
        print('rmq::return_status')
        with self.conn as connection:
            with connection.channel() as channel:
                properties = {
                    'content_type': 'application/json',
                    'headers': {'Status': 'OK'}
                }
                message = Message.create(channel, '{"status":"OK"}', properties)
                message.publish(self.config['queue_name_return_status'])

