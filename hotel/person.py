#!python
#-*- coding:utf-8 -*-
__author__ = 'altnti'

import pymongo

class Person:
    def __init__(self):
        #self.keys = {'name':0, 'id':4, 'sex':5, 'bd':6, 'addr':7, 'zc':8, 'phone':19,
        #             'tel':20, 'fax':21, 'email':22, 'time':31, 'room':32}
        self.keys = [('name',0), ('id',4), ('sex',5), ('bd',6), ('addr',7), ('zc',8), ('phone',19),
                     ('tel',20), ('fax',21), ('email',22), ('time',31), ('room',32)]
        #self.idxs = [0, 4, 5, 6, 7, 8, 19, 20, 21, 22, ]

        #self.mongo = pymongo.MongoClient("192.168.0.9", 2015)
        #self.db    = self.mongo.hotel
        self.coll  = pymongo.MongoClient("192.168.0.9", 2015)['hotel']['guest']
        #print(self.db.name)

    def parse(self, items):
        for item in self.keys:
            print( "%s:%s" % (item[0], items[item[1]]) )

    def save_to_mongo(self, line):
        items = line.decode('utf-8').split(u',')
        #split = []
        json = {}
        for item in self.keys:
            json[item[0]] = items[item[1]]
            #split.append( "\"%s\":\"%s\"" % (item[0], items[item[1]]) )
        #json = "{" + ','.join(split) + "}"
        #print( json.encode('utf-8') )
        self.coll.insert_one( json )

