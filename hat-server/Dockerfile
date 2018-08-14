FROM alpine:3.8

RUN mkdir -p /opt/hat_server/annimations && \
    cd /opt/hat_server/ && \
    apk add --no-cache python3 && \
    pip3 install flask===1.0.2 ipdb ipython pudb

CMD ["/usr/bin/python3", "/opt/hat_server/hat_server.py"]

COPY * /opt/hat_server/
