#Chat room
1. python manage.py migrate
2. python -m pip install channels_redis (if installed, please skip this step)
3. Win: Please install [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/), and run 'docker run -p 6379:6379 -d redis:5' in the installed  'Docker Quickstart Terminal'  
Mac/Linux: Please install [docker for desktop](https://www.docker.com/products/docker-desktop), and run 'docker run -p 6379:6379 -d redis:5' in terminal, and change the IP address in the 'mychat/settings.py' file from 192.168.99.100 to 127.0.0.1
4. python manage.py runserver
5. Open browser, and type in 127.0.0.1:8000/chat/