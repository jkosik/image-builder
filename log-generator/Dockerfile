FROM alpine
RUN apk add --no-cache \
  bash \
  logger

COPY log-generator/entrypoint.sh /app/entrypoint.sh

RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]
