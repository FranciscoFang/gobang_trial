import tensorflow as tf

def make_models():
    model1 = tf.keras.models.Sequential()
    model1.add(tf.keras.layers.Conv2D(filters=2, kernel_size=(5,5), strides=1, activation='relu', input_shape=(15,15,2)))
    model1.add(tf.keras.layers.Dropout(0.1))
    model1.add(tf.keras.layers.Conv2D(filters=2, kernel_size=(5,5), strides=1, activation='relu'))
    model1.add(tf.keras.layers.Dropout(0.1))
    model1.add(tf.keras.layers.Conv2D(filters=9, kernel_size=(3,3), strides=1, activation='relu'))
    model1.add(tf.keras.layers.Dropout(0.1))
    model1.add(tf.keras.layers.Reshape((15,15)))
    model1.compile(optimizer="adam", loss=tf.keras.losses.BinaryCrossentropy(), metrics=["accuracy"])
    model1.summary()
    model2 = tf.keras.models.Sequential()
    model2.add(tf.keras.layers.Conv2D(filters=2, kernel_size=(5,5), strides=1, activation='relu', input_shape=(15,15,2)))
    model2.add(tf.keras.layers.Dropout(0.1))
    model2.add(tf.keras.layers.Conv2D(filters=2, kernel_size=(5,5), strides=1, activation='relu'))
    model2.add(tf.keras.layers.Dropout(0.1))
    model2.add(tf.keras.layers.Conv2D(filters=9, kernel_size=(3,3), strides=1, activation='relu'))
    model2.add(tf.keras.layers.Dropout(0.1))
    model2.add(tf.keras.layers.Reshape((15,15)))
    model2.compile(optimizer="adam", loss=tf.keras.losses.BinaryCrossentropy(), metrics=["accuracy"])
    model2.summary()
    return model1, model2