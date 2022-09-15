# 必要なパッケージ
# pip install pyzmq
import zmq
import time
import argparse

class Context(object):
    def __init__(self, *args, **kwargs):
        self.Context = zmq.Context()

    def __del__(self):
        self.Context.destroy()

class REP(Context):
    def __init__(self, host="*", port=5050, *args, **kwargs):
        super(REP, self).__init__(*args, **kwargs)
        self.rep = self.Context.socket(zmq.REP)
        self.rep.bind(f"tcp://{host}:{port}")

    def __del__(self):
        self.rep.close()

    def __call__(self, *args, **kwargs):

        for idx in range(10):
            recv = self.rep.recv_string()
            print("REP: ", recv)
            time.sleep(1)
            self.rep.send_string(recv)

def argparses():
    parser = argparse.ArgumentParser("Rep sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Rep Host")
    parser.add_argument("--port", default=5050, type=int, help="Rep Port")
    return parser.parse_args()

def main():
    args = argparses()
    REP(host=args.host, port=args.port)()

if __name__ == '__main__':
    main()
