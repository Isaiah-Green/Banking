from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_from_directory
from Customer import Customer
app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("BankingWebpges", "index.html")
@app.route('api/user-action' , methods=['POST'])
def handle_action():
        data = request.get_json()
        action = data.get('action')
        username = data.get('Username')
        password = data.get('Password')
        if action == 'login':
            cus = Customer(entry_number=0)
            response = cus.load_customer(username , password)
            if response["Success"]:
                return jsonify({"Sucess": True, "msg": "Login Sucessful"})
            else:
                return jsonify({"Sucess": False, "meg": "Sorry Login Could Not be Processed , please Try again."})
if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8000, debug=True)