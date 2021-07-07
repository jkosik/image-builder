#!/bin/bash

while true; do
  RANDOM=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
  echo "Random string $RANDOM printed to stdout."
  sleep 3
done