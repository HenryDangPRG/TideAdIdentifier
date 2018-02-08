import numpy as np
import subprocess
from keras.preprocessing import image
from keras.models import load_model

def img_to_array(file_name):
    loaded_img = image.load_img(file_name, target_size=(img_width, img_height))
    img_array = image.img_to_array(loaded_img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

if __name__ == "__main__":
    directory = "predictions/"
    num_images = int(subprocess.getoutput("ls predictions | wc -l"))
    img_width, img_height = (128, 72)

    # load the saved model, and use it for prediction
    model = load_model("saved_model.h5")
    images = []

    for i in range(1, num_images+1):
        # Need up to 6 leading zeroes for formatting
        i_ = "{:0>7}".format(i)
        next_img = img_to_array(directory + "prediction-" + str(i_) + ".png")
        images.append(next_img)  
    images = np.vstack(images) 
    prediction = model.predict(images) 
    percent_tide = sum(prediction)[0] * 100 / num_images

    print("There is a " + str(percent_tide) + "% chance this is not a Tide ad.")

    # If more than half the images are NOT Tide ads
    if(sum(prediction) >= num_images / 2):
        print("It can be concluded that this is NOT a Tide ad!")
    else:
        print("It can be concluded that this IS a Tide ad!")
