import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.speak_member({'conference_id':'myroom', 
                      'member_id':'10',
                      'text':'you are in conference myroom',
                      'voice':'WOMAN',
                      'language':'en-US'
                    })
