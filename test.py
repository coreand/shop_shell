import config

import binascii
from hashlib import sha256


# def adjust_float(a):
#     a = str(a)
#     dot_idx = a.find('.')
#     if dot_idx == -1:
#         a += ".00"
#     elif len(a) - dot_idx - 1 < 2:
#         a += "0"
#     return a
#
#
# order_id = "12345"
# amount = 150
# amount = adjust_float(amount)
# desc = "Test payment №12345"
# desc = binascii.b2a_base64(desc.encode('utf8'))[:-1].decode()
# string_to_hash = ":".join(map(str, [config.PAYEER_MERCHANT_ID, order_id, amount, config.PAYEER_CURRENCY, desc,
#                                    config.PAYEER_SECRET_KEY]))
#
# res = sha256(string_to_hash.encode())
# res = res.hexdigest().upper()
#
# print(res)

# import application
#
#
class Test:
    pass
#
#
# message = Test()
# message.chat = Test()
# message.chat.id = 139263421
# message.text = "300208162"
# application.handle_reply_inviter(message)
# from urllib.request import urlopen, Request
# from urllib.parse import urlencode
#
# values = urlencode(
#     {
#         'account': config.PAYEER_ACCOUNT,
#         'apiId': config.PAYEER_API_ID,
#         'apiPass': config.PAYEER_API_KEY,
#         'action': 'initOutput',
#         'ps': "189279909",
#         'sumIn': '0.01',
#         'curIn': 'USD',
#         'param_ACCOUNT_NUMBER': config.PAYEER_ACCOUNT
#     }
# ).encode()
#
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
# request = Request('https://payeer.com/ajax/api/api.php?initOutput', data=values, headers=headers)
#
# response_body = urlopen(request).read()
# import json
# print(json.loads(response_body))


