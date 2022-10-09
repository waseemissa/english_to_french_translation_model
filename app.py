import os
import logging

from flask import Flask, request, jsonify, render_template

from model.model import EngToFrenchTranslator

app = Flask(__name__)  

# define model, english & french tokenizers paths
model_path = './model/final_model.h5'
en_tokenizer_path = './model/english_tokenizer.json'
fr_tokenizer_path = './model/french_tokenizer.json'

# create instance
model = EngToFrenchTranslator(model_path, en_tokenizer_path, fr_tokenizer_path)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    """Render Our Web Page"""
    return render_template('index.html')


@app.route("/translate", methods=["GET"])
def predict():
    sentence = request.args.get("english_sentence")
    prediction = model.predict(sentence)
    
    logging.info("prediction from model= {}".format(prediction))
    return jsonify({"french_translation": str(prediction)})

def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=8000, debug=False) 


if __name__ == "__main__":
    main()