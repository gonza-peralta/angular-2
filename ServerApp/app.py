# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route('/')
# def showMachineList():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
from flask import Flask, send_from_directory, render_template
import os

BASE_URL = os.path.abspath(os.path.dirname(__file__))
CLIENT_APP_FOLDER = os.path.join(BASE_URL, "ClientApp")

app = Flask(__name__)

print(BASE_URL)
print(CLIENT_APP_FOLDER)

# This is required by zone.js as it need to access the
# "main.js" file in the "ClientApp\app" folder which it
# does by accessing "<your-site-path>/app/main.js"
@app.route('/app/<path:filename>')
def client_app_app_folder(filename):
    # print("En client_app_app_folder " + filename)
    return send_from_directory(os.path.join(CLIENT_APP_FOLDER, "app"), filename)

# Custom static data
@app.route('/client-app/<path:filename>')
def client_app_folder(filename):
    # print("En client_app_folder " + filename)
    return send_from_directory(CLIENT_APP_FOLDER, filename)

@app.route('/')
def showMachineList():
		return render_template('index.html')

if __name__ == "__main__":
		app.run(host='0.0.0.0')