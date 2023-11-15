import pandas as pd
from flask import Flask, render_template, request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import os

app=Flask(__name__)
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # This creates a local webserver and automatically handles authentication.
drive = GoogleDrive(gauth)

def download_pdf(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as pdf_file:
        pdf_file.write(response.content)


def upload_to_google_drive(file_path, file_name):
    file1 = drive.CreateFile({'title': file_name})
    file1.Upload()
    file1.SetContentFile(file_path)
    file1.Upload()

    return file1['id']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_url = request.form['pdf_url']

        # Download the PDF file
        pdf_file_path = 'downloaded_pdf.pdf'
        download_pdf(pdf_url, pdf_file_path)

        # Upload the PDF file to Google Drive
        uploaded_file_id = upload_to_google_drive(pdf_file_path, 'uploaded_pdf.pdf')

        # Delete the downloaded PDF file
        os.remove(pdf_file_path)

        return render_template('success.html', file_id=uploaded_file_id)

    return render_template('index.html')


# @app.route('/',methods=['GET'])
# def testing():
#     df=pd.read_csv('test.csv')
#     country=df['country'][0]
#     return render_template('index.html',label=country)

if __name__=='__main__':
     app.run(debug=True)



