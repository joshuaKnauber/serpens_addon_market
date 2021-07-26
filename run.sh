#!/bin/bash

cd /home/finn/serpens_addon_market/

touch output.log

nohup python serpens_bot.py >> output.log 2>> output.log &

