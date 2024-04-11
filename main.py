# Part A: Model Building

import spacy
from flask import Flask, request, jsonify, send_from_directory , render_template

# Loading the pre-trained model
nlp = spacy.load("en_core_web_lg")


def calculate_similarity(text1, text2):
    # Process text with spaCy model
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
# Similarity score
    similarity_score = doc1.similarity(doc2)
    return similarity_score

#Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_similarity', methods=['POST'])
def calculate_similarity_endpoint():
    # Get text1 and text2 from request body
    data = request.get_json()
    text1 = data['text1']
    text2 = data['text2']
    
#Similarity score
    similarity_score = calculate_similarity(text1, text2)
    
#Response body
    response = {
        'similarity score': similarity_score
    }
    
#Response
    return jsonify(response)

