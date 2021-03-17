from .crypto_algo import CaesarCipher, MorseCode, VigenereCipher, RunningKeyCipher
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS,cross_origin

# Creating flask application

origin_lists = ['http://localhost:3000/', 'https://cryptography-flask-api.herokuapp.com/']

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app=app)


class CaesarAPI(Resource):
    @cross_origin(origin=origin_lists,headers=['Content-Type',])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            encrypted_text = CaesarCipher(
                form_data["text"], int(form_data["key"])).encrypt()
            return {"result": encrypted_text}
        elif form_data["operation"] == "decrypt":
            decrypted_text = CaesarCipher(
                form_data["text"], int(form_data["key"])).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class MorseCodeAPI(Resource):
    @cross_origin(origin=origin_lists,headers=['Content-Type',])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            encrypted_text = MorseCode(form_data["text"].upper()).encrypt()
            return {"result": encrypted_text}
        elif form_data["operation"] == "decrypt":
            decrypted_text = MorseCode(form_data["text"]).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class VignereCipherAPI(Resource):
    @cross_origin(origin=origin_lists,headers=['Content-Type',])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            encrypted_text = VigenereCipher(
                form_data["text"], form_data["key"]).encrypt()
            return {"result": encrypted_text}
        elif form_data["operation"] == "decrypt":
            decrypted_text = VigenereCipher(
                form_data["text"], form_data["key"]).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class RunningKeyCipherAPI(Resource):
    @cross_origin(origin=origin_lists,headers=['Content-Type',])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            encrypted_text = RunningKeyCipher(
                form_data['text'], form_data['key']).encrypt()
            return {"result": encrypted_text}
        elif form_data["operation"] == "decrypt":
            decrypted_text = RunningKeyCipher(
                form_data['text'], form_data['key']).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


api.add_resource(CaesarAPI, "/caesar")
api.add_resource(MorseCodeAPI, "/morsecode")
api.add_resource(VignereCipherAPI, "/vignere")
api.add_resource(RunningKeyCipherAPI, "/runningkeycipher")
