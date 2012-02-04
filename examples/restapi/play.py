import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.play({'call_uuid':'XXXXX', 'urls':'http://mysoundurl.dom/sound.mp3,http://mysoundurl.dom/sound2.mp3')
