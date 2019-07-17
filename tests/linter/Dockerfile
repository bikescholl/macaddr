FROM python:3.7.4-alpine3.10
RUN apk add build-base
ADD config/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN adduser -s /bin/sh -u 1000 -D linter
RUN mkdir /scripts
ADD scripts /scripts
RUN chmod -R +x /scripts
USER linter
ENTRYPOINT [ "pylint", "/scripts/mac_addr_lookup.py" ]
