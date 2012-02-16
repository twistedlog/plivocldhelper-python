import xml.etree.ElementTree as etree
import base64
import hmac
from hashlib import sha1

import requests

try:
    import json
except ImportError:
    import simplejson as json


PLIVO_VERSION = "v1"


class PlivoError(Exception):
    pass


def validate_signature(uri, post_params, signature, auth_token):
    for k, v in sorted(post_params.items()):
        uri += k + v
    return base64.encodestring(hmac.new(self.auth_token, s, sha1).digest()).strip() == signature 


class RestAPI(object):
    def __init__(self, auth_id, auth_token, url='http://api.plivo.com', version=PLIVO_VERSION):
        self.version = version
        self.url = url.rstrip('/') + '/' + self.version
        self.auth_id = auth_id
        self.auth_token = auth_token
        self._api = self.url + '/Account/%s' % self.auth_id
        self.headers = {'User-Agent':'PythonPlivo'}

    def _request(self, method, path, data={}, params={}):
        path = path.rstrip('/') + '/'
        if method == 'POST':
            r = requests.post(self._api + path, headers=self.headers, 
                              auth=(self.auth_id, self.auth_token),
                              params=params,
                              data=json.dumps(data))
        elif method == 'GET':
            r = requests.get(self._api + path, headers=self.headers, 
                             auth=(self.auth_id, self.auth_token),
                             params=params,
                             data=data)
        elif method == 'DELETE':
            r = requests.delete(self._api + path, headers=self.headers, 
                                auth=(self.auth_id, self.auth_token),
                                params=params,
                                data=data)
        elif method == 'PUT':
            r = requests.put(self._api + path, headers=self.headers, 
                             auth=(self.auth_id, self.auth_token),
                             params=params,
                             data=json.dumps(data))
        content = r.content
        if content:
            try:
                response = json.loads(content) 
            except ValueError:
                response = content
        else:
            response = content
        return (r.status_code, response)

    @staticmethod
    def get_param(params, key):
        try:
            return params[key]
        except KeyError:
            raise PlivoException("missing mandatory parameter %s" % key)
                
    ## Accounts ##
    def get_account(self, params={}):
        return self._request('GET', '')

    def modify_account(self, params={}):
        return self._request('POST', '', data=params)

    def get_subaccounts(self, params={}):
        return self._request('GET', '/Subaccount/')

    def create_subaccount(self, params={}):
        return self._request('POST', '/Subaccount/', data=params)

    def get_subaccount(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('GET', '/Subaccount/%s/' % subauth_id)

    def modify_subaccount(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('POST', '/Subaccount/%s/' % subauth_id, data=params)

    def delete_subaccount(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('DELETE', '/Subaccount/%s/' % subauth_id)

    ## Applications ##
    def get_applications(self, params={}):
        return self._request('GET', '/Application/', params=params)

    def create_application(self, params={}):
        return self._request('POST', '/Application/', data=params)

    def get_application(self, params={}):
        app_id = self.params.pop("app_id")
        return self._request('GET', '/Application/%s/' % app_id)

    def modify_application(self, params={}):
        app_id = self.params.pop("app_id")
        return self._request('POST', '/Application/%s/' % app_id, data=params)

    def delete_application(self, params={}):
        app_id = self.params.pop("app_id")
        return self._request('DELETE', '/Application/%s/' % app_id)

    def get_subaccount_applications(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('GET', '/Subaccount/%s/Application/' % subauth_id)

    def get_subaccount_application(self, params={}):
        subauth_id = params.pop("subauth_id")
        app_id = self.params.pop("app_id")
        return self._request('GET', '/Subaccount/%s/Application/%s/' % (subauth_id, app_id))

    def create_subaccount_application(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('POST', '/Subaccount/%s/Application/' % subauth_id, data=params)

    def modify_subaccount_application(self, params={}):
        subauth_id = params.pop("subauth_id")
        app_id = self.params.pop("app_id")
        return self._request('POST', '/Subaccount/%s/Application/%s/' % (subauth_id, app_id), data=params)

    def delete_subaccount_application(self, params={}):
        subauth_id = params.pop("subauth_id")
        app_id = self.params.pop("app_id")
        return self._request('DELETE', '/Subaccount/%s/Application/%s/' % (subauth_id, app_id))

    ## Numbers ##
    def get_numbers(self, params={}):
        return self._request('GET', '/Number/', params=params)

    def search_numbers(self, params={}):
        return self._request('GET', '/Number/Search/', params=params)

    def get_number(self, params={}):
        number = self.params.pop("number")
        return self._request('GET', '/Number/%s/' % number)

    def rent_number(self, params={}):
        number = self.params.pop("number")
        return self._request('POST', '/Number/Action/%s/' % number)

    def unrent_number(self, params={}):
        number = self.params.pop("number")
        return self._request('DELETE', '/Number/Action/%s/' % number)

    def get_subaccount_numbers(self, params={}):
        subauth_id = params.pop("subauth_id")
        return self._request('GET', '/Subaccount/%s/Number/' % subauth_id, params=params)

    def get_subaccount_number(self, params={}):
        subauth_id = params.pop("subauth_id")
        number = self.params.pop("number")
        return self._request('GET', '/Subaccount/%s/Number/%s/' % (subauth_id, number))

    ## Schedule ##
    def get_scheduled_tasks(self, params={}):
        return self._request('GET', '/Schedule/')

    def cancel_scheduled_task(self, params={}):
        task_id = params.pop("task_id")
        return self._request('DELETE', '/Schedule/%s/' % task_id)

    ## Calls ##
    def get_cdrs(self, params={}):
        return self._request('GET', '/Call/', params=params)

    def get_cdr(self, params={}):
        record_id = params.pop('record_id')
        return self._request('GET', '/Call/%s/' % record_id)

    def get_live_calls(self, params={}):
        return self._request('GET', '/Call/', params={'status':'live'})

    def get_live_call(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('GET', '/Call/%s/' % call_uuid, params={'status':'live'})

    def make_call(self, params={}):
        return self._request('POST', '/Call/', data=params)

    def hangup_all_calls(self, params={}):
        return self._request('DELETE', '/Call/')

    def transfer_call(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/' % call_uuid, data=params)

    def hangup_call(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/' % call_uuid)

    def record(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Record/' % call_uuid, data=params)
        
    def stop_record(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/Record/' % call_uuid)

    def play(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Play/' % call_uuid, data=params)
        
    def stop_play(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('DELETE', '/Call/%s/Play/' % call_uuid)

    def speak(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/Speak/' % call_uuid, data=params)
        
    def send_digits(self, params={}):
        call_uuid = params.pop('call_uuid')
        return self._request('POST', '/Call/%s/DTMF/' % call_uuid, data=params)

    def get_subaccount_cdrs(self, params={}):
        subauth_id = params.pop('subauth_id')
        return self._request('GET', '/Subaccount/%s/Call/' % subauth_id, params=params)

    def get_subaccount_cdr(self, params={}):
        subauth_id = params.pop('subauth_id')
        record_id = params.pop('record_id')
        return self._request('GET', '/Subaccount/%s/Call/%s/' % (subauth_id, record_id))

    ## Calls requests ##
    def hangup_request(self, params={}):
        request_uuid = params.pop('request_uuid')
        return self._request('DELETE', '/Request/%s/' % request_uuid)

    ## Conferences ##
    def get_live_conferences(self, params={}):
        return self._request('GET', '/Conference/', params=params)

    def hangup_all_conferences(self, params={}):
        return self._request('DELETE', '/Conference/')

    def get_live_conference(self, params={}):
        conference_id = params.pop('conference_id')
        return self._request('GET', '/Conference/%s/' % conference_id, params=params)

    def hangup_conference(self, params={}):
        conference_id = params.pop('conference_id')
        return self._request('DELETE', '/Conference/%s/' % conference_id)

    def hangup_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/' % (conference_id, member_id))

    def play_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Play/' % (conference_id, member_id), data=params)
        
    def stop_play_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Play/' % (conference_id, member_id))

    def speak_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Speak/' % (conference_id, member_id), data=params)

    def deaf_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Deaf/' % (conference_id, member_id))

    def undeaf_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Deaf/' % (conference_id, member_id))

    def mute_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Mute/' % (conference_id, member_id))

    def unmute_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('DELETE', '/Conference/%s/Member/%s/Mute/' % (conference_id, member_id))

    def kick_member(self, params={}):
        conference_id = params.pop('conference_id')
        member_id = params.pop('member_id')
        return self._request('POST', '/Conference/%s/Member/%s/Kick/' % (conference_id, member_id))

    def record_conference(self, params={}): 
        conference_id = params.pop('conference_id')
        return self._request('POST', '/Conference/%s/Record/' % conference_id, params)

    def stop_record_conference(self, params={}): 
        conference_id = params.pop('conference_id')
        return self._request('DELETE', '/Conference/%s/Record/' % conference_id)

    ## Recordings ##
    def get_recordings(self, params={}):
        return self._request('GET', '/Recording/', params=params)

    def get_recording(self, params={}):
        recording_id = params.pop('recording_id')
        return self._request('GET', '/Recording/%s/' % recording_id)

    def get_subaccount_recordings(self, params={}):
        subauth_id = params.pop('subauth_id')
        return self._request('GET', '/Subaccount/%s/Recording/' % subauth_id)

    def get_subaccount_recording(self, params={}):
        subauth_id = params.pop('subauth_id')
        recording_id = params.pop('recording_id')
        return self._request('GET', '/Subaccount/%s/Recording/%s/' % (subauth_id, recording_id))

    ## Endpoints ##
    def get_endpoints(self, params={}):
        return self._request('GET', '/Endpoint/', params=params)

    def create_endpoint(self, params={}):
        return self._request('POST', '/Endpoint/', data=params)

    def get_endpoint(self, params={}):
        endpoint_id = params.pop('endpoint_id')
        return self._request('GET', '/Endpoint/%s/' % endpoint_id)

    def modify_endpoint(self, params={}):
        endpoint_id = params.pop('endpoint_id')
        return self._request('POST', '/Endpoint/%s/' % endpoint_id, data=params)

    def delete_endpoint(self, params={}):
        endpoint_id = params.pop('endpoint_id')
        return self._request('DELETE', '/Endpoint/%s/' % endpoint_id)

    def get_subaccount_endpoints(self, params={}):
        subauth_id = params.pop('subauth_id')
        return self._request('GET', '/Subaccount/%s/Endpoint/' % subauth_id)

    def create_subaccount_endpoint(self, params={}):
        subauth_id = params.pop('subauth_id')
        return self._request('POST', '/Subaccount/%s/Endpoint/' % subauth_id, data=params)

    def get_subaccount_endpoint(self, params={}):
        subauth_id = params.pop('subauth_id')
        endpoint_id = params.pop('endpoint_id')
        return self._request('GET', '/Subaccount/%s/Endpoint/%s/' % (subauth_id, endpoint_id))

    def modify_subaccount_endpoint(self, params={}):
        subauth_id = params.pop('subauth_id')
        endpoint_id = params.pop('endpoint_id')
        return self._request('POST', '/Subaccount/%s/Endpoint/%s/' % (subauth_id, endpoint_id), data=params)

    def delete_subaccount_endpoint(self, params={}):
        subauth_id = params.pop('subauth_id')
        endpoint_id = params.pop('endpoint_id')
        return self._request('DELETE', '/Subaccount/%s/Endpoint/%s/' % (subauth_id, endpoint_id))

    ## Carriers ##
    def get_carriers(self, params={}):
        return self._request('GET', '/Carrier/', params=params)

    def create_carrier(self, params={}):
        return self._request('POST', '/Carrier/', data=params)

    def get_carrier(self, params={}):
        carrier_id = params.pop('carrier_id')
        return self._request('GET', '/Carrier/%s/' % carrier_id)

    def modify_carrier(self, params={}):
        carrier_id = params.pop('carrier_id')
        return self._request('POST', '/Carrier/%s/' % carrier_id, data=params)

    def delete_carrier(self, params={}):
        carrier_id = params.pop('carrier_id')
        return self._request('DELETE', '/Carrier/%s/' % carrier_id)

    ## Carrier Routings ##
    def get_carrier_routings(self, params={}):
        return self._request('GET', '/CarrierRouting/', params=params)

    def create_carrier_routing(self, params={}):
        return self._request('POST', '/CarrierRouting/', data=params)

    def get_carrier_routing(self, params={}):
        routing_id = params.pop('routing_id')
        return self._request('GET', '/CarrierRouting/%s/' % routing_id)

    def modify_carrier_routing(self, params={}):
        routing_id = params.pop('routing_id')
        return self._request('POST', '/CarrierRouting/%s/' % routing_id, data=params)

    def delete_carrier_routing(self, params={}):
        routing_id = params.pop('routing_id')
        return self._request('DELETE', '/CarrierRouting/%s/' % routing_id)

    ## Message ##
    def send_message(self, params={}):
        return self._request('POST', '/Message/', data=params)



class Element(object):
    nestables = ()
    valid_attributes = ()

    def __init__(self, body='', **attributes):
        self.attributes = {}
        self.name = self.__class__.__name__
        self.body = body
        self.node = None
        for k, v in attributes.iteritems():
            if not k in self.valid_attributes:
                raise PlivoError('invalid attribute %s for %s' % (k, self.name))
            self.attributes[k] = self._convert_value(v)
        self.node = etree.Element(self.name, attrib=self.attributes)
        if self.body:
            self.node.text = self.body

    @staticmethod
    def _convert_value(v):
        if v is True:
            return u'true'
        elif v is False:
            return u'false'
        elif v is None:
            return u'none'
        elif v == 'get':
            return u'GET'
        elif v == 'post':
            return u'POST'
        return unicode(v)

    def add(self, element):
        if element.name in self.nestables:
            self.node.append(element.node)
            return element
        raise PlivoError('%s not nestable in %s' % (element.name, self.name))

    def to_xml(self):
        return etree.tostring(self.node, encoding="utf-8")

    def __str__(self):
        return self.to_xml()

    def __repr__(self):
        return self.to_xml()

    def addSpeak(self, body, **kwargs):
        return self.add(Speak(body, **kwargs))

    def addPlay(self, body, **kwargs):
        return self.add(Play(body, **kwargs))

    def addGetDigits(self, **kwargs):
        return self.add(GetDigits(**kwargs))

    def addRecord(self, **kwargs):
        return self.add(Record(**kwargs))

    def addDial(self, **kwargs):
        return self.add(Dial(**kwargs))

    def addNumber(self, body, **kwargs):
        return self.add(Number(body, **kwargs))

    def addUser(self, body, **kwargs):
        return self.add(User(body, **kwargs))

    def addRedirect(self, body, **kwargs):
        return self.add(Redirect(body, **kwargs))

    def addWait(self, **kwargs):
        return self.add(Wait(**kwargs))

    def addHangup(self, **kwargs):
        return self.add(Hangup(**kwargs))

    def addPreAnswer(self, **kwargs):
        return self.add(PreAnswer(**kwargs))

    def addConference(self, body, **kwargs):
        return self.add(Conference(body, **kwargs))

    def addMessage(self, body, **kwargs):
        return self.add(Message(body, **kwargs))


class Response(Element):
    nestables = ('Speak', 'Play', 'GetDigits', 'Record', 'Dial', 'Message',
                 'Redirect', 'Wait', 'Hangup', 'PreAnswer', 'Conference')
    valid_attributes = ()

    def __init__(self):
        Element.__init__(self, body='')


class Speak(Element):
    nestables = ()
    valid_attributes = ('voice', 'language', 'loop')
        
    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No text set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Play(Element):
    nestables = ()
    valid_attributes = ('loop')
        
    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No url set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Wait(Element):
    nestables = ()
    valid_attributes = ('length')
        
    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Redirect(Element):
    nestables = ()
    valid_attributes = ('method')
        
    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No url set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Hangup(Element):
    nestables = ()
    valid_attributes = ('schedule', 'reason')
        
    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class GetDigits(Element):
    nestables = ('Speak', 'Play', 'Wait')
    valid_attributes = ('action', 'method', 'timeout', 'finishOnKey',
                        'numDigits', 'retries', 'invalidDigitsSound',
                        'validDigits', 'playBeep')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Number(Element):
    nestables = ()
    valid_attributes = ('sendDigits', 'sendOnPreanswer')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No number set for %s' % self.name)
        Element.__init__(self, body, **attributes)
        

class User(Element):
    nestables = ()
    valid_attributes = ('sendDigits', 'sendOnPreanswer')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No user set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Dial(Element):
    nestables = ('Number', 'User')
    valid_attributes = ('action','method','timeout','hangupOnStar',
                        'timeLimit','callerId', 'callerName', 'confirmSound',
                        'dialMusic', 'confirmKey', 'redirect',
                        'callbackUrl', 'callbackMethod', 'digitsMatch')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Conference(Element):
    nestables = ()
    valid_attributes = ('muted','beep','startConferenceOnEnter',
                        'endConferenceOnExit','waitSound','enterSound', 'exitSound',
                        'timeLimit', 'hangupOnStar', 'maxMembers',
                        'record', 'recordFileFormat', 'action', 'method', 'redirect',
                        'digitsMatch', 'callbackUrl', 'callbackMethod',
                        'stayAlone', 'floorEvent')

    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No conference name set for %s' % self.name)
        Element.__init__(self, body, **attributes)


class Record(Element):
    nestables = ()
    valid_attributes = ('action', 'method', 'timeout','finishOnKey',
                        'maxLength', 'bothLegs', 'playBeep',
                        'redirect', 'fileFormat')

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class PreAnswer(Element):
    nestables = ('Play', 'Speak', 'GetDigits', 'Wait', 'Redirect')
    valid_attributes = ()

    def __init__(self, **attributes):
        Element.__init__(self, body='', **attributes)


class Message(Element):
    nestables = ()
    valid_attributes = ('src', 'dst', 'type')
        
    def __init__(self, body, **attributes):
        if not body:
            raise PlivoError('No text set for %s' % self.name)
        Element.__init__(self, body, **attributes)


