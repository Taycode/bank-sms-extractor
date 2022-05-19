from flask_restx import Namespace, Resource
from flask import request
from src.sms.sms_dto import process_sms_dto
from src.sms.sms_util import process_bank_sms, correct_balance_and_amount


sms_namespace = Namespace('Sms', 'SMS Module')


@sms_namespace.route('/process')
class ProcessSms(Resource):
    """Resource for Processing SMS"""

    @sms_namespace.expect([process_sms_dto(sms_namespace)])
    def post(self):
        payload = request.json
        result = list(map(process_bank_sms, payload))
        result = list(filter(lambda x: x is not None, result))
        result = list(map(correct_balance_and_amount, result))
        return result
