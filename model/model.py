import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

from tensorflow.keras.models import load_model
import logging

class EngToFrenchTranslator:

    def __init__(self, model_path, en_tokenizer_path, fr_tokenizer_path):
        logging.info("EngToFrenchTranslator class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")
        logging.info("Loading The English Tokenizer")
        self.eng_tokenizer = tokenizer_from_json(en_tokenizer_path)
        logging.info("English Tokenizer is loaded!")
        logging.info("Loading The French Tokenizer")
        self.fr_tokenizer = tokenizer_from_json(fr_tokenizer_path)
        logging.info("French Tokenizer is loaded!")
        

    def predict(self, sentence):
        y_id_to_word = {value: key for key, value in self.fr_tokenizer.word_index.items()}
        y_id_to_word[0] = '<PAD>'

        sentence = self.eng_tokenizer.texts_to_sequences([sentence])
        
        sentence = pad_sequences(sentence, maxlen=max_eng, padding='post')
        predictions = self.model.predict(sentence)

        return ' '.join([y_id_to_word[np.argmax(x)] for x in predictions[0]])

def main():
	model = EngToFrenchTranslator('final_model.h5', 'english_tokenizer.json', 'french_tokenizer.json')
	predicted_class = model.predict("https://cdn.britannica.com/60/8160-050-08CCEABC/German-shepherd.jpg")
	logging.info("This is an image of a {}".format(predicted_class)) 


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()