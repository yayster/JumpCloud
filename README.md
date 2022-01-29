# JumpCloud
Cloud Operations Engineer Exercise
---
[The Assignment Sheet](Cloud%20Operations%20Engineer%20Exercise%202021.pdf)
---
## Building and lauching the container 
```
docker build -t flask-app . && docker run -p 8000:5000 --name flask-app-test flask-app
```

## Testing the container

look and run at the script [test.sh](test.sh)

```
curl -i http://127.0.0.1:8000/ && \
curl -i -H "Content-Type: application/json" -X POST -d '{"axion":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"axion":"read","action":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"download"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"read"}' http://127.0.0.1:8000/manage_file 
```

## Logging for observability

My goal would be to injest the STDOUT and STDERR of the container into some log consolidation service.

### [json-logging module](https://github.com/bobbui/json-logging-python)
This module is great to change the logging to json.
However, I am not seeing how to log the request body, which would be important.

I am seeing that there are a lot of other monitoring options as well.

```
docker logs flask-app-test
```
---
---

# Notes on the Task

I had committed to this utilizing [Django](https://www.djangoproject.com/) as a framework.

However, after two days of plunking around with the framework, I grew fatigued trying to navigate all the different configuration files and settings.  What I was stumbling on and getting mired in were so far away from the original objective that the decision to utilize the framework was questioned as the cons heavily outweighed the benefits.  Additionally, the weight of the framework itself is exceptional for the task at hand.  I creating a multi-container app; one container was running Postgres.  This is just too heavy of any application for the task at hand.

So I switched to using Flask instead.   I found a quick tutorial on Flask that gave me everything I needed to accomplish the basic task without getting bogged down in the weeds of the framework.
---
./app.py >> /var/log/flask.log 2>&1


---
## Containerizing

https://stackoverflow.com/questions/41752405/running-flask-app-in-a-docker-container

---
davidkayal@DAVIDs-MBP simple_api % sudo touch /var/log/JumpCloud_flask_container.log
Password:
davidkayal@DAVIDs-MBP simple_api % sudo chmod 775 /var/log/JumpCloud_flask_container.log
davidkayal@DAVIDs-MBP simple_api % sudo chown root:staff /var/log/JumpCloud_flask_container.log
davidkayal@DAVIDs-MBP simple_api % ls -l /var/log/JumpCloud_flask_container.log
-rwxrwxr-x  1 root  staff  0 Jan 14 18:53 /var/log/JumpCloud_flask_container.log
davidkayal@DAVIDs-MBP simple_api % docker

docker logs flask-app-test -f >> /var/log/JumpCloud_flask_container.log 2>&1 &

