from .crypto_algo import CaesarCipher, MorseCode, VigenereCipher, RunningKeyCipher, ROT13
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Creating flask application

origin_lists = ['https://cryptography-io.web.app', ]

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app=app)

limiter = Limiter(app=app,
                  key_func=get_remote_address,
                  default_limits=["200 per day", "50 per hour"])


class Home(Resource):
    def get(self):
        return jsonify({'Use': {"URL": [
            {"/caesar": "encrypt or decrypt using Caesar Cipher"},
            {"/morsecode": "encrypt or decrypt using Morse Code"},
            {"/vignere": "encrypt or decrypt using Vignere Cipher"},
            {"/runningkeycipher": "encrypt or decrypt using Running Key Cipher"},
            {"/rot13": "encrypt or decrypt using ROT13 Algorithm"}
        ]},
            "Note": "MorseCode and ROT13 does not require a key to encrypt pr decrypt."})


class ROT13API(Resource):
    @ cross_origin(origin=origin_lists, headers=['Content-Type', ])
    @ limiter.limit("5 per minute")
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == 'encrypt':
            return {"result": ROT13(form_data["text"]).encrypt()}
        elif form_data["operation"] == 'decrypt':
            return {"result": ROT13(form_data["text"]).decrypt()}


class CaesarAPI(Resource):
    @ cross_origin(origin=origin_lists, headers=['Content-Type', ])
    @ limiter.limit("5 per minute")
    def post(self):
        form_data = request.get_json()

        if form_data["operation"] == "encrypt":
            return {"result": CaesarCipher(form_data["text"], int(form_data["key"])).encrypt()}

        elif form_data["operation"] == "decrypt":
            return {"result": CaesarCipher(form_data["text"], int(form_data["key"])).decrypt()}

        else:
            return {"message": "wrong operation"}


class MorseCodeAPI(Resource):
    @ cross_origin(origin=origin_lists, headers=['Content-Type', ])
    @ limiter.limit("5 per minute")
    def post(self):
        form_data = request.get_json()

        if form_data["operation"] == "encrypt":
            return {"result": MorseCode(form_data["text"].upper()).encrypt()}

        elif form_data["operation"] == "decrypt":
            return {"result": MorseCode(form_data["text"]).decrypt()}

        else:
            return {"message": "wrong operation"}


class VignereCipherAPI(Resource):
    @ cross_origin(origin=origin_lists, headers=['Content-Type', ])
    @ limiter.limit("5 per minute")
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            return {"result": VigenereCipher(form_data["text"], form_data["key"]).encrypt()}
        elif form_data["operation"] == "decrypt":
            return {"result": VigenereCipher(form_data["text"], form_data["key"]).decrypt()}
        else:
            return {"message": "wrong operation"}


class RunningKeyCipherAPI(Resource):
    @ cross_origin(origin=origin_lists, headers=['Content-Type', ])
    @ limiter.limit("5 per minute")
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            return {"result": RunningKeyCipher(form_data['text'], form_data['key']).encrypt()}
        elif form_data["operation"] == "decrypt":
            return {"result": RunningKeyCipher(form_data['text'], form_data['key']).decrypt()}
        else:
            return {"message": "wrong operation"}


api.add_resource(Home, "/")
api.add_resource(CaesarAPI, "/caesar")
api.add_resource(MorseCodeAPI, "/morsecode")
api.add_resource(VignereCipherAPI, "/vignere")
api.add_resource(RunningKeyCipherAPI, "/runningkeycipher")
api.add_resource(ROT13API, "/rot13")
