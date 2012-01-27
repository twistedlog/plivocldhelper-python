# -*- coding: utf-8 -*-

__VERSION__ = "v1"


import urllib, urllib2, base64, hmac
from urlparse import urlparse
from urllib import quote
from hashlib import sha1
from xml.dom.minidom import Document
try:
    import json
except ImportError:
    import simplejson as json
import httplib2


class PlivoException(Exception): 
    pass


def request(url, method, params={}, extra_headers={}, auth_user=None, auth_password=None, timeout=30):
    headers = {'User-Agent':'PlivoHelper'}
    headers.update(extra_headers)

    if method in ('POST', 'PUT'):
        headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    elif method in ('GET', 'DELETE'):
        if params:
            qs = urlparse(url).query
            encoded_params = urllib.urlencode(params, doseq=True)
            if qs:
                url = '%s&%s' % (url, encoded_params)
            else:
                url = '%s?%s' % (url, encoded_params)
        params = {}

    h = httplib2.Http(".cache", timeout=timeout)
    h.follow_all_redirects = True

    if auth_user and auth_password:
        h.add_credentials(auth_user, auth_password)

    if method == 'POST':
        r, content = h.request(url, "POST", body=urllib.urlencode(params), headers=headers)
    elif method == 'DELETE':
        r, content = h.request(url, "DELETE", body='', headers=headers)
    elif method == 'PUT':
        r, content = h.request(url, "PUT", body=urllib.urlencode(params), headers=headers)
    else:
        r, content = h.request(url, "GET", headers=headers)
    return (r.status, content, r)


