#!/bin/bash

if [ ! -e /var/log/JumpCloud_flask_container.log ]
then
   sudo touch /var/log/JumpCloud_flask_container.log
fi
sudo chmod 775 /var/log/JumpCloud_flask_container.log
sudo chown root:staff /var/log/JumpCloud_flask_container.log
ls -l /var/log/JumpCloud_flask_container.log
