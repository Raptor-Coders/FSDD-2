import pika

def callback(ch, method, properties, body):
    print(f"Received {body}")

#  Create a conection to the RabbitMQ server. The BlockingConnection creates
#  a layer on top of Pika’s asynchronous core providing methods that will block until their
# expected response has returned.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#  Declare the same queue
channel.queue_declare(queue='hello')

# Set up a callback function to handle incoming messages
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for messages. To exit, press Ctrl+C')
channel.start_consuming()