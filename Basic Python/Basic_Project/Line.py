from songline import Sendline
token = 'EQYvkWEg6wleHmyZui6ueJSs4g3HblGCSHkov3L3sO6'

messenger = Sendline(token)
while True:
    messenger.sendtext('hello')
    messenger.sticker(620,4)
    messenger.sendimage('https://images.unsplash.com/photo-1681238339260-67f4e6ab5717?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=715&q=80')
