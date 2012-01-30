import xml.etree.ElementTree as etree
import base64
import hmac
from hashlib import sha1

import slumber


PLIVO_VERSION = "v1"


class PlivoError(Exception):
    pass


def validate_signature(uri, post_params, signature, auth_id, auth_token):
    for k, v in sorted(post_params.items()):
        uri += k + v
    return base64.encodestring(hmac.new(self.auth_token, s, sha1).digest()).strip() == signature 


class RestAPI(object):
    def __init__(self, auth_id, auth_token, url='http://api.plivo.com', version=PLIVO_VERSION):
        self.version = version
        self.url = url.rstrip('/') + '/' + self.version + '/'
        self.auth_id = auth_id
        self.auth_token = auth_token
        self.api = slumber.API(self.url, auth=(auth_id, auth_token))

    def _api(self):
        return self.api.Account(self.auth_id)

    ## Accounts ##
    def get_account(self):
        return self._api().get()

    def modify_account(self, **params):
        return self._api().post(params)

    def get_subaccounts(self):
        return self._api().Subaccount.get()

    def get_subaccount(self, subauth_id):
        return self._api().Subaccount(subauth_id).get()

    def modify_subaccount(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).post(params)

    def delete_subaccount(self, subauth_id):
        return self._api().Subaccount(subauth_id).delete()

    ## Applications ##
    def get_applications(self, **params):
        return self._api().Application.get(params)

    def create_application(self, **params):
        return self._api().Application.post(params)

    def get_application(self, app_id):
        return self._api().Application(app_id).get()

    def modify_application(self, app_id, **params):
        return self._api().Application(app_id).post(params)

    def delete_application(self, app_id):
        return self._api().Application(app_id).delete()

    def get_subaccount_applications(self, subauth_id):
        return self._api().Subaccount(subauth_id).Application.get()

    def create_subaccount_application(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).Application.get(params)

    def get_subaccount_application(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).Application.get(params)

    def modify_subaccount_application(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).Application.post(params)

    def delete_subaccount_application(self, subauth_id):
        return self._api().Subaccount(subauth_id).Application.delete()

    ## Numbers ##
    def get_numbers(self, **params):
        return self._api().Number.get(params)

    def search_numbers(self, number, **params):
        params['number'] = number
        return self._api().Number.Search.get(**params)

    def get_number(self, number):
        return self._api().Number(number).get()

    def rent_number(self, number):
        return self._api().Number(number).post()

    def unrent_number(self, number):
        return self._api().Number(number).delete()

    def get_subaccount_numbers(self, **params):
        return self._api().Number.get(params)

    ## Schedule ##
    def get_scheduled_tasks(self):
        return self._api().Schedule.get()

    def cancel_scheduled_task(self, task_id):
        return self._api().Schedule(task_id).delete()

    ## Calls ##
    def get_cdrs(self, **params):
        return self._api().Call.get(params)

    def get_cdr(self, record_id):
        return self._api().Call(record_id).get()

    def get_live_calls(self):
        return self._api().Call.get({'status':'live'})

    def get_live_call(self, calluuid):
        return self._api().Call(calluuid).get({'status':'live'})

    def make_call(self, **params):
        return self._api().Call.post(params)

    def hangup_all_calls(self):
        return self._api().Call.delete()

    def transfer_call(self, calluuid, **params):
        return self._api().Call(calluuid).post(params)

    def hangup_call(self, calluuid):
        return self._api().Call(calluuid).delete()

    def record(self, calluuid, **params):
        return self._api().Call(calluuid).Record.post(params)
        
    def stop_record(self, calluuid):
        return self._api().Call(calluuid).Record.delete()

    def play(self, calluuid, **params):
        return self._api().Call(calluuid).Play.post(params)
        
    def stop_play(self, calluuid):
        return self._api().Call(calluuid).Play.delete()

    def send_digits(self, calluuid, **params):
        return self._api().Call(calluuid).DTMF.post(params)

    def get_subaccount_cdrs(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).Call.get(params)

    def get_subaccount_cdr(self, subauth_id, record_id):
        return self._api().Subaccount(subauth_id).Call(record_id).get()

    ## Calls requests ##
    def hangup_request(self, requestuuid):
        return self._api().Request(requestuuid).delete()

    ## Conferences ##
    def get_live_conferences(self, **params):
        return self._api().Conference.get(params)

    def hangup_all_conferences(self):
        return self._api().Conference.delete()

    def get_live_conference(self, conference_id, **params):
        return self._api().Conference(conference_id).get(params)

    def hangup_conference(self):
        return self._api().Conference(conference_id).delete()

    def hangup_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).delete()

    def play_conference(self, member_id, **params):
        return self._api().Conference(conference_id).Member(member_id).Play.post(params)
        
    def stop_play_conference(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Play.delete()

    def speak_conference(self, member_id, **params):
        return self._api().Conference(conference_id).Member(member_id).Speak.post(params)

    def deaf_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Deaf.post()

    def undeaf_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Deaf.delete()

    def mute_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Mute.post()

    def unmute_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Unmute.delete()

    def kick_member(self, member_id):
        return self._api().Conference(conference_id).Member(member_id).Kick.post()

    def record_conference(self): 
        return self._api().Conference(conference_id).Record.post()

    def stop_record_conference(self): 
        return self._api().Conference(conference_id).Record.delete()

    ## Recordings ##
    def get_recordings(self, **params):
        return self._api().Recording.get(params)

    def get_recording(self, recording_id):
        return self._api().Recording(recording_id).get()

    def get_subaccount_recording(self, subauth_id, recording_id):
        return self._api().Subaccount(subauth_id).Recording(recording_id).get()

    ## Endpoints ##
    def get_endpoints(self, **params):
        return self._api().Endpoint.get(params)

    def create_endpoint(self, **params):
        return self._api().Endpoint.post(params)

    def get_endpoint(self, endpoint_id):
        return self._api().Endpoint(endpoint_id).get()

    def modify_endpoint(self, endpoint_id, **params):
        return self._api().Endpoint(endpoint_id).post(params)

    def delete_endpoint(self, endpoint_id):
        return self._api().Endpoint(endpoint_id).delete()

    def get_endpoint(self, endpoint_id):
        return self._api().Endpoint(endpoint_id).get()

    def modify_endpoint(self, endpoint_id, **params):
        return self._api().Endpoint(endpoint_id).post(params)

    def delete_endpoint(self, endpoint_id):
        return self._api().Endpoint(endpoint_id).delete()

    def create_subaccount_endpoint(self, subauth_id, **params):
        return self._api().Subaccount(subauth_id).Endpoint.post(params)

    def get_subaccount_endpoint(self, subauth_id, endpoint_id):
        return self._api().Subaccount(subauth_id).Endpoint(endpoint_id).get()

    def modify_subaccount_endpoint(self, subauth_id, endpoint_id, **params):
        return self._api().Subaccount(subauth_id).Endpoint(endpoint_id).post(params)

    def delete_subaccount_endpoint(self, subauth_id, endpoint_id):
        return self._api().Subaccount(subauth_id).Endpoint(endpoint_id).delete()

    ## Carriers ##
    def get_carriers(self, **params):
        return self._api().Carrier.get(params)

    def create_carrier(self, **params):
        return self._api().Carrier.post(params)

    def get_carrier(self, carrier_id):
        return self._api().Carrier(carrier_id).get()

    def modify_carrier(self, carrier_id, **params):
        return self._api().Carrier(carrier_id).post(params)

    def delete_carier(self, carrier_id):
        return self._api().Carrier(carrier_id).delete()

    ## Carrier Routings ##
    def get_carrier_routings(self, **params):
        return self._api().CarrierRouting.get(params)

    def create_carrier_routing(self, **params):
        return self._api().CarrierRouting.post(params)

    def get_carrier_routing(self, routing_id):
        return self._api().CarrierRouting(routing_id).get()

    def modify_carrier_routing(self, routing_id, **params):
        return self._api().CarrierRouting(routing_id).post(params)

    def delete_carrier_routing(self, routing_id):
        return self._api().CarrierRouting(routing_id).delete()



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


class Response(Element):
    nestables = ('Speak', 'Play', 'GetDigits', 'Record', 'Dial',
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
