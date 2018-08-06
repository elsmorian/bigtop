FROM python:3.7.0-alpine3.8

COPY * /opt/hat_server/

RUN cd /opt/hat_server/ && pip install flask===1.0.2

CMD ["/usr/local/bin/python3 /opt/hat_server/hat_server.py"]