import re


def sterling_bank_processor(message: str):
    """Processes Sterling Bank SMS"""

    # Fetch Transaction Type
    transaction_type = re.findall(r'Credit|Debit|Money In|Money Out', message)
    transaction_type = 'credit' if transaction_type in ['Credit','Money In'] else 'debit'

    # Fetch account number
    account_number = re.findall(r'\*+\d+', message)

    # Fetch Description
    description = re.findall(r'Desc:.*?(?:(?!\sRef).)*', message)
    description = description[0]
    description = description[len('Desc: '):]

    # Fetch Amount
    try:
        amount = re.findall(r'NGN[\d+,]+.\d+', message)
        amount = amount[0]
        amount = amount[len('NGN'):]
    except:
        amount = re.findall(r'Amt: NGN [\d+,]+.\d+', message)
        amount = amount[0]
        amount = amount[len('Amt: NGN '):]

    # Fetch Date
    try:
        date = re.findall(r'\d+-\w+-\d{4}.+@.+\d+:\d+', message)
        date = date[0]
    except:
        date = re.findall(r'\d+:\d+.{4}\d+-\w+-\d{4}', message)
        date = date[0]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'date': date
    }



