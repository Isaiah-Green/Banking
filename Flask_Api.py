from flask import Flask, jsonify, request , render_template
from flask_cors import CORS
from flask import send_from_directory
from Customer import Customer

app = Flask(__name__)

@app.route("/")
def home():
     return render_template('index.html')
@app.route("/UserLogin.html")
def LoginPage():
     return render_template('UserLogin.html')
@app.route('/api/user-action' , methods=['POST'])
def handle_action():
        data = request.get_json()
        print(data)
        action = data.get('action')
        username = data.get('UserName')
        password = data.get('Password')
        if action == 'login':
            cus = Customer(entry_number=0)
            response = cus.load_customer(userName = username , password=password)
            if response["Sucess"]:
                return jsonify({"Sucess": True, "msg": "Login Sucessful"})
            else:
                return jsonify({"Sucess": False, "meg": "Sorry Login Could Not be Processed , please Try again."})
if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8000, debug=True)