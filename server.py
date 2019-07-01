from flask import Flask, jsonify, Response, request

apm = 0
total = 0

app = Flask(__name__)
class Server():
        @app.route('/')
        def count():
                return jsonify(apm)

        @app.route('/reset')
        def reset():
                global apm
                global total
                total = total + apm
                apm = 0
                return jsonify("Great success")
                
        @app.route('/apm/<int:keys>')
        def update(keys):
                global apm
                apm += 1
                return jsonify(apm)

app.run(port=3048)
Server()