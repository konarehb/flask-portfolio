from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/templates/index')
def index():
    return render_template('index.html', title='')

if __name__ == '__main__':
    app.run(debug=True)