from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/templates/index')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)