FROM alpine
RUN apk add --no-cache \
  bash \
  logger
COPY entrypoint.sh /app
ENTRYPOINT ["/app/entrypoint.sh"]
