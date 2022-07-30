from flask import Flask,render_template
import pickle
import numpy as np



popular_df = pickle.load(open('popular.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           Author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           Votes=list(popular_df['num_rating'].values),
                           Rating=list(popular_df['avg_rating'].values)

                           )

if __name__ == '__main__':
    app.run(debug=True)
