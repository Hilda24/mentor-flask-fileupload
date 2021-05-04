'''
Godlin Hilda J
Sharmila S
Student mentor session - flask - file upload
'''
import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)


app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/upload')
def upload_file():
    print(url_for('static', filename="ro.pdf"))
    return render_template('index.html')
	
    
@app.route('/uploader', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
		


@app.route('/get-info', methods = ['GET', 'POST'])
def get_info():
    if request.method == 'POST':

        f = request.files['file']
        
        f.save(secure_filename(f.filename))
        
        file = open(f.filename,"r")
        line_count = 0
        word_count = 0

        content = file.read()
        line_list = content.split("\n")
        
        for line in line_list:
            word_list = line.split(" ")
            word_count += len(word_list)
            
        for i in line_list:
            if i:
                line_count += 1
		
        print(word_count-1, len(line_list)-1)

        print("This is the number of lines in the file")
        print(line_count)

        print("This is the number of words in the file")
        print(word_count)

        return {
            'line count': line_count,
            'word count': word_count
        }

	
@app.route('/image', methods = ['GET', 'POST'])
def display_image():
    if request.method == 'POST':
        f = request.files['file']

        filename = secure_filename(f.filename)
        print('hhshh---------',  app.config['UPLOAD_FOLDER'] + filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        return render_template('image-display.html', filename = f.filename )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)



