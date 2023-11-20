from mailosaur import MailosaurClient
from mailosaur.models import MessageCreateOptions

api_key =""
mailosaur = MailosaurClient(api_key)

options = MessageCreateOptions(
    to="paul.krzyz@gmail.com",
    send=True,
    subject='Test mail',
    text='Hello there...'
)

