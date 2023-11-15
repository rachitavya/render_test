from flask import Flask, render_template, request, send_file
import requests
import os

app = Flask(__name__)

def download_pdf(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as pdf_file:
        pdf_file.write(response.content)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_url = request.form['pdf_url']

        # Download the PDF file
        pdf_file_path = 'downloaded_pdf.pdf'
        print(pdf_file_path)
        download_pdf(pdf_url, pdf_file_path)
        print('reached point 2')

        # Send the PDF file as an attachment for the user to download
        return send_file(pdf_file_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
