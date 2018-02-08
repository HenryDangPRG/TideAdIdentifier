# TideAdIdentifier

TideAdIdentifier is a convolutional neural network that is capable of determining whether a video is a Tide ad or not.
It can also be re-trained with more data to increase the accuracy of its predictions.

To train TideAdIntififier, simply clone this repository and place five files in the directory: 

1. non_tide.avi : an avi file containing ads that are NOT Tide ads.
2. tide.avi : an avi file containing Tide ads
3. tide_test.avi : an avi containing a Tide ad that is NOT included in tide.avi
4. non_tide_test.avi : an avi file contaning ads that are NOT Tide ads and NOT in non_tide.avi
5. Any .avi file that is an ad (for prediction)

Once you have all five of these files in the same directory, run 

`./generate_data.sh`

then 

`./generate_predictions.sh`

and finally 

`generate_tests.sh AVI_FILE_NAME`

where *AVI_FILE_NAME* is the name of the avi file that you want to use for prediction.

Next, train the CNN by running

`python3 learn.py`

Then, you can use the trained CNN for prediction by running :

`python3 predict.py`

## Effectiveness

For most ads, TideAdIdentifier will produce a certainty percentage of around 30-70%, unless you input one
of the ads that was used in the training set.

To improve TideAdIdentifier's accuracy, use more data (longer videos) and train for more epochs. 
Increasing the dimensions of TideAdIdentifier's images may also increase accuracy as well.
