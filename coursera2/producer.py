import pika

#  Create a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

#  Publish a message to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, World from FSDD2!')

print("Sent 'Hello, World!'")

#  Close the connection
connection.close()
