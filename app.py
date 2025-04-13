from flask import Flask, render_template, redirect
import datetime

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
@app.route('/templates/index')
def index():
    # Obtention de l'année actuelle
    current_year = datetime.datetime.now().year
    # Rendu du template 'index.html' avec l'année actuelle comme variable
    return render_template('index.html', current_year=current_year)

# Route pour télécharger le CV
@app.route('/view_resume', methods=['POST'])
def open_cv():
    # Chemin vers le fichier PDF du CV
    file_path = 'https://f003.backblazeb2.com/file/buymymusic-app/ASSETS/resume.pdf'
    # Envoi du fichier PDF en réponse à la requête
    return redirect(file_path)

if __name__ == '__main__':
    # Lancement de l'application Flask en mode débogage sur toutes les interfaces sur le port 5000
    app.run(debug=True, host='0.0.0.0', port=int('5500'))