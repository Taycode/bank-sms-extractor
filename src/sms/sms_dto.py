from flask_restx import fields, Namespace


def process_sms_dto(api: Namespace):
    return api.model('SMS', {
        'sender': fields.String,
        'message': fields.String,
    })
