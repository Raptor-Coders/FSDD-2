from mailosaur import MailosaurClient
from mailosaur.models import MessageCreateOptions

api_key = "qmhmWcGbuSDVd6031GJ1z7TxO5rMjkIw"
mailosaur = MailosaurClient(api_key)

options = MessageCreateOptions(
  to="paul.krzyz@gmail.com",
  send=True,
  subject='Test mail',
  text='Hello there...'
)


def send_email():
  mailosaur.messages.create("aqrdtfwd", options)