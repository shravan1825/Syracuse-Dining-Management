from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
from datetime import datetime



# Hashing a password
def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def index():
#     return("Hello")
#Home screen

#Login
@app.route('/', methods=['GET','POST'])
def post_handling():
    # print(request.method)
    if request.method == "GET":
        print("GETTTTTTT")
        return ("enter details")

    content = request.get_json()
    email = content["email"]
    passw = content["password"]

    current_datetime = datetime.now()
    timestamp = current_datetime.timestamp()
    # encrypted_password = encrypt_password(passw)

    #password from database:
    real_user_password = passw  
    # decrypted_password = decrypt_password(real_user_password)

    if passw == real_user_password:

        return redirect(url_for('homepage_handler', timestamp1=timestamp))


    return ("Error")
    
@app.route('/homeScreen/<timestamp1>', methods=["GET","POST"])
def homepage_handler(timestamp1):
    return(f"Home dashboard + /homeScreen/{timestamp1}")




if __name__ == '__main__':
    app.run(debug=True)
