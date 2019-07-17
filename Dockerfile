FROM python:3.7.4-alpine3.10
ARG access_key
ARG mac_address
ENV mac_address=$mac_address
ENV key=$access_key
ADD /config/requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt
RUN adduser -s /bin/sh -u 1000 -D -H mac_addr
ADD config/resolv.conf /etc/resolv.conf
RUN mkdir /scripts
ADD scripts /scripts
RUN chmod -R +x /scripts
USER mac_addr
#ENTRYPOINT [ "/bin/sh", "/scripts/start.sh" ]
