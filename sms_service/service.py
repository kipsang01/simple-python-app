import logging

import africastalking
from django.conf import settings

logger = logging.getLogger(__name__)

def send_sms(phone_numbers, message):
    username = settings.AFRICAS_TALKING_USERNAME
    api_key = settings.AFRICAS_TALKING_API_KEY
    sender_id = settings.AFRICAS_TALKING_SENDER_ID
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS  

    try:
        response = sms.send(message, phone_numbers, sender_id=sender_id)
        return response
    except Exception as e:
        logger.critical(e)
        return None