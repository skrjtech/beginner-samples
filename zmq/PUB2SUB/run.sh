#!/bin/bash
HOST="127.0.0.1"
PORT=5050
python PUB.py --host $HOST --port $PORT & # 放送局 起動
for ch in `seq 1 10`
do
  python SUB.py --host $HOST --port $PORT --channel $ch & # 受信機
done