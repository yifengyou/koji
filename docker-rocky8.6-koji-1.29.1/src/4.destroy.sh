#!/bin/bash

set -e

docker container prune -f
docker container rm --force rocky8.6-koji

echo "All done!"
