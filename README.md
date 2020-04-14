# Chat room
### How to run on localhost:
For Mac or Linux, please use python3
1. python manage.py migrate
2. python -m pip install channels_redis (if installed, please skip this step)
3. Win: Please install [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/), and run 'docker run -p 6379:6379 -d redis:5' in the installed  'Docker Quickstart Terminal'  
Mac/Linux: Please install [docker for desktop](https://www.docker.com/products/docker-desktop), and run 'docker run -p 6379:6379 -d redis:5' in terminal, and change the IP address in the 'mychat/settings.py' file from 192.168.99.100 to 127.0.0.1
4. python manage.py runserver
5. Open browser, and type in 127.0.0.1:8000/chat/


### Changes on AWS EC2:
1. mychat/setting.py  
From ALLOWED_HOSTS = []  
To ALLOWED_HOSTS = ['*',]

     From "hosts": [('127.0.0.1', 6379)],  
     To "hosts": [('chatroom-redis-001.evowxw.0001.use2.cache.amazonaws.com',6379)],
2. Run command: python3 manage.py runserver 0.0.0.0:9000
3. URL: http://ec2-3-16-186-223.us-east-2.compute.amazonaws.com:9000/chat/