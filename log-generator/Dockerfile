FROM alpine
RUN apk add --no-cache \
  bash \
  logger
RUN ls
COPY entrypoint.sh /app/
ENTRYPOINT ["/app/entrypoint.sh"]
