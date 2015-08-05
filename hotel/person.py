#!python
#-*- coding:utf-8 -*-
__author__ = 'altnti'

import pymongo

class Person:
    def __init__(self):
        self.keys = [('name',0), ('id',4), ('sex',5), ('bd',6), ('addr',7), ('zc',8), ('phone',19),
                     ('tel',20), ('fax',21), ('email',22), ('time',31), ('room',32)]

        self.coll = pymongo.MongoClient("192.168.0.9", 2015)['hotel']['guest']

    def parse(self, items):
        for item in self.keys:
            print( "%s:%s" % (item[0], items[item[1]]) )

    def save_to_mongo(self, line):
        items = line.decode('utf-8').split(u',')
        if len(items) != 33:
            return

        json = {}
        for item in self.keys:
            json[item[0]] = items[item[1]]
        self.coll.insert_one( json )

