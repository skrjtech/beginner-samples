#!/bin/python
# 必要なパッケージ
# pip install pyzmq
import zmq
import argparse

class Context(object):
    def __init__(self, *args, **kwargs):
        self.Context = zmq.Context()

    def __del__(self):
        self.Context.term()

class REP(Context):
    def __init__(self, host, port, killhost, *args, **kwargs):
        super(REP, self).__init__(*args, **kwargs)
        self.kbind = f"tcp://{killhost}:{killhost}"
        self.rep = self.Context.socket(zmq.REP); self.rep.connect(f"tcp://{host}:{port}")

    def __del__(self):
        self.rep.close()

    def __call__(self, *args, **kwargs):
        while True:
            recv = self.rep.recv_string()
            print("REP: ", recv)
            self.rep.send_string(recv)
            if recv == "KILL": break

def argparses():
    parser = argparse.ArgumentParser("Rep sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Rep Host")
    parser.add_argument("--port", default=5050, type=int, help="Rep Port")
    parser.add_argument("--khost", default="127.0.0.1", type=str, help="Kill Host")
    parser.add_argument("--kport", default=5052, type=int, help="Kill Port")
    return parser.parse_args()

def main():
    args = argparses()
    REP(host=args.host, port=args.port, killhost=args.khost, killport=args.kport)()

def Test():
    HOST = "127.0.0.10"
    REP(host=HOST, port=5050, killhost=HOST, killport=5052)()

if __name__ == '__main__':
    # main()
    Test()