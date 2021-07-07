FROM alpine
RUN apk add --no-cache \
  bash \
  logger
COPY . /app
ENTRYPOINT ["/app/entrypoint.sh"]
