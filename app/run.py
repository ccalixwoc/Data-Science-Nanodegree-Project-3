import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
import plotly.graph_objs as go
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../DisasterResponse.db')
df = pd.read_sql_table('Responses', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    # Data for 1st visual
    df_earthquake = df.groupby(['earthquake','genre']).count().reset_index()
    df_earthquake = df_earthquake[['earthquake','genre', 'id']]
    df_earthquake = df_earthquake.loc[df_earthquake['earthquake'] == 1]
    
    # Data for 2nd visual
    df_genre = df.groupby(['genre']).sum().reset_index()
    df_genre = df_genre.drop(['id'],axis = 1)
    df_genre = pd.melt(df_genre, id_vars = ['genre'])
    direct_messages = df_genre.loc[df_genre['genre'] == 'direct'].sort_values('value',ascending = False)
    
    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x = df_earthquake['genre'],
                    y = df_earthquake['id']
                )
            ],

            'layout': {
                'title': 'Positive Earthquake Message Count by Genre',
                'yaxis': {
                    'title': "Genre"
                },
                'xaxis': {
                    'title': "Message Count"
                }
            }
        },
        {
            'data': [
                Bar(
                    x = direct_messages['variable'],
                    y = direct_messages['value']
                )
            ],

            'layout': {
                'title': 'Direct Message Count by Category',
                'yaxis': {
                    'title': "Message Count"
                },
                'xaxis': {
                    'title': "Category"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        }
    ]
 
    
  # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()