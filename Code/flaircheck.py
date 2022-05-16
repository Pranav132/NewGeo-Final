from flair.models import TextClassifier
from flair.data import Sentence
import csv

classifier = TextClassifier.load('en-sentiment')
sent = ""

f = open('botstuff.txt', 'a')

with open('10000tweets.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # if header row, then move on
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            # getting tweet
            sent = row[2]
            sentence = Sentence(sent)
            classifier.predict(sentence)
            label = str(sentence.labels[0]).split()
            label = label[len(label)-2:]
            f.write(label[0])
            f.write(',')
            f.write(label[1])
            f.write("\n")
            line_count += 1
            print(line_count)
