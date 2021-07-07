FROM alpine
RUN apk add --no-cache \
  bash \
  logger
RUN mkdir /app
COPY ./entrypoint.sh /app/
ENTRYPOINT ["/app/entrypoint.sh"]
