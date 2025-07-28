import requests
import base64
from datetime import datetime

class MpesaService:
    def __init__(self, consumer_key, consumer_secret, shortcode, passkey):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.shortcode = shortcode
        self.passkey = passkey
        self.access_token = self.get_access_token()

    def get_access_token(self):
        url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        response = requests.get(url, auth=(self.consumer_key, self.consumer_secret))
        return response.json()['access_token']

    def lipa_na_mpesa_online(self, phone_number, amount, callback_url, account_reference):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode((self.shortcode + self.passkey + timestamp).encode()).decode()

        url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": account_reference,
            "TransactionDesc": "Payment for goods/services"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def b2c_payment(self, phone_number, amount, remarks):
        url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "InitiatorName": "testapi",
            "SecurityCredential": "YOUR_SECURITY_CREDENTIAL", # This needs to be generated
            "CommandID": "BusinessPayment",
            "Amount": amount,
            "PartyA": self.shortcode,
            "PartyB": phone_number,
            "Remarks": remarks,
            "QueueTimeOutURL": "https://your-callback-url.com/timeout",
            "ResultURL": "https://your-callback-url.com/result",
            "Occassion": "Business Payment"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()
