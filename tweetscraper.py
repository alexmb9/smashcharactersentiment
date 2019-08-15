#TWITTER SMASH ULTIMATE CHARACTER SENTIMENT

# -*- coding: utf-8 -*-

import tweepy
import csv
import json

#enter your keys inbetween green quotation marks

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Maximum number of tweets to be extracted

maximum_number_of_tweets_to_be_extracted = 300
charactername=input('Enter a name of a smash character:')
smashcharacter=(charactername+' smash')

#writes every tweet onto a text file with the query and encodes it in utf-8

for tweet in tweepy.Cursor(api.search, q=smashcharacter,
rpp=750).items(maximum_number_of_tweets_to_be_extracted):
    with open('smashcharactersentiment' + '.txt', 'a') as \
    the_file:
            the_file.write(str(tweet.text.encode('utf-8')) + '\n')

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \
,'smash ultimate', charactername, 'related tweets.')

open

def countsentiment():

    #decoding textfile
    
    with open("smashcharactersentiment.txt", "rb") as f:
        text = f.read().rstrip()  # rstrip to remove trailing spaces
        decoded = text.decode('unicode-escape').encode('latin1').decode('utf-8')
    with open("sentimentcounter.txt", "wb") as f:
        f.write(decoded.encode('unicode-escape'+'\n'))

    #Opening decoded textfile and splitting into list                                       

    hatecounter=0
    likecounter=0

    with open('sentimentcounter.txt', "r") as word_list:
        words = word_list.read().split(' ')

    #Sentiment calculator

    likes=words.count('like')
    loves=words.count('love')
    goods=words.count('good')
    bests=words.count('best')

    positivesentiment=likes+loves+goods+bests

    dislikes=words.count('dislike')
    hates=words.count('hate')
    bads=words.count('bad')
    worsts=words.count('worst')

    negativesentiment=dislikes+hates+bads+worsts
 
    print(charactername, 'positive twitter sentiment:', positivesentiment)
    print(charactername, 'negative twitter sentiment:', negativesentiment)

    #Cleans textfiles

    open('sentimentcounter.txt', 'w').close()
    open('smashcharactersentiment.txt', 'w').close()

countsentiment()


        


                


