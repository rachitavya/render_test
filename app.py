import pandas as pd
from flask import Flask, render_template

app=Flask(__name__)


@app.route('/',methods=['GET'])
def testing():
    df=pd.read_csv('test.csv')
    country=df['country'][0]
    return render_template('index.html',label=country)

if __name__=='__main__':
     app.run(debug=True)