from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/tuto/')
def home():
	return render_template('le_tuto_entier.html')


@app.route('/contact/')
def contact():
	return render_template('contact.html')

@app.route('/vocabulaire.html')
def vocabulaire():
	return render_template('vocabulaire.html')

@app.route('/Grammaire.html')
def Grammaire():
	return render_template('Grammaire.html')

@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
    	print(request.form['pseudo'])
    	return 'salut ' + request.form['pseudo']
 		

if __name__ == '__main__':
	app.run(debug=True)

#@app.errorhandler(404)
#def page_not_found(erreur_404):
#    return render_template('erreur_404.html'), 404
