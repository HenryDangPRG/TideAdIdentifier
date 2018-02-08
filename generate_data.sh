#!/bin/bash

rm -rf tide_ads
rm -rf non_tide_ads

mkdir tide_ads
mkdir non_tide_ads
cd tide_ads && ffmpeg -i ../tide.avi -r 5 -f image2 image-%07d.png
cd ../non_tide_ads && ffmpeg -i ../non_tide.avi -r 5 -f image2 image-%07d.png
