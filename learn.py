from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# Could use larger dimensions, but will make training
# times much much longer
img_width, img_height = (128, 72)

train_dir = 'train_data'
test_dir = 'test_data'

num_train_samples = 4000
num_test_samples = 2000
epochs = 20
batch_size = 8

if __name__ == "__main__":
    # If data is formatted to have the channels first,
    # then stick the RGB channels in front, else put them
    # at the end.
    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    # This CNN uses three rounds of convolution

    # First convolution layer
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Second convolution layer
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Third convolution layer
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Convolution is done, so make the fully connected layer
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))

    # Drop 50% of the neurons
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    # It can either be Tide ad or not Tide Ad. 
    # There's only two choices, so binary cross entropy
    # is the loss algorithm of choice
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    # perform random transformations so that the
    # data is more varied
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    # make extra training data by modifying original training images
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    # make extra testing data by modifying original test images
    validation_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    # Train the CNN
    model.fit_generator(
        train_generator,
        steps_per_epoch=num_train_samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=num_test_samples // batch_size)

    # Saved CNN model for use with predictions
    model.save('saved_model.h5')
