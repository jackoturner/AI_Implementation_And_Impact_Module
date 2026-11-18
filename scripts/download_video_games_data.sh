#!/usr/bin/env bash

set -e

mkdir -p data/raw

curl --fail --location \
  --output data/raw/Video_Games_5.json.gz \
  https://mcauleylab.ucsd.edu/public_datasets/data/amazon_v2/categoryFilesSmall/Video_Games_5.json.gz