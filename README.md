# Disaster Respone Pipeline Project

## Table of Contents
1. [Installation](#Installation)
2. [Motivation](#Motivation)
3. [File Structure](#FileStructure)
4. [Licensing, Authors and Acknowledgment](#Licensing,AuthorsandAcknowledgment)

## Installation
To run this project, I used Python 3 and installed the following libraries: 
- numpy
- pandas
- scikit-learn
- plotly
- sqlalchemy
- flask
- json 

## Motivation
This project consists in a machine learning model that takes disaster-related messages and classifies it into several categories according to their content. Notably, this project showcases my abilities to streamline data preprocessing and machine learning feature engineering through pipelines. This project focuses on natural language processing techniques such as stemming, tokenization, etc.

## File Structure
To run this file, use the 'run.py' file. This will allow you to display the html site on your browser. The app folder contains all the files related to the frontend and backend of the project. The data folder contains the raw data and a preprocessed database. The models folder contains the machine learning model.

```
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- Responses.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 
```
## Results
A glance at the classifier. Enter a text message on the textbox and it will classify it into several categories. Below you can see data exploration charts that were created using Plotly.

![Classifier](https://github.com/ccalixwoc/Data-Science-Nanodegree-Project-3/blob/master/Classifier-img.JPG)

## Licensing, Authors and Acknowledgment
All data was provided through the Data Science Nanodegree.
