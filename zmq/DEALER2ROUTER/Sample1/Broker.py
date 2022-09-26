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

class Dealer2Router(Context):
    def __init__(self, frontendhost, frontendport, backendhost, backendport, killhost, killport, *args, **kwargs):
        super(Dealer2Router, self).__init__(*args, **kwargs)
        self.f = f"tcp://{frontendhost}:{frontendport}"
        self.b = f"tcp://{backendhost}:{backendport}"
        self.k = f"tcp://{killhost}:{killport}"
        self.Initializer()

    def Initializer(self):
        self.frontend = self.Context.socket(zmq.DEALER); self.frontend.bind(self.f) # REP <-> DEALER
        self.backend = self.Context.socket(zmq.ROUTER); self.backend.bind(self.b)   # REQ <-> ROUTER
        self.killsignal = self.Context.socket(zmq.SUB); self.killsignal.connect(self.k); self.killsignal.setsockopt(zmq.SUBSCRIBE, b'') # KILL SIGNAL GET

        self.poller = zmq.Poller()
        self.poller.register(self.killsignal, zmq.POLLIN)  # KILL信号 シグナル受信でエグジット
        self.poller.register(self.frontend, zmq.POLLIN)
        self.poller.register(self.backend, zmq.POLLIN)

    def __del__(self):
        self.killsignal.close()
        self.frontend.close()
        self.backend.close()

    def __call__(self, *args, **kwargs):
        self.Run()

    def Proxy(self):
        try:
            zmq.proxy(self.frontend, self.backend)
        except zmq.ContextTerminated:
            return

    def Run(self):
        # socks = dict(self.poller.poll())  # <- 記述場所に注意 (1
        while True:
            socks = dict(self.poller.poll()) # <- 記述場所に注意 (2
            if socks.get(self.frontend) == zmq.POLLIN:
                msg = self.frontend.recv_multipart()
                self.backend.send_multipart(msg)
            if socks.get(self.backend) == zmq.POLLIN:
                msg = self.backend.recv_multipart()
                self.frontend.send_multipart(msg)
            if socks.get(self.killsignal) == zmq.POLLIN:
                break

def argparses():
    parser = argparse.ArgumentParser("Sub sample")
    parser.add_argument("--fhost", default="127.0.0.1", type=str, help="Frontend Host")
    parser.add_argument("--fport", default=5050, type=int, help="Frontend Port")
    parser.add_argument("--bhost", default="127.0.0.1", type=str, help="Backend Host")
    parser.add_argument("--bport", default=5051, type=int, help="Backend Port")
    parser.add_argument("--khost", default="127.0.0.1", type=str, help="Kill Host")
    parser.add_argument("--kport", default=5052, type=int, help="Kill Port")
    return parser.parse_args()

def main():
    args = argparses()
    Dealer2Router(frontendhost=args.fhost, frontendport=args.fport, backendhost=args.bhost, backendport=args.bport, killhost=args.khost, killport=args.kport)()

def Test():
    HOST = "127.0.0.10"
    Dealer2Router(frontendhost=HOST, frontendport=5050, backendhost=HOST, backendport=5051, killhost=HOST, killport=5052)()

if __name__ == '__main__':
    # main()
    Test()