class REST(object):
    """Plivo helper class for making REST apis requests"""
    def __init__(self, auth_id='', auth_token='', 
                 api_version=__VERSION__,
                 url='http://api.plivo.com'):
        self.url = url.rstrip('/')
        self.auth_id = auth_id
        self.auth_token = auth_token
        self.opener = None
        self.api_version = api_version

    def request(self, path, method='POST', data={}):
        """sends a request and gets a response from the Plivo REST API

        path: the URL (relative to the endpoint URL, after the /v1
        method: the HTTP method to use, defaults to POST
        data: for POST or PUT, a dict of data to send

        returns Plivo response in XML or raises an exception on error
        """
        if not path:
            raise ValueError('Invalid path parameter')
        if method and method not in ['GET', 'POST', 'DELETE', 'PUT']:
            raise NotImplementedError(
                'HTTP %s method not implemented' % method)
        uri = self.url + '/' + self.api_version + path
        code, content, rh = request(uri, method, params=data, 
                                    auth_user=self.auth_id,
                                    auth_password=self.auth_token
                                   )
        if code > 204:
            error = {'error':content}
            return (code, error)
        if content:
            content = json.loads(content)
        else:
            content = {}
        return (code, content)

    ## Accounts ##
    def account(self):
        path = '/Account/'
        method = 'GET'
        return self.request(path, method)

    def account_info(self):
        path = '/Account/%s/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    def account_change(self, **params):
        path = '/Account/%s/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    ## Subaccount ##
    def subaccount_info(self, subauth_id, **params):
        path = '/Account/%s/Subaccount/%s/' % (self.auth_id, subauth_id)
        method = 'GET'
        return self.request(path, method, params)

    def subaccount_change(self, subauth_id, **params):
        path = '/Account/%s/Subaccount/%s/' % (self.auth_id, subauth_id)
        method = 'POST'
        return self.request(path, method, params)

    def subaccount_delete(self, subauth_id):
        path = '/Account/%s/Subaccount/%s/' % (self.auth_id, subauth_id)
        method = 'DELETE'
        return self.request(path, method)

    ## Applications ##
    def applications_info(self, **params):
        path = '/Account/%s/Applications/' % self.auth_id
        method = 'GET'
        return self.request(path, method, params)

    def application_create(self, **params):
        path = '/Account/%s/Applications/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    def application_info(self, app_id):
        path = '/Account/%s/Applications/%s/' % (self.auth_id, app_id)
        method = 'GET'
        return self.request(path, method)

    def application_change(self, app_id, **params):
        path = '/Account/%s/Applications/%s/' % (self.auth_id, app_id)
        method = 'GET'
        return self.request(path, method, params)

    def application_delete(self, app_id):
        path = '/Account/%s/Applications/%s/' % (self.auth_id, app_id)
        method = 'DELETE'
        return self.request(path, method)

    ## Incoming Numbers ##
    def incoming_numbers_info(self, **params):
        path = '/Account/%s/IncomingNumbers/' % self.auth_id
        method = 'GET'
        return self.request(path, method, params)

    def incoming_number_order(self, **params):
        path = '/Account/%s/IncomingNumbers/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    def incoming_number_info(self, number):
        path = '/Account/%s/IncomingNumbers/%s/' % (self.auth_id, number)
        method = 'GET'
        return self.request(path, method)

    def incoming_number_change(self, number, **params):
        path = '/Account/%s/IncomingNumbers/%s/' % (self.auth_id, number)
        method = 'POST'
        return self.request(path, method, params)

    def incoming_number_delete(self, number):
        path = '/Account/%s/IncomingNumbers/%s/' % (self.auth_id, number)
        method = 'DELETE'
        return self.request(path, method)

    ## Schedule ##
    def schedule_cancel(self, task_id):
        path = '/Account/%s/ScheduleCancel/%s/' % (self.auth_id, task_id)
        method = 'DELETE'
        return self.request(path, method)

    ## Outgoing Caller ID ##
    def outgoing_callerids_info(self, **params):
        path = '/Account/%s/OutgoingCallerIds/' % self.auth_id
        method = 'GET'
        return self.request(path, method, params)

    def outgoing_callerid_add(self, **params):
        path = '/Account/%s/OutgoingCallerIds/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    ## Calls ##
    def calls_info(self):
        path = '/Account/%s/Calls/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    def make_call(self, **params):
        path = '/Account/%s/Calls/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    def calls_hangup(self):
        path = '/Account/%s/Calls/' % self.auth_id
        method = 'DELETE'
        return self.request(path, method)

    def call_info(self, calluuid):
        path = '/Account/%s/Calls/%s/' % (self.auth_id, calluuid)
        method = 'GET'
        return self.request(path, method)

    def call_transfer(self, calluuid, params):
        path = '/Account/%s/Calls/%s/' % (self.auth_id, calluuid)
        method = 'POST'
        return self.request(path, method, params)

    def call_hangup(self, calluuid):
        path = '/Account/%s/Calls/%s/' % (self.auth_id, calluuid)
        method = 'DELETE'
        return self.request(path, method)

    def call_record_start(self, calluuid, **params):
        path = '/Account/%s/Calls/%s/Record/' % (self.auth_id, calluuid)
        method = 'POST'
        return self.request(path, method, params)

    def call_record_stop(self, calluuid, **params):
        path = '/Account/%s/Calls/%s/Record/' % (self.auth_id, calluuid)
        method = 'DELETE'
        return self.request(path, method, params)

    def call_play_start(self, calluuid, **params):
        path = '/Account/%s/Calls/%s/Play/' % (self.auth_id, calluuid)
        method = 'POST'
        return self.request(path, method, params)

    def call_play_stop(self, calluuid):
        path = '/Account/%s/Calls/%s/Play/' % (self.auth_id, calluuid)
        method = 'DELETE'
        return self.request(path, method)

    def call_send_dtmf(self, calluuid, **params):
        path = '/Account/%s/Calls/%s/DTMF/' % (self.auth_id, calluuid)
        method = 'POST'
        return self.request(path, method, params)

    def call_recordings(self, calluuid):
        path = '/Account/%s/Calls/%s/Recordings/' % (self.auth_id, calluuid)
        method = 'GET'
        return self.request(path, method)

    def call_logs(self, calluuid):
        path = '/Account/%s/Calls/%s/Logs/' % (self.auth_id, calluuid)
        method = 'GET'
        return self.request(path, method)

    ## Calls Requests ##
    def request_hangup(self, requestuuid):
        path = '/Account/%s/Requests/%s/' % (self.auth_id, requestuuid)
        method = 'DELETE'
        return self.request(path, method)

    ## Conferences ##
    def conferences_info(self):
        path = '/Account/%s/Conferences/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    def conferences_hangup(self):
        path = '/Account/%s/Conferences/' % self.auth_id
        method = 'DELETE'
        return self.request(path, method)
        
    def conference_info(self, conference_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/' % (self.auth_id, conf)
        method = 'GET'
        return self.request(path, method)

    def conference_hangup(self, conference_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/' % (self.auth_id, conf)
        method = 'DELETE'
        return self.request(path, method)

    def conference_hangup_member(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/' % (self.auth_id, conf, member_id)
        method = 'DELETE'
        return self.request(path, method)

    def conference_play_start(self, conference_id, member_id, **params):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Play/' % (self.auth_id, conf, member_id)
        method = 'POST'
        return self.request(path, method, params)

    def conference_play_stop(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Play/' % (self.auth_id, conf, member_id)
        method = 'DELETE'
        return self.request(path, method)

    def conference_speak(self, conference_id, member_id, **params):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Speak/' % (self.auth_id, conf, member_id)
        method = 'POST'
        return self.request(path, method, params)

    def conference_deaf(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Deaf/' % (self.auth_id, conf, member_id)
        method = 'POST'
        return self.request(path, method)
        
    def conference_undeaf(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Deaf/' % (self.auth_id, conf, member_id)
        method = 'DELETE'
        return self.request(path, method)

    def conference_mute(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Mute/' % (self.auth_id, conf, member_id)
        method = 'POST'
        return self.request(path, method)
        
    def conference_unmute(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Mute/' % (self.auth_id, conf, member_id)
        method = 'DELETE'
        return self.request(path, method)

    def conference_kick(self, conference_id, member_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Members/%s/Kick/' % (self.auth_id, conf, member_id)
        method = 'DELETE'
        return self.request(path, method)

    def conference_record_start(self, conference_id, **params):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Record/' % (self.auth_id, conf)
        method = 'POST'
        return self.request(path, method)

    def conference_record_stop(self, conference_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Record/' % (self.auth_id, conf)
        method = 'DELETE'
        return self.request(path, method)

    def conference_recordings_info(self, conference_id):
        conf = quote(conference_id)
        path = '/Account/%s/Conferences/%s/Recordings/' % (self.auth_id, conf)
        method = 'GET'
        return self.request(path, method)

    ## Recordings ##
    def account_recordings_info(self):
        path = '/Account/%s/Recordings/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    ## Endpoints ##
    def endpoints_info(self):
        path = '/Account/%s/Endpoints/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    def endpoint_create(self, **params):
        path = '/Account/%s/Endpoints/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    def endpoints_delete_all(self):
        path = '/Account/%s/Endpoints/' % self.auth_id
        method = 'DELETE'
        return self.request(path, method, params)

    def endpoint_info(self, endpoint_id):
        path = '/Account/%s/Endpoints/%s/' % (self.auth_id, endpoint_id)
        method = 'GET'
        return self.request(path, method)

    def endpoint_delete(self, endpoint_id):
        path = '/Account/%s/Endpoints/%s/' % (self.auth_id, endpoint_id)
        method = 'DELETE'
        return self.request(path, method)

    ## Carriers ##
    def carriers_info(self):
        path = '/Account/%s/Carriers/' % self.auth_id
        method = 'GET'
        return self.request(path, method)

    def carrier_create(self, **params):
        path = '/Account/%s/Carriers/' % self.auth_id
        method = 'POST'
        return self.request(path, method, params)

    def carrier_info(self, carrier_id):
        path = '/Account/%s/Carriers/%s/' % (self.auth_id, carrier_id)
        method = 'GET'
        return self.request(path, method)

    def carrier_delete(self, carrier_id):
        path = '/Account/%s/Carriers/%s/' % (self.auth_id, carrier_id)
        method = 'DELETE'
        return self.request(path, method)

    ## Rates ##
    def rates(self, **params):
        path = '/Account/%s/Rates/' % self.auth_id
        method = 'GET'
        return self.request(path, method, params)



class Element(object):
    """Plivo basic element object.
    """
    VALID_ATTRS = ()

    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.body = None
        self.nestables = ()
        self.elements = []
        self.attrs = {}
        for k, v in kwargs.items():
            if k == "sender":
                k = "from"
            self._is_valid_attribute(k)
            v = Element.bool2txt(v)
            if v is not None:
                self.attrs[k] = unicode(v)

    def _is_valid_attribute(self, attr):
        if not attr in self.VALID_ATTRS:
            raise PlivoException("Invalid attribute '%s' for Element %s" \
                % (attr, self.name))

    @staticmethod
    def bool2txt(var):
        """Map True to 'true'
        and False to 'false'
        else don't modify value
        """
        if var is True:
            return 'true'
        elif var is False:
            return 'false'
        return var

    def __repr__(self):
        """
        String representation of a element
        """
        doc = Document()
        return self._xml(doc).toxml()

    def _xml(self, root):
        """
        Return an XML element representing this element
        """
        element = root.createElement(self.name)

        # Add attributes
        keys = self.attrs.keys()
        keys.sort()
        for a in keys:
            element.setAttribute(a, self.attrs[a])

        if self.body:
            text = root.createTextNode(self.body)
            element.appendChild(text)

        for c in self.elements:
            element.appendChild(c._xml(root))

        return element

    @staticmethod
    def check_post_get_method(method=None):
        if not method in ('GET', 'POST'):
            raise PlivoException("Invalid method parameter, must be 'GET' or 'POST'")

    def append(self, element):
        if not self.nestables:
            raise PlivoException("%s is not nestable" % self.name)
        if not element.name in self.nestables:
            raise PlivoException("%s is not nestable inside %s" % \
                            (element.name, self.name))
        self.elements.append(element)
        return element

    def asUrl(self):
        return urllib.quote(str(self))

    def addSpeak(self, text, **kwargs):
        return self.append(Speak(text, **kwargs))

    def addPlay(self, url, **kwargs):
        return self.append(Play(url, **kwargs))

    def addWait(self, **kwargs):
        return self.append(Wait(**kwargs))

    def addRedirect(self, url=None, **kwargs):
        return self.append(Redirect(url, **kwargs))

    def addHangup(self, **kwargs):
        return self.append(Hangup(**kwargs))

    def addGetDigits(self, **kwargs):
        return self.append(GetDigits(**kwargs))

    def addNumber(self, number, **kwargs):
        return self.append(Number(number, **kwargs))

    def addUser(self, user, **kwargs):
        return self.append(User(user, **kwargs))

    def addDial(self, **kwargs):
        return self.append(Dial(**kwargs))

    def addRecord(self, **kwargs):
        return self.append(Record(**kwargs))

    def addConference(self, name, **kwargs):
        return self.append(Conference(name, **kwargs))

    def addPreAnswer(self, **kwargs):
        return self.append(PreAnswer(**kwargs))


class Response(Element):
    VALID_ATTRS = ()

    def __init__(self):
        Element.__init__(self)
        self.nestables = ('Speak', 'Play', 'GetDigits', 'Record', 'Dial',
                        'Redirect', 'Wait', 'Hangup', 'PreAnswer', 'Conference')

class Speak(Element):
    VALID_ATTRS = ('voice', 'language', 'loop')

    def __init__(self, text, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = text


class Play(Element):
    VALID_ATTRS = ('loop',)

    def __init__(self, url, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = url


class Wait(Element):
    VALID_ATTRS = ('length',)

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)


class Redirect(Element):
    VALID_ATTRS = ('method',)

    def __init__(self, url=None, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = url


class Hangup(Element):
    VALID_ATTRS = ('schedule', 'reason')

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)


class GetDigits(Element):
    VALID_ATTRS = ('action', 'method', 'timeout', 'finishOnKey',
                   'numDigits', 'retries', 'invalidDigitsSound',
                   'validDigits', 'playBeep')

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)
        self.nestables = ('Speak', 'Play', 'Wait')


class Number(Element):
    VALID_ATTRS = ('sendDigits', 'sendOnPreanswer')

    def __init__(self, number, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = number


class User(Element):
    VALID_ATTRS = ('sendDigits', 'sendOnPreanswer')

    def __init__(self, number, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = number


class Conference(Element):
    VALID_ATTRS = ('muted','beep','startConferenceOnEnter',
                   'endConferenceOnExit','waitSound','enterSound', 'exitSound',
                   'timeLimit', 'hangupOnStar', 'maxMembers',
                   'record', 'recordFileFormat', 'action', 'method', 'redirect',
                   'digitsMatch', 'callbackUrl', 'callbackMethod', 
                   'stayAlone', 'floorEvent')

    def __init__(self, room, **kwargs):
        Element.__init__(self, **kwargs)
        self.body = room


class Dial(Element):
    VALID_ATTRS = ('action','method','timeout','hangupOnStar',
                   'timeLimit','callerId', 'callerName', 'confirmSound',
                   'dialMusic', 'confirmKey', 'redirect',
                   'callbackUrl', 'callbackMethod', 'digitsMatch')

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)
        self.nestables = ('Number', 'User')


class Record(Element):
    VALID_ATTRS = ('action', 'method', 'timeout','finishOnKey',
                   'maxLength', 'bothLegs', 'playBeep',
                   'redirect', 'fileFormat')

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)


class PreAnswer(Element):
    VALID_ATTRS = ()

    def __init__(self, **kwargs):
        Element.__init__(self, **kwargs)
        self.nestables = ('Play', 'Speak', 'GetDigits', 'Wait', 'Redirect', 'SIPTransfer')



class Utils(object):
    def __init__(self, auth_id='', auth_token=''):
        """initialize a plivo utility object

        auth_id: Plivo account SID/ID
        auth_token: Plivo account token

        returns a Plivo util object
        """
        self.auth_id = auth_id
        self.auth_token = auth_token

    def validateRequest(self, uri, postVars, expectedSignature):
        """validate a request from plivo

        uri: the full URI that Plivo requested on your server
        postVars: post vars that Plivo sent with the request
        expectedSignature: signature in HTTP X-Plivo-Signature header

        returns true if the request passes validation, false if not
        """

        # append the POST variables sorted by key to the uri
        s = uri
        for k, v in sorted(postVars.items()):
            s += k + v

        # compute signature and compare signatures
        return (base64.encodestring(hmac.new(self.auth_token, s, sha1).digest()).\
            strip() == expectedSignature)

