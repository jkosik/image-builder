#!/bin/bash

while true; do
  RANDOM=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 10 ; echo '')
  echo "Random string $RANDOM printed to stdout."
  logger -i "Random string $RANDOM printed to syslog."
  sleep 3
done