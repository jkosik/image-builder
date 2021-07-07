FROM alpine
RUN apk add --no-cache \
  bash \
  logger
COPY entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
