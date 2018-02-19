"""Splitting text data into tokens."""

import re

def sent_tokenize(text):
    """Split text into sentences."""
    
    # Split text by sentence delimiters 
    sentences = re.split(r'([A-Z][^\.!?]*[\.!?])', text)
    # Remove leading and trailing spaces from each sentence
    clean_sentences = []
    for sentence in sentences:
        if len(sentence) > 1 and sentence != ' ':
            clean_sentence = sentence.replace('.','')
            clean_sentence = clean_sentence.replace('?','')
            clean_sentences.append(clean_sentence)
            
    return clean_sentences
    


def word_tokenize(sent):
    """Split a sentence into words."""
    
    # Split sent by word delimiters 
    words = re.split(r' ', sent)
    return words  


def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")
    
    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)
    
    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability