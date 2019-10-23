import os
import tensorflow as tf 
import keras
from keras.applications import MobileNetV2
from keras.layers import GlobalAveragePooling2D, Dense

class Prediction {
    
    def __init__(self, model_weights_path):
        self.model = self.get_model(model_weights_path);
    
    def get_model(self, model_weights_path):
        assert os.path.isfile(model_weights_path), "{} is not a file"
        base_model = MobileNetV2(input_shape=(256, 256, 3), include_top=False);
        x = GlobalAveragePooling2D()(base_model.output)
        x = Dense(1, activation='sigmoid')(x)
        model = Model(inputs=base_model.input, outputs=x)

        model.load_weights(model_weights_path)

        return model

    def predict(self, image):
        pred = model.predict(np.array([image]))
        return pred
        
}