from mailosaur import MailosaurClient
from mailosaur.models import MessageCreateOptions

api_key = "qmhmWcGbuSDVd6031GJ1z7TxO5rMjkIw"
mailosaur = MailosaurClient(api_key)

options = MessageCreateOptions(
  to="akin11235@gmail.com",
  send=True,
  subject='Test mail',
  text='Hello there...'
)


def send_email():
  mailosaur.messages.create("aqrdtfwd", options)

def new_student_mailer():
  mailosaur.messages.create("aqrdtfwd", options=MessageCreateOptions(
    to="akin11235@gmail.com",
    send=True,
    subject='Welcome Message',
    text='Thanks for joining the course'
  ))


def new_subscription_mailer():
  mailosaur.messages.create("aqrdtfwd", options=MessageCreateOptions(
    to="akin11235@gmail.com",
    send=True,
    subject='New Subscription Email',
    text='Thanks for signing up!'
  ))


def new_contact_mailer():
  mailosaur.messages.create("aqrdtfwd", options=MessageCreateOptions(
    to="akin11235@gmail.com",
    send=True,
    subject='New Contact Entity',
    text='Now we got you!'
  ))