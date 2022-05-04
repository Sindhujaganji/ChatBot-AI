# ChatBot-AI
ChatBot using AI for user interaction
# Weather Forecasting Chatbot Documentation


This project is to create a generalized chatbot which can interact with the customers and resolve their issues without wasting time, money and manpower. 

This can be used later for any other purpose by making a few changes.

To create this chatbot we have used **Natural Language Processing**, a powerful tool which makes computer understand what humans write and speak, as well as **Conversational AI**, combines NLP and chatbot which helps customers to interact.

**Files** Below are the procedures or files with which we have designed chatbot.

> **Training.py** Here we trained the chatbot with the dataset we streamed and processed it for next revolution. We made numpy vector arrays out of the dataset to make train_x and train_y, so that we can fit our model with it. 

>**Testing.py** We will test our built model with a user's query. First, we had to process the query into a vector array so that we could fit it to the model for prediction. Then we predict the result with the help of the saved model. If the prediction matches any class, we fetch the class, get the response and show it to the user.

> **Weather.py** When a user’s query is about to know the weather news, the chatbot will predict the certain keyword. After getting the certain keyword, we will start our forecasting service. We can fetch the API by logging into any weather forecasting website.  Later, connect to the weather database by using API key. Before that, we must fetch the city name from the user's query. Then, we will find the longitude and latitude of that city, pasted these on our API key and then get the live weather news of that city. We can show this information in a html view by using flask.

> **Intents.json** We have initialized a json format dataset where we added some patterns with their respective responses. And we added classes to every pattern set, so that chatbot model can easily recognize pattern’s origin.'

**Libraries** To make this project work few libraries need to be imported. They are listed below:
import nltk
import random, json , pickle
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
from nltk import flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD
from flask import Flask, render_template, request


### Executing this project
Make sure the path is correct and all required libraries are installed.

>>>python weather.py (it will run all the modules and a HTTP link will be displayed)

Copy that URL and paste it in the browser. Chatbot interface will be displayed and you can get response for your queries. 

**Future Work** By changing the dataset for related sectors, we can make chatbot in any kind of intention based chatbot like school chatbot, industrial chatbot, bank chatbot etc. No need to change the models.`
