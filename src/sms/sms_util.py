from src.sms.processors import bank_processors


def process_bank_sms(data):
    """Processes bank sms"""
    message = data.get('message')
    sender = data.get('sender')
    processor = bank_processors.get(sender)
    if not processor:
        return None
    try:
        data = processor(message)
        return data
    except Exception:
        return None


def remove_comma_from_number(number: str):
    """Returns a float of a string number"""
    return float(number.replace(',', ''))


def correct_balance_and_amount(data):
    """Corrects balance and amount"""
    amount = data.get('amount') or None
    balance = data.get('balance') or None
    if amount:
        amount = remove_comma_from_number(amount)
    if balance:
        balance = remove_comma_from_number(balance)
    return {**data, 'amount': amount, 'balance': balance}
