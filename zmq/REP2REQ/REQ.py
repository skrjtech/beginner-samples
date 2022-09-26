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

class REQ(Context):
    def __init__(self, host="*", port=5050, *args, **kwargs):
        super(REQ, self).__init__(*args, **kwargs)
        self.req = self.Context.socket(zmq.REQ)
        self.req.connect(f"tcp://{host}:{port}")

    def __del__(self):
        self.req.close()

    def __call__(self, *args, **kwargs):
        for idx in range(10):
            self.req.send_string(str(idx))
            time.sleep(1)
            recv = self.req.recv_string()
            print("REQ: ", recv)

def argparses():
    parser = argparse.ArgumentParser("Req sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Req Host")
    parser.add_argument("--port", default=5050, type=int, help="Req Port")
    return parser.parse_args()

def main():
    args = argparses()
    REQ(host=args.host, port=args.port)()

if __name__ == '__main__':
    main()
