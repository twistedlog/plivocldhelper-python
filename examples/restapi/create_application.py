import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)
'''
app_name, answer_url
{'api_id': '59c48490-4bad-11e1-86da-211d0d6a048f', 'error': {u'fallback_method': [u'This field is required.'], u'hangup_method': [u'This field is required.'], u'message_method': [u'This field is required.'], u'answer_method': [u'This field is required.']}}

optional: answer_method, fallback_answer_url, fallback_method, hangup_url
        hangup_method, message_url, message_method, default_app
'''
params = {'answer_url':'http://electric-snow-3852.herokuapp.com/response/redirect/',
          'app_name':'Test Redirect'}
print r.create_application(**params)
