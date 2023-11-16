import requests
from flask import Flask, render_template, request, send_file, redirect, url_for
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    pdf_url = request.form.get('pdf_url')
    
    if not pdf_url:
        return render_template('index.html', error='Please enter a PDF URL')

    response = requests.get(pdf_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Serve the PDF for download without saving it to a file
        return send_file(
            io.BytesIO(response.content),
            as_attachment=True,
            download_name='downloaded_file.pdf',
            mimetype='application/pdf'
        )
    else:
        return render_template('index.html', error='Failed to download PDF. Please check the URL.')

if __name__ == '__main__':
    app.run(debug=True)
