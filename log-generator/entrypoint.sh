#!/bin/bash

while true; do
  SEC_ELAPSED=$(date +%s%N)
  echo "Random string $SEC_ELAPSED (seconds elapsed) printed to stdout."
  sleep 3
done