#!/usr/bin/env bash
export KALTURA_INSTANCES=2

# export PORT=6500
# PORT ENV VAR IS NOT USED.

export KALTURA_DEFINITIONS_DB='kaldefs.db'
export UPLOAD_FOLDER=/some/valid/folder
export KTS_ADMIN_USER=ktsadmin
export KTS_ADMIN_PWD=ktsadmin

# The following environment variables are only needed if the definitions DB
# doesn't exist and we need to pre-populate it.
# Otherwise just using the GUI works fine too.

# Works for self hosted Kaltura servers
export k_1_ADMIN_SECRET=someSecret
export k_1_KALTURA_CONFIG_ID=1
export k_1_KALTURA_NAME=my_kaltura
export k_1_USER_NAME=username@example.com
export k_1_KALTURA_PATH=my.kaltura.example.com
export k_1_PARTNER_ID=99
export k_1_PLAYER_ID=1234567
export k_1_SECRET=someSecret
export k_1_THUMBNAIL_PLAYER_ID=1234568

# And works for kaltura subscribers too.
export k_2_ADMIN_SECRET=someSecret
export k_2_KALTURA_CONFIG_ID=2
export k_2_KALTURA_NAME=foobar
export k_2_USER_NAME=myKalturaAccount@example.com
export k_2_KALTURA_PATH=www.kaltura.com
export k_2_PARTNER_ID=12345
export k_2_PLAYER_ID=2345095
export k_2_SECRET=someSecret
export k_2_THUMBNAIL_PLAYER_ID=2345092

echo 'initial kaltura configurations: '
python properties.py
# python server.py
# python runtornado.py
# less safe way of killing the process:
# echo 'attempting to kill old process'
# kill -9 $(cat kts.pid)
# echo 'waiting to ensure old processes are killed'
# sleep 10
# better way: 
if ! ps aux  | grep `cat kts.pid` | awk '{print $2}' | grep `cat kts.pid` > /dev/null
then
    echo "Process Does not Exists"
else
    echo "Process Exists"
    kill -9 `cat kts.pid`
    echo "Process Now killed"
fi
echo 'waiting to ensure old processes are killed'
sleep 10

echo 'Starting gunicorn daemon'

nohup gunicorn -w 4 --access-logfile='kts_access.log' --error-logfile='kts_error.log' -b 0.0.0.0:6500 server:app &

echo $! > kts.pid
echo 'Started.'


echo 'Started.'
