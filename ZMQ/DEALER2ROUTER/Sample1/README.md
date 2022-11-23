# ブローカーの構成
REP 受信 <- REQ 送信の順で通信 (KILLSIGNALで通信終了)
```
. run.sh
```
連結仕組み
1) REP <- [ DEALER <-> ROUTER ] <- REQ OK!
2) REP -> [ DEALER <-> ROUTER ] -> REQ NG!
