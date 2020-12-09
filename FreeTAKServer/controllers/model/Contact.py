#######################################################
# 
# Contact.py
# Python implementation of the Class Contact
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:08 AM
# Original author: Corvo
# 
#######################################################
from .ContactVariables import ContactVariables as vars

class Contact:
    def __init__(self):
        self.callsign = None 
        self.endpoint = None
        self.iconsetpath = None
        self.uid = None
        self.name = None

    @staticmethod
    def drop_point(CALLSIGN = vars.drop_point().CALLSIGN):
        contact = Contact()
        contact.setcallsign(callsign=CALLSIGN)
        return contact

    @staticmethod
    def connection(CALLSIGN = vars.connection().CALLSIGN, ENDPOINT = vars.connection().ENDPOINT,
                   ICONSETPATH = vars.connection().ICONSETPATH,UID = vars.connection().UID,
                   NAME = vars.connection().NAME):

        contact = Contact()
        contact.setcallsign(CALLSIGN)
        contact.setname(NAME)
        contact.setuid(UID)
        contact.setendpoint(ENDPOINT)
        contact.seticonsetpath(ICONSETPATH)
        return contact

    @staticmethod
    def geochat(CALLSIGN=vars.geochat().CALLSIGN, ENDPOINT=vars.geochat().ENDPOINT,
                   ICONSETPATH=vars.geochat().ICONSETPATH, UID=vars.geochat().UID,
                   NAME=vars.geochat().NAME):
        contact = Contact()
        contact.setcallsign(CALLSIGN)
        contact.setname(NAME)
        contact.setuid(UID)
        contact.setendpoint(ENDPOINT)
        contact.seticonsetpath(ICONSETPATH)
        return contact

    @staticmethod
    def emergency_on(CALLSIGN=vars.emergency_on().CALLSIGN, ENDPOINT=vars.emergency_on().ENDPOINT,
                ICONSETPATH=vars.emergency_on().ICONSETPATH, UID=vars.emergency_on().UID,
                NAME=vars.emergency_on().NAME):
        contact = Contact()
        contact.setcallsign(CALLSIGN)
        contact.setname(NAME)
        contact.setuid(UID)
        contact.setendpoint(ENDPOINT)
        contact.seticonsetpath(ICONSETPATH)
        return contact

    # iconsetpath getter 
    def geticonsetpath(self): 
        return self.iconsetpath 
 
    # iconsetpath setter 
    def seticonsetpath(self, iconsetpath=None):
        self.iconsetpath=iconsetpath 
 
    # callsign getter 
    def getcallsign(self): 
        return self.callsign 
 
    # callsign setter 
    def setcallsign(self, callsign=None):
        self.callsign=callsign 
 
     
    # endpoint getter 
    def getendpoint(self): 
        return self.endpoint 
 
    # endpoint setter 
    def setendpoint(self, endpoint=None):
        self.endpoint=endpoint

    def getuid(self):
        return self.uid

        # uid setter 

    def setuid(self, uid=None):
        self.uid = uid 
        
    def getname(self):
        return self.name

        # name setter 

    def setname(self, name=None):
        self.name = name

    def getphone(self):
        return self.phone

    def setphone(self, phone=None):
        self.phone = phone
