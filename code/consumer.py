import pika
#import signal
#import sys

#def signal_handler(sig, frame):
#    print('You pressed Ctrl+C!')
#    channel.stop_consuming()
#    channel.close()
#    sys.exit(0)


def callback(ch, method, properties, body):
    print(f"Received {body}")


# attach signal to signal handler
# this will be called when CTRL+C is pressed
# this will allow us to close the connection before we exit
#signal.signal(signal.SIGINT, signal_handler)


# Create a connection to the RabitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='hello')

# Setup a callback function to handle incoming messages
# We need to tell RabbitMQ that this particular callback funciton should receive
#auto_ack=True, allows RabbitMQ to delte the message after it is processed
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print('Waiting for messages.  To exit, press Ctrl+C')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('You pressed Ctrl+C!')
    channel.stop_consuming()
connection.close()
