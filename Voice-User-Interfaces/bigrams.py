from collections import Counter
import utils

def sentence_to_bigrams(sentence):
    """
    Add start '<s>' and stop '</s>' tags to the sentence and tokenize it into a list
    of lower-case words (sentence_tokens) and bigrams (sentence_bigrams)
    :param sentence: string
    :return: list, list
        sentence_tokens: ordered list of words found in the sentence
        sentence_bigrams: a list of ordered two-word tuples found in the sentence
    """
    sentence_tokens = ['<s>'] + sentence.lower().split() + ['</s>']
    sentence_bigrams = []
    for i in range(len(sentence_tokens) - 1):
        sentence_bigrams.append((sentence_tokens[i], sentence_tokens[i+1]))
    return sentence_tokens, sentence_bigrams

def bigrams_from_transcript(filename):
    """
    read a file of sentences, adding start '<s>' and stop '</s>' tags; Tokenize it into a list of lower case words
    and bigrams
    :param filename: string 
        filename: path to a text file consisting of lines of non-puncuated text; assume one sentence per line
    :return: list, list
        tokens: ordered list of words found in the file
        bigrams: a list of ordered two-word tuples found in the file
    """
    tokens = []
    bigrams = []
    with open(filename, 'r') as f:
        for line in f:
            line_tokens, line_bigrams = sentence_to_bigrams(line)
            tokens = tokens + line_tokens
            bigrams = bigrams + line_bigrams
    return tokens, bigrams

def bigram_mle(tokens, bigrams):
    """
    provide a dictionary of probabilities for all bigrams in a corpus of text
    the calculation is based on maximum likelihood estimation and does not include
    any smoothing.  A tag '<unk>' has been added for unknown probabilities.
    :param tokens: list
        tokens: list of all tokens in the corpus
    :param bigrams: list
        bigrams: list of all two word tuples in the corpus
    :return: dict
        bg_mle_dict: a dictionary of bigrams:
            key: tuple of two bigram words, in order OR <unk> key
            value: float probability

    """
    bg_mle_dict = {}
    bg_mle_dict['<unk>'] = 0.

    token_counts = Counter(tokens)
    bigram_counts = Counter(bigrams)
    for bigram in bigram_counts:
        bg_mle_dict[bigram] = bigram_counts[bigram] / token_counts[bigram[0]]
    return bg_mle_dict


def sample_run():
    tokens, bigrams = bigrams_from_transcript('bigram-transcript.txt')
    bg_dict = bigram_mle(tokens, bigrams)
    print(bg_dict)