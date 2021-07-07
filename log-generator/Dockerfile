FROM alpine
RUN apk add --no-cache \
  bash \
  logger
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
