#### Simple chat application

Application run in docker. To build image clone repo and run:
```commandline
docker build -t simple_chat:v.1.0 .
```
To run allpication run:
```commandline
docker run -p 8888:8000 simple_chat:v.1.0
```
Server available on http://127.0.0.1:8888/

Database already filled with some data.
Available endpoints:
- [admin/](http://127.0.0.1:8888/admin/) - for login use **username=chat_admin, password=1111**.
- **api/api-token-auth/** - to get auth-token. Send POST-request with
**Body form-data with username=User_1, password=1111** using Postman or something else.
- **api/thread/** - create thread. Send POST-request with headers 
**Authorization: Token <token_you_get>** and Body raw json, for example **{"participants": [2, 3, 4]}**.
- **api/thread/thread_id/delete/** - delete thread. Send DELETE-request with token and thread_id(example=1) in URL.
- **api/thread/thread_id/messages/** - get thread messages. Send GET-request with token and thread_id(example=1) in URL.
- **api/user/user_id/threads/** - get user threads. Send GET-request with token and user_id(example=2) in URL.
- **api/user/user_id/new_message/** - create message. Send POST-request with token and Body raw json, 
for example **{"text": "Some text", "thread": 1}** and user_id(example=2) in URL.
- **api/user/user_id/unread/** - user's unread messages. Send GET-request with token and user_id(example=2) in URL.
- **api/message/message_id/** - mark message as read. Send POST-request with token message_id(example=3) in URL.

Have a nice day)
