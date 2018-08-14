FROM python:3.7.0-alpine3.8

RUN mkdir -p /opt/hat_server/annimations && \
    cd /opt/hat_server/ && \
    pip install flask===1.0.2 ipdb ipython pudb

CMD ["/usr/local/bin/python3", "/opt/hat_server/hat_server.py"]

COPY * /opt/hat_server/