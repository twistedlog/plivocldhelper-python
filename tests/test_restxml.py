# -*- coding: utf-8 -*-
import unittest
import plivocldhelper
import re

class PlivoTest(unittest.TestCase):
    def strip(self, xml):
        return re.sub(r'\n|\t', '', str(xml).strip())

    def improperAppend(self, verb):
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Speak(""))
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.GetDigits())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Play(""))
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Record())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Hangup())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Redirect())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Dial())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Conference(""))
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Wait())

class TestResponse(PlivoTest):

    def testEmptyResponse(self):
        r = plivocldhelper.Response()
        self.assertEquals(self.strip(r), "<Response/>")

class TestSpeak(PlivoTest):

    def testEmptySpeak(self):
        """should be a say with no text"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Speak(""))
        self.assertEquals(self.strip(r), '<Response><Speak/></Response>')

    def testSpeakHelloWorld(self):
        """should say hello monkey"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Speak("Hello World"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Speak>Hello World</Speak></Response>')

    def testSpeakLoop(self):
        """should say hello monkey and loop 3 times"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Speak("Hello Monkey", loop=3))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Speak loop="3">Hello Monkey</Speak></Response>')

    def testSpeakAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                          plivocldhelper.Speak, "", foo="bar")

    def testSpeakBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Speak(""))

class TestPlay(PlivoTest):

    def testEmptyPlay(self):
        """should play hello monkey"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Play(""))
        r = self.strip(r)
        self.assertEqual(r,"<Response><Play/></Response>")

    def testPlayHello(self):
        """should play hello monkey"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Play("http://hellomonkey.mp3"))
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play>http://hellomonkey.mp3</Play></Response>')

    def testPlayHelloLoop(self):
        """should play hello monkey loop"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Play("http://hellomonkey.mp3", loop=3))
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayConvienceMethod(self):
        """convenience method: should play hello monkey"""
        r = plivocldhelper.Response()
        r.addPlay("http://hellomonkey.mp3", loop=3)
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                          plivocldhelper.Play, "", foo="bar")

    def testPlayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Play(""))

class TestRecord(PlivoTest):

    def testRecordEmpty(self):
        """should record"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Record())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record/></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Record(timeout=4,finishOnKey="#", maxLength=30))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="#" maxLength="30" timeout="4"/></Response>')
  
    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = plivocldhelper.Response()
        r.addRecord(timeout=4,finishOnKey="#", maxLength=30)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="#" maxLength="30" timeout="4"/></Response>')

    def testRecordAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                          plivocldhelper.Record, foo="bar")

    def testRecordBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Record())

class TestRedirect(PlivoTest):

    def testRedirectEmpty(self):
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Redirect())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect/></Response>')

    def testRedirectMethod(self):
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Redirect(url="example.com", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com</Redirect></Response>')

    def testRedirectMethodGetParams(self):
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Redirect(url="example.com?id=34&action=hey", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>')

    def testAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                          plivocldhelper.Redirect, "", foo="bar")

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Redirect())


class TestHangup(PlivoTest):

    def testHangup(self):
        """convenience: should Hangup to a url via POST"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Hangup())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup/></Response>')

    def testHangupConvience(self):
        """convenience: should Hangup to a url via POST"""
        r = plivocldhelper.Response()
        r.addHangup()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup/></Response>')

    def testSchedule(self):
        r = plivocldhelper.Response()
        r.addHangup(schedule=10)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup schedule="10"/></Response>')

    def testSchedule(self):
        r = plivocldhelper.Response()
        r.addHangup(reason="rejected")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup reason="rejected"/></Response>')

    def testAddAttribute(self):
        self.assertRaises(plivocldhelper.PlivoException,
                          plivocldhelper.Hangup, foo="bar")

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Hangup())


class TestDial(PlivoTest):

    def testDial(self):
        """ should redirect the call"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Dial("1231231234"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testConvienceMethod(self):
        """ should dial to a url via post"""
        r = plivocldhelper.Response()
        r.addDial()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial/></Response>')

    def testAddNumber(self):
        """add a number to a dial"""
        r = plivocldhelper.Response()
        d = plivocldhelper.Dial()
        d.append(plivocldhelper.Number("1231231234"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddNumberConvience(self):
        """add a number to a dial, convience method"""
        r = plivocldhelper.Response()
        d = r.addDial()
        d.addNumber("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')

class TestConference(PlivoTest):

    def testAddConference(self):
        """ add a conference to a dial"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.Conference("My Room"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Conference>My Room</Conference></Response>')

    def testAddConferenceConvenceMethod(self):
        """ add a conference to a dial, conviently"""
        r = plivocldhelper.Response()
        r.addConference("My Room")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Conference>My Room</Conference></Response>')

    def testAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                    plivocldhelper.Conference, "MyRoom", foo="bar")

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(plivocldhelper.Conference("Hello"))


class TestGetDigits(PlivoTest):

    def testEmpty(self):
        """ a gather with nothing inside"""
        r = plivocldhelper.Response()
        r.append(plivocldhelper.GetDigits())
        r = self.strip(r)
        self.assertEquals(r, '<Response><GetDigits/></Response>')

    def testAddAttribute(self):
        """add attribute"""
        self.assertRaises(plivocldhelper.PlivoException,
                    plivocldhelper.GetDigits, foo="bar")

    def testNestedSpeakPlayWait(self):
        """ a gather with a say, play, and pause"""
        r = plivocldhelper.Response()
        g = plivocldhelper.GetDigits()
        g.append(plivocldhelper.Speak("Hey"))
        g.append(plivocldhelper.Play("hey.mp3"))
        g.append(plivocldhelper.Wait())
        r.append(g)
        r = self.strip(r)
        self.assertEquals(r, '<Response><GetDigits><Speak>Hey</Speak><Play>hey.mp3</Play><Wait/></GetDigits></Response>')


    def testNestedSpeakPlayWaitConvience(self):
        """ a gather with a say, play, and pause"""
        r = plivocldhelper.Response()
        g = r.addGetDigits()
        g.addSpeak("Hey")
        g.addPlay("hey.mp3")
        g.addWait()
        r = self.strip(r)
        self.assertEquals(r, '<Response><GetDigits><Speak>Hey</Speak><Play>hey.mp3</Play><Wait/></GetDigits></Response>')

    def testImproperNesting(self):
        """ bad nesting"""
        verb = plivocldhelper.GetDigits()
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.GetDigits())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Record())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Hangup())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Redirect())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Dial())
        self.assertRaises(plivocldhelper.PlivoException, verb.append, plivocldhelper.Conference(""))

if __name__ == '__main__':
    unittest.main()
