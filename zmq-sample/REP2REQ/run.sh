#!/bin/bash
HOST="127.0.0.1"
PORT=5050
python REP.py --host $HOST --port $PORT & # 先に起動 クライアントからの接続を待つ データを受けってから送信
sleep 1
python REQ.py --host $HOST --port $PORT # 起動後にデータ送信
