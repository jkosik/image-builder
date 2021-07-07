FROM alpine
RUN apk add --no-cache \
  bash \
  logger
COPY log-generator/entrypoint.sh /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
