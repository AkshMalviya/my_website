from flask import Flask,render_template,request
import csv
app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template("index.html")	

@app.route("/<page_name>")
def html_page(page_name):
	return render_template(page_name)	

# def creating_db(data):
# 	email=data["email"]
# 	message=data["message"]
# 	subject=data["subject"]
# 	with open("database.txt",mode="a") as databa:
# 		databa.write(f"Email:{email} \nSubject:{subject}\nMessage:{message}\n\n\n")


def creating_db2(data):
	email=data["email"]
	message=data["message"]
	subject=data["subject"]	
	with open("database2.csv",mode="a") as database2:
		obj = csv.writer(database2,delimiter="," , quotechar='|', quoting=csv.QUOTE_MINIMAL)
		obj.writerow([email,subject,message])


@app.route("/submitting" , methods=['POST','GET'])
def subm():
	if request.method == 'POST':
		data = request.form.to_dict()
		creating_db2(data)
		return render_template("thankyou.html")