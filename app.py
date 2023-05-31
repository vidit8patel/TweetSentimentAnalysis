import streamlit as st
import re
import numpy as np
import pickle
import string
from PIL import Image
from nltk.corpus import stopwords
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()

stop_words = stopwords.words('english')


def cleanTweet(text):
    cleanedTweets = []

    for tweets in text:
        # Converting text to lowercase
        tweets = tweets.lower()

        # Removing newline breaks
        tweets = re.sub(r'\n', '', tweets)

        # Removing URLs
        tweets = re.sub(r"(?:\|http?\://|https?\://|www)\S+", "", tweets)

        # Removing @usernames
        tweets = re.sub('@[^\s]+', '', tweets)

        # Removing punctuations, numbers & special characters
        tweets = re.sub("[^a-zA-Z]", " ", tweets)

        # Removing emojis
        tweets = re.compile("["
                            u"U0001F600-U0001F64F"  # emoticons
                            u"U0001F300-U0001F5FF"  # symbols & pictographs
                            u"U0001F680-U0001F6FF"  # transport & map symbols
                            u"U0001F1E0-U0001F1FF"  # flags (iOS)
                            u"U00002702-U000027B0"
                            u"U000024C2-U0001F251"
                            "]+", flags=re.UNICODE).sub(r'', tweets)

        finaltweet = ''
        # Removing short words(with length less than 3) & stop words
        temp = tweets.split()
        stop_words = stopwords.words('english')
        stop_words = stop_words + ['hi', 'im', 'amp', 'quot']
        textwithoutstopwords = [word for word in temp if not word in stop_words and len(word) > 2]

        # Lemmatization
        lem = WordNetLemmatizer()
        lemmatizedText = [lem.lemmatize(y) for y in textwithoutstopwords]
        finaltweet = ' '.join(lemmatizedText)
        cleanedTweets.append(finaltweet)
    return cleanedTweets


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Sentiment Analysis")
image = Image.open('img.png')
st.image(image)
st.subheader("Enter the tweet/message for which sentiment is to be predicted.")
inputText = []
inputSite = st.text_area("")
inputText.append(inputSite)


if st.button('Predict'):
    cleaned = tfidf.transform(cleanTweet(inputText))
    result = model.predict(cleaned)
    if result:
        st.header("This tweet/message is positive!")
    else:
        st.header("The tweet/message is negative.")