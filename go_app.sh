#!/bin/bash
set -e
LOGFILE=/home/box/web/log/gunicorn/ask.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=10
USER=box
GROUP=box
PORT=8000
cd /home/box/web/ask
exec /home/box/web/ask/gunicorn -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE \
  --bind 0.0.0.0:$PORT
