FROM python:3.7.4-alpine3.10
ARG API_KEY
ENV API_KEY=$API_KEY
RUN apk add build-base
ADD /config/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN adduser -s /bin/sh -u 1000 -D -H mac_addr
RUN mkdir /scripts
ADD scripts /scripts
RUN chmod -R +x /scripts
USER mac_addr
ENTRYPOINT [ "python", "/scripts/mac_addr_lookup.py" ]
