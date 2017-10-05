from flask import Flask, render_template, request, redirect, url_for, jsonify 

app = Flask(__name__)

@app.route('/')
@app.route('/configure/', methods = ['GET','POST'])
def configureFakey():
	# return 'This page will show all my restaurants'
	# restaurants = session.query(Restaurant).all()
	if request.method == 'POST':
		new_title = request.form['title']
		# new_information = request.form['information']
		new_information = request.form['information']
		new_image_caption = request.form['image_caption'].replace("//","*")
		return redirect(url_for('showFakey', new_title = new_title , new_information = new_information, new_image_caption = new_image_caption))
	else:
		return render_template('configure_fakey.html')

@app.route('/fakeypedia/<new_title>/<new_information>/<new_image_caption>')
def showFakey(new_title, new_information, new_image_caption):
	# return 'This page will be for making a new restaurant'
		return render_template('new_fakey.html',new_title=new_title, new_information = new_information, new_image_caption = new_image_caption)

if __name__ == '__main__':
	app.debug = True 
	app.run(host = '0.0.0.0', port = 5000)


