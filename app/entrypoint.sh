#!/bin/sh

set -e

python3 -m flask init-db

python3 -m flask run --host=0.0.0.0
