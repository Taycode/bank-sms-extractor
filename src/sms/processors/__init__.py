from src.sms.processors.first_bank import first_bank_processor
from src.sms.processors.access_bank import access_bank_processor
from src.sms.processors.gtbank import gtbank_processor
bank_processors = {
    "FirstBank": first_bank_processor,
    "AccessBank": access_bank_processor,
    "GTBank": gtbank_processor,
}
