import csv
import spacy

# Loading pre-trained model from spacy
nlp = spacy.load("en_core_web_lg")

def calculate_similarity(text1, text2):
    # Process text with spaCy model
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
# Calculate similarity score
    similarity_score = doc1.similarity(doc2)
    return similarity_score

# Open the input CSV file
with open('DataNeuron_Text_Similarity.csv', 'r', newline='', encoding='utf-8') as infile:
    csvreader = csv.DictReader(infile)
    
# Preparing output CSV file
    with open('results.csv', 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['text1', 'text2', 'similarity_score']
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
        csvwriter.writeheader()

        for row in csvreader:
            text1 = row['text1']
            text2 = row['text2']
            
# Calculating similarity score
            similarity_score = calculate_similarity(text1, text2)
            
# Writing the output CSV file
            csvwriter.writerow({'text1': text1, 'text2': text2, 'similarity_score': similarity_score})

print("!")
