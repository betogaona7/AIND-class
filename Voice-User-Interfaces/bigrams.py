from collections import Counter
import numpy as np

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

def bigram_add1_logs(transcript_file):
    """
    provide a smoothed log probability dictionary based on a transcript
    :param transcript_file: string
        transcript_file is the path filename containing unpunctuated text sentences
    :return: dict
        bg_add1_log_dict: dictionary of smoothed bigrams log probabilities including
        tags: <s>: start of sentence, </s>: end of sentence, <unk>: unknown placeholder probability
    """

    tokens, bigrams = bigrams_from_transcript(transcript_file)
    token_counts = Counter(tokens)
    bigram_counts = Counter(bigrams)
    vocab_count = len(token_counts)

    bg_addone_dict = {}
    for bg in bigram_counts:
        bg_addone_dict[bg] = np.log((bigram_counts[bg] + 1.) / (token_counts[bg[0]] + vocab_count))
    bg_addone_dict['<unk>'] = np.log(1. / vocab_count)
    return bg_addone_dict

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

def log_prob_of_sentence(sentence, bigram_log_dict):
    tokens, bigrams = sentence_to_bigrams(sentence)
    total_log_prob = 0.
    for bigram in bigrams:
        if bigram in bigram_log_dict:
            total_log_prob = total_log_prob + bigram_log_dict[bigram]
        else:
            total_log_prob = total_log_prob + bigram_log_dict['<unk>']
    return total_log_prob

test_sentences = [
    'the old man spoke to me',
    'me to spoke man old the',
    'old man me old man me',
]

def sample_run():
    # sample usage by test code (this definition not actually run for the quiz)
    bigram_log_dict = bigram_add1_logs('bigram-transcript.txt')
    for sentence in test_sentences:
        print('*** "{}"'.format(sentence))
        print(log_prob_of_sentence(sentence, bigram_log_dict))