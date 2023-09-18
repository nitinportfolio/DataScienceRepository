import re
import os
import sys
import numpy as np
import pandas as pd
import spacy
import unicodedata
from bs4 import BeautifulSoup
from textblob import TextBlob


from spacy.lang.en.stop_words import STOP_WORDS as stopwords

nlp = spacy.load('en_core_web_lg')

# Word Count
def _get_wordcounts(x):
    length =  len(str(x).split())

    return length

# Character Count
# To remove white spaces
def _get_charcounts(x):
    s = x.split()
    x = ''.join(s)
    return len(x)

# Average WOrd Length
def _get_avg_wordlength(x):
    count = _get_charcounts(x)/_get_wordcounts(x)
    return count

def _get_stopwords_count(x):
    l_stopwords = len([t for t in x.split() if t in stopwords])
    return l_stopwords

def _get_hashtag_counts(x):
    l_hash = len([t for t in x.split() if t.startswith('#')])
    return l_hash

def _get_mentions_counts(x):
    l_mentions = len([t for t in x.split() if t.startswith('@')])
    return l_mentions

def _get_digits_counts(x):
    l_digits =  len([t for t in x.split() if t.isdigit()])
    return l_digits

def _get_uppercase_counts(x):
    l_uppercase = len([t for t in x.split() if t.isupper()])
    return l_uppercase

def _cont_ext(x):

    cList = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it had",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there had",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'alls": "you alls",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had",
    "you'd've": "you would have",
    "you'll": "you you will",
    "you'll've": "you you will have",
    "you're": "you are",
    "you've": "you have"
    }

    if type(x) is str:
        for k in cList:
            value = cList[k]
            x = x.replace(k, value)
        return(x)
    else:
        return(x)

def _get_emails(x):
    emails = re.findall(r'([a-z0-9._-]+@[a-z0-9+._-]+\.[a-z09+_-]+)',x)
    count_emails =  len(emails)
    return emails, count_emails

def _remove_emails(x):
    rem_emails = re.sub(r'([a-z0-9._-]+@[a-z0-9+._-]+\.[a-z09+_-]+)',"",x)
    return rem_emails

def _get_urls(x):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x)
    count_urls = len(urls)
    return urls, count_urls

def _remove_urls(x):
    urls_rem = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',x)
    return urls_rem

def _remove_rt(x):
    rt_rem = re.sub(r'\brt\b', '',x).strip()
    return rt_rem

def _remove_special_chars(x):
    spcl_rem = re.sub(r'[^\w ]+', "", x)
    space_rem = ' '.join(spcl_rem.split())
    return space_rem

def _remove_html_tags(x):
    html_rem = BeautifulSoup(x,"html.parser").get_text().strip()
    return html_rem

def _remove_accented_chars(x):
    accented_rem = unicodedata.normalize('NFKD', x).encode('ascii', errors='ignore').decode('utf-8', errors='ignore')
    return accented_rem

def _remove_stopwords(x):
    stopwords_rem= ' '.join([t for t in text.split() if t not in stopwords])
    return stopwords_rem


def make_base(x):
    x = str(x)
    xlist = []
    doc = nlp(x)

    for token in doc:
        var_lemma = token.lemma_
        if var_lemma == 'PROP' or var_lemma == 'be':
            var_lemma = token.text
        xlist.append(var_lemma)

    return ' '.join(xlist)


def _get_value_counts(df, col):
    text = ' '.join(df[col])
    text = text.split()
    freq = pd.Series(text).value_counts()
    return freq

def _remove_common_words(x, freq, n = 20):

    fw_top_n = freq.head(n)
    cm_rem = ' '.join([t for t in x.split() if t not in fw_top_n])
    return cm_rem

def _remove_rare_words(x,freq, n=20):

    fw_bt_n = freq.tail(n)
    rw_rem = ' '.join([t for t in x.split() if t not in fw_bt_n])
    return rw_rem

def _spelling_correction(x):
    spell_corr = TextBlob(x).correct()
    return spell_corr














