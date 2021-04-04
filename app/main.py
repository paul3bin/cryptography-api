from .crypto_algo import CaesarCipher, MorseCode, VigenereCipher, RunningKeyCipher, ROT13
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

# Creating flask application

origin_lists = ['https://cryptography-io.web.app', ]

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app=app)


class ROT13API(Resource):
    @cross_origin(origin=origin_lists, headers=['Content-Type', ])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == 'encrypt':
            return {"result": ROT13(form_data["text"]).encrypt()}
        elif form_data["operation"] == 'decrypt':
            return {"result": ROT13(form_data["text"]).decrypt()}


class CaesarAPI(Resource):
    @cross_origin(origin=origin_lists, headers=['Content-Type', ])
    def post(self):
        form_data = request.get_json()

        if form_data["operation"] == "encrypt":
            return {"result": CaesarCipher(form_data["text"], int(form_data["key"])).encrypt()}

        elif form_data["operation"] == "decrypt":
            return {"result": CaesarCipher(form_data["text"], int(form_data["key"])).decrypt()}

        else:
            return {"message": "wrong operation"}


class MorseCodeAPI(Resource):
    @cross_origin(origin=origin_lists, headers=['Content-Type', ])
    def post(self):
        form_data = request.get_json()

        if form_data["operation"] == "encrypt":
            return {"result": MorseCode(form_data["text"].upper()).encrypt()}

        elif form_data["operation"] == "decrypt":
            return {"result": MorseCode(form_data["text"]).decrypt()}

        else:
            return {"message": "wrong operation"}


class VignereCipherAPI(Resource):
    @cross_origin(origin=origin_lists, headers=['Content-Type', ])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            return {"result": VigenereCipher(form_data["text"], form_data["key"]).encrypt()}
        elif form_data["operation"] == "decrypt":
            return {"result": VigenereCipher(form_data["text"], form_data["key"]).decrypt()}
        else:
            return {"message": "wrong operation"}


class RunningKeyCipherAPI(Resource):
    @cross_origin(origin=origin_lists, headers=['Content-Type', ])
    def post(self):
        form_data = request.get_json()
        if form_data["operation"] == "encrypt":
            return {"result": RunningKeyCipher(form_data['text'], form_data['key']).encrypt()}
        elif form_data["operation"] == "decrypt":
            return {"result": RunningKeyCipher(form_data['text'], form_data['key']).decrypt()}
        else:
            return {"message": "wrong operation"}


api.add_resource(CaesarAPI, "/caesar")
api.add_resource(MorseCodeAPI, "/morsecode")
api.add_resource(VignereCipherAPI, "/vignere")
api.add_resource(RunningKeyCipherAPI, "/runningkeycipher")
api.add_resource(ROT13API, "/rot13")
