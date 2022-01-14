# JumpCloud
Cloud Operations Engineer Exercise
---
[The Assignment Sheet](Cloud%20Operations%20Engineer%20Exercise%202021.pdf)
---
```
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"download"}' http://localhost:5000/manage_file

curl -i -H "Content-Type: application/json" -X POST -d '{"action":"read"}' http://localhost:5000/manage_file
```
---
I had committed to this utilizing [Django](https://www.djangoproject.com/) as a framework.

However, after two days of plunking around with the framework, I grew fatigued trying to navigate all the different configuration files and settings.  What I was stumbling on and getting mired in were so far away from the original objective that the decision to utilize the framework was questioned as the cons heavily outweighed the benefits.  Additionally, the weight of the framework itself is exceptional for the task at hand.

So I switched to using Flask instead.   I found a quick tutorial on Flask that gave me everything I needed to accomplish the basic task without getting bogged down in the weeds of the framework.
---

