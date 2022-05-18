from flask_restx import Namespace, Resource
from flask import request
from src.sms.sms_dto import process_sms_dto
from src.sms.processors.first_bank import first_bank_processor
from src.sms.processors import bank_processors


sms_namespace = Namespace('Sms', 'SMS Module')


@sms_namespace.route('/process')
class ProcessSms(Resource):
    """Resource for Processing SMS"""

    @sms_namespace.expect(process_sms_dto(sms_namespace))
    def post(self):
        payload = request.json
        message = payload['message']
        sender = payload['sender']
        processor = bank_processors.get(sender)
        if not processor:
            return {'message': 'Not a bank'}, 400
        data = processor(message)
        return data
