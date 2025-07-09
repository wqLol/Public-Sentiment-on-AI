import nltk

f = open('input.txt', 'r')
data = f.read()
text = nltk.Text(data.split(" "))
f.close()

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

print(data)
score = analyzer.polarity_scores(data)

print(score)

# print(nltk.FreqDist(text).most_common(50))