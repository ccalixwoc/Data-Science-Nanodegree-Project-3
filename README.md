# Disaster Respone Pipeline Project

## Table of Contents
1. [Installation](#Installation)
2. [Motivation](#Motivation)
3. [File Descriptions](#FileDescriptions)
4. [Results](#Results)
5. [Licensing, Authors and Acknowledgment](#Licensing,AuthorsandAcknowledgment)

## Installation
To run this project, I used Python 3 and installed the following libraries: 
- numpy
- pandas
- scikit-learn
- plotly
- sqlalchemy
- flask
- json 

## File Structure
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
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 
```

