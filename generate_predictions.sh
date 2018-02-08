#!/bin/bash

rm -rf predictions
mkdir predictions

file="../"
file+="$1"
cd predictions && ffmpeg -i $file -vf scale=512:288 -r 5 -f image2 prediction-%07d.png
