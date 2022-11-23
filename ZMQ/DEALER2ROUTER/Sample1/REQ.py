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

class REQ(Context):
    def __init__(self, host, port, killhost, killport, *args, **kwargs):
        super(REQ, self).__init__(*args, **kwargs)
        self.kbind = f"tcp://{killhost}:{killport}"
        self.req = self.Context.socket(zmq.REQ); self.req.connect(f"tcp://{host}:{port}")
        self.killsignal = self.Context.socket(zmq.PUB); self.killsignal.bind(self.kbind)

    def __del__(self):
        self.req.close()
        self.killsignal.close()

    def __call__(self, *args, **kwargs):
        for idx in range(10):
            self.req.send_string(str(idx))
            recv = self.req.recv_string()
            print("REQ: ", recv)
        self.Kill()

    def Kill(self):
        self.req.send_string("KILL")
        self.req.recv_string()
        time.sleep(1)  # <- これ重要 スリープしないと受信ソケットが閉じられ正常にキルができない
        self.killsignal.send_string("KILL")
        print("KILL: Send")

def argparses():
    parser = argparse.ArgumentParser("Rep sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Rep Host")
    parser.add_argument("--port", default=5051, type=int, help="Rep Port")
    parser.add_argument("--khost", default="127.0.0.1", type=str, help="Kill Host")
    parser.add_argument("--kport", default=5052, type=int, help="Kill Port")
    return parser.parse_args()

def main():
    args = argparses()
    REQ(host=args.host, port=args.port, killhost=args.khost, killport=args.kport)()

def Test():
    HOST = "127.0.0.10"
    REQ(host=HOST, port=5051, killhost=HOST, killport=5052)()

if __name__ == '__main__':
    # main()
    Test()