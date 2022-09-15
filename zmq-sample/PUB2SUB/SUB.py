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

class SUB(Context):
    def __init__(self, host="*", port=5050, channel=1, *args, **kwargs):
        super(SUB, self).__init__(*args, **kwargs)
        self.channel = channel
        self.sub = self.Context.socket(zmq.SUB)
        self.sub.setsockopt_string(zmq.SUBSCRIBE, str(channel))
        self.sub.connect(f"tcp://{host}:{port}")

    def __del__(self):
        self.sub.close()

    def __call__(self, *args, **kwargs):
            recv = self.sub.recv_string()
            print(f"SUB ({self.channel}): ", recv)

def argparses():
    parser = argparse.ArgumentParser("Sub sample")
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Sub Host")
    parser.add_argument("--port", default=5050, type=int, help="Sub Port")
    parser.add_argument("--channel", default=1, type=int, help="Sub Channel")
    return parser.parse_args()

def main():
    args = argparses()
    SUB(host=args.host, port=args.port, channel=args.channel)()

if __name__ == '__main__':
    main()