import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

from tensorflow.keras.models import load_model
from keras.preprocessing import text
from keras_preprocessing.sequence import pad_sequences
import numpy as np
import logging
import json

class EngToFrenchTranslator:

    def __init__(self, model_path, en_tokenizer_path, fr_tokenizer_path):
        logging.info("EngToFrenchTranslator class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")
        logging.info("Loading The English Tokenizer")
        with open(en_tokenizer_path) as f:
            data = json.load(f)
            self.eng_tokenizer = text.tokenizer_from_json(data)
            logging.info("English Tokenizer is loaded!")
        logging.info("Loading The French Tokenizer")
        with open(fr_tokenizer_path) as f:
            data = json.load(f)
            self.fr_tokenizer = text.tokenizer_from_json(data)
            logging.info("French Tokenizer is loaded!")
        

    def predict(self, sentence):
        y_id_to_word = {value: key for key, value in self.fr_tokenizer.word_index.items()}
        y_id_to_word[0] = ''

        sentence = self.eng_tokenizer.texts_to_sequences([sentence])
        
        sentence = pad_sequences(sentence, maxlen=15, padding='post')
        predictions = self.model.predict(sentence)

        return ' '.join([y_id_to_word[np.argmax(x)] for x in predictions[0]])

def main():
	model = EngToFrenchTranslator('final_model.h5', 'english_tokenizer.json', 'french_tokenizer.json')
	predicted_class = model.predict("she is driving the truck")
	logging.info("Translated To French: {}".format(predicted_class)) 


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()