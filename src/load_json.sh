#!/bin/bash

echo "["

while IFS='=' read -r key value
do
  if [ -z "$value" ]; then
    value=null
  fi
  echo "  {"
  echo "    \"name\": \"$key\","
  echo "    \"slotSetting\": false,"
  echo "    \"value\": \"$value\""
  echo "  },"
done < .env

echo "]"