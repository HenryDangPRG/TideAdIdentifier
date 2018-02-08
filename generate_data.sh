#!/bin/bash

rm -rf train_data
mkdir train_data
cd train_data

mkdir tide_ads
mkdir non_tide_ads

cd tide_ads && ffmpeg -i ../../tide.avi -vf scale=512:288 -r 5 -f image2 tide-%07d.png
cd ../non_tide_ads && ffmpeg -i ../../non_tide.avi -vf scale=512:288 -r 5 -f image2 nottide-%07d.png
