import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

print("\n")
#using the first function from the nltk package
print(word_tokenize(text))
print("\n")
#function that separates the text by sentences.
print(nltk.tokenize.sent_tokenize(text))

print("\n")
stopwords = stopwords.words("english")
new_text=[]

for i in text.split():
    if i not in stopwords:
        new_text.append(i)
# Print statement 3
print(new_text)
