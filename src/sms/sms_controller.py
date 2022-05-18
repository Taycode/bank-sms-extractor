from flask_restx import Namespace, Resource
from flask import request
from src.sms.sms_dto import process_sms_dto
sms_namespace = Namespace('Sms', 'SMS Module')


@sms_namespace.route('/process')
class ProcessSms(Resource):
    """Resource for Processing SMS"""

    @sms_namespace.expect(process_sms_dto(sms_namespace))
    def post(self):
        payload = request.json
        return payload
