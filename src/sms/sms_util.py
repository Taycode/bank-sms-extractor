from src.sms.processors import bank_processors


def process_bank_sms(data):
    """Processes bank sms"""
    message = data.get('message')
    sender = data.get('sender')
    processor = bank_processors.get(sender)
    if not processor:
        return {'message': 'Not a bank'}, 400
    data = processor(message)
    return data


def remove_comma_from_number(number: str):
    """Returns a float of a string number"""
    return float(number.replace(',', ''))
