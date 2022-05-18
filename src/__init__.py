from flask import Flask
from flask_restx import Api
from src.sms.sms_controller import sms_namespace

api = Api(
    title='Bank Sms Extractor App',
    description='Extractor for parsing bank sms transactions',
    doc='/docs/'
)


def create_app():
    """Creates Flask App"""
    app = Flask(__name__)
    api.init_app(app)

    api.add_namespace(sms_namespace, '/sms')
    return app
