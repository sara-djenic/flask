from __future__ import print_function
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def predavanja():
	f = open("RAFraspored.csv","r", encoding='utf8')
	redovi = f.readlines()
	sva_imena = [red.split(',')[2] for red in redovi]
	jedinstvena_imena = []
	for ime in sva_imena:
		if ime not in jedinstvena_imena:
			jedinstvena_imena.append(ime)

	sva_imena = jedinstvena_imena.sort()

	sve_ucionice = [red.split(',')[6] for red in redovi]
	jedinstvene_ucionice = []
	for ucionica in sve_ucionice:
		
		if ucionica not in jedinstvene_ucionice:
			jedinstvene_ucionice.append(ucionica)
	print(jedinstvene_ucionice)
	sve_ucionice = jedinstvene_ucionice.sort()

	return render_template("index.html",redovi = redovi,sva_imena = jedinstvena_imena, sve_ucionice = jedinstvene_ucionice)

if __name__ == '__main__':
	app.run()