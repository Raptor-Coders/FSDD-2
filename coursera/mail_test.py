from mailosaur import MailosaurClient
from mailosaur.models import MessageCreateOptions


api_key = "..."
mailosaur = MailosaurClient(api_key)


options = MessageCreateOptions(
    to="registered@email",
    send=True,
    subject='Test mail',
    text='Hello there...'
)

mailosaur.messages.create("...", options)
