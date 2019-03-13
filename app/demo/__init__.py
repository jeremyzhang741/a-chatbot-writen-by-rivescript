# -*- coding: utf-8 -*-


from flask import Flask

import jeremyzhang7413_chatbot


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        jeremyzhang7413_chatbot.bp,
        url_prefix='/jeremyzhang7413/chatbot')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)