import re

def standardcharter_bank_processor(message: str):
    """Processes StandardCharter Bank SMS"""

    # Fetch Transaction type
    transaction_type = re.findall(r'Credit|Debit', message)
    transaction_type = transaction_type[0]
    transaction_type = 'credit' if transaction_type == 'Credit' else 'debit'

    # Fetch Account Number 
    account_number = re.findall(r'Acct:x+\d+', message)
    account_number = account_number[0]
    account_number = account_number[len('Acct:'):]

    # Fetch Description
    description = re.findall(r'Desc:*?(?:(?!,\sDate).)*', message)
    description = description[0]

    # Fetch Amount
    amount = re.findall(r'Amt:NGN[\d+,]+.\d+', message)
    amount = amount[0]
    amount = amount[len('Amt:NGN'):]

    # Fetch Date 
    date = re.findall(r'\d{2}-\d{2}-\d{2}', message)
    date = date[0]

    # Fetch Balance
    balance = re.findall(r'Bal:NGN[\d+,]+.\d+', message)
    balance = balance[0]
    balance = balance[len('Bal:NGN')]

    return {
        'description': description,
        'transaction_type': transaction_type,
        'account_number': account_number,
        'amount': amount,
        'balance': balance,
        'date': date
    }
    
