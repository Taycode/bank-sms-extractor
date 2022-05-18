from src.sms.processors.first_bank import first_bank_processor
from src.sms.processors.access_bank import access_bank_processor
from src.sms.processors.gtbank import gtbank_processor
from src.sms.processors.keystone_bank import keystone_bank_processor
from src.sms.processors.uba import uba_processor
from src.sms.processors.wema_bank import wema_bank_processor
bank_processors = {
    "FirstBank": first_bank_processor,
    "AccessBank": access_bank_processor,
    "GTBank": gtbank_processor,
    "KEYSTONE": keystone_bank_processor,
    "UBA": uba_processor,
    "WemaBank": wema_bank_processor,
}
