#!python
#-*- coding:utf-8 -*-
__author__ = 'altnti'

import pymongo

class Person:
    def __init__(self):
        self.keys = [('id',3), ('sex',4), ('bd',5), ('addr',6), ('zc',7), ('phone',18),
                     ('tel',19), ('fax',20), ('email',21), ('time',30), ('room',31)]

        self.coll = pymongo.MongoClient("192.168.0.9", 2015)['hotel']['guest']

        self.operator = {32:self.parse_32, 7:self.parse_7};

    def parse(self, line):
        line = line.decode('utf-8')
        name = u''
        if line[0]==u'\"':
            try:
                idx  = line.index(u"\"",1)
                name = line[1:idx]
                line = line[idx+2:]
            except:
                print line
        else:
            idx  = line.index(u",")
            name = line[0:idx]
            line = line[idx+1:]
        items = line.split(u',')

        try:
            json = {}
            self.operator[len(items)](items, json)
            json["name"] = name
            print ','.join(["%s:%s"%(k,v) for k,v in json.items()])
        except:
            pass

    def parse_7(self, items, json):
        for i in range(0, 4):
            key = self.keys[i]
            if len(items[key[1]])!=0:
                json[key[0]] = items[key[1]]

    def parse_32(self, items, json):
        for key in self.keys:
            if len(items[key[1]])!=0:
                json[key[0]] = items[key[1]]

    def parse_34(self, items, json):
        pass

    def save_to_mongo(self, line):
        self.coll.insert_one( self.parse(line) )

