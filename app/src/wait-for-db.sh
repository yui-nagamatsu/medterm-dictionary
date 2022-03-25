#!/bin/bash

set -e

# host = "$1"
# shift

# echo "$host"

# until mysql -h "$host" -P 3306 --silent; do
#   echo 'Waiting for mysqld to be connectable...'
#   sleep 2
# done
sleep 5
echo "db is up!"
exec "$@"