#!/usr/bin/with-contenv bashio

DELAY=$(bashio::config 'delay')

echo [backup_cleaner_service] Starting service
while :
do
    python3 cleanup.py
    echo [backup_cleaner_service] Next check in ${DELAY} seconds
    sleep ${DELAY}
done