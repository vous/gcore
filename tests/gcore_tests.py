# -*- coding: utf-8 *-*
from nose.tools import *
import gcore

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
