#!/bin/python
# 必要なパッケージ
# pip install pyzmq
import zmq
import time
import argparse

class Context(object):
    def __init__(self, *args, **kwargs):
        self.Context = zmq.Context()

    def __del__(self):
        self.Context.term()

class PUB(Context):
    def __init__(self, host="*", port=5050, *args, **kwargs):
        super(PUB, self).__init__(*args, **kwargs)
        self.pub = self.Context.socket(zmq.PUB)
        self.pub.bind(f"tcp://{host}:{port}")

    def __del__(self):
        self.pub.close()

    def __call__(self, *args, **kwargs):
        time.sleep(1)
        self.pub.send_string("KILL")

def argparses():
    parser = argparse.ArgumentParser("Pub sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Pub Host")
    parser.add_argument("--port", default=5050, type=int, help="Pub Port")
    return parser.parse_args()

def main():
    args = argparses()
    PUB(host=args.host, port=args.port)()

def Test():
    HOST = "127.0.0.10"
    PUB(host=HOST, port=5052)()

if __name__ == '__main__':
    # main()
    Test()