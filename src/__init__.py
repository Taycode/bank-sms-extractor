from flask import Flask
from flask_restx import Api


api = Api(
    title='Bank Sms Extractor App',
    description='Extractor for parsing bank sms transactions',
    docs='/docs/'
)


def create_app():
    """Creates Flask App"""
    app = Flask(__name__)
    api.__init__(app)
    return app
