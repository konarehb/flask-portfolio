from flask import Flask, render_template, send_file
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/templates/index')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)

@app.route('/open_cv', methods=['POST'])
def open_cv():
    file_path = 'static/assets/konarehb_cv.pdf'
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int('5000'))