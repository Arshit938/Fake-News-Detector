import joblib
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import numpy as np
ps = PorterStemmer()
def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [ps.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

model=joblib.load('news_detector.joblib')
vector=joblib.load('text_to_num.joblib')

def detect(query):
    ip=vector.transform([query])
    pred=model.predict(ip)
    if pred[0] == 0:
        return True
    else:
        return False


# detect(stemming('Arshit ankit is mental'))

