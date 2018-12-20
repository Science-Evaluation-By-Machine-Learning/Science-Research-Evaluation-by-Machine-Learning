import nltk

word_netlemmatizer = nltk.stem.WordNetLemmatizer().lemmatize('interesting','v')
print(word_netlemmatizer)