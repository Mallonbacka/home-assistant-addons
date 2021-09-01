ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install Python and Requests
RUN apk add --no-cache python3
RUN apk add --no-cache py3-requests

# Copy data for add-on
COPY run.sh /
COPY cleanup.py /
RUN chmod a+x /run.sh

CMD [ "./run.sh" ]
