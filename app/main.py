from .crypto_algo import CaesarCipher, MorseCode, VigenereCipher, RunningKeyCipher
from flask import Flask, request
from flask_restful import Api, Resource

# Creating flask application

app = Flask(__name__)
api = Api(app=app)


class CaesarAPI(Resource):
    def post(self):
        if request.form["operation"] == "encrypt":
            encrypted_text = CaesarCipher(
                request.form["text"], int(request.form["key"])).encrypt()
            return {"result": encrypted_text}
        elif request.form["operation"] == "decrypt":
            decrypted_text = CaesarCipher(
                request.form["text"], int(request.form["key"])).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class MorseCodeAPI(Resource, MorseCode):
    def post(self):
        if request.form["operation"] == "encrypt":
            encrypted_text = MorseCode.encrypt(
                self, request.form["text"].upper())
            return {"result": encrypted_text}
        elif request.form["operation"] == "decrypt":
            decrypted_text = MorseCode.decrypt(self, request.form["text"])
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class VignereCipherAPI(Resource):
    def post(self):
        if request.form["operation"] == "encrypt":
            encrypted_text = VigenereCipher(
                request.form["text"], request.form["key"]).encrypt()
            return {"result": encrypted_text}
        elif request.form["operation"] == "decrypt":
            decrypted_text = VigenereCipher(
                request.form["text"], request.form["key"]).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


class RunningKeyCipherAPI(Resource):
    def post(self):
        if request.form["operation"] == "encrypt":
            encrypted_text = RunningKeyCipher(
                request.form['text'], request.form['key']).encrypt()
            return {"result": encrypted_text}
        elif request.form["operation"] == "decrypt":
            decrypted_text = RunningKeyCipher(
                request.form['text'], request.form['key']).decrypt()
            return {"result": decrypted_text}
        else:
            return {"message": "wrong operation"}


api.add_resource(CaesarAPI, "/caesar")
api.add_resource(MorseCodeAPI, "/morsecode")
api.add_resource(VignereCipherAPI, "/vignere")
api.add_resource(RunningKeyCipherAPI, "/runningkeycipher")
