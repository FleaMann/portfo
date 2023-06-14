from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        fields = ["Name", "Email", "Message"]
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, dialect='excel')
        # csv_writer.writerow(fields)
        csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(f'data {{data}}')
            return render_template('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'
