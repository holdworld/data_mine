#!python
#-*- coding:utf-8 -*-
__author__ = 'altnti'

import pymongo

class Person:
    def __init__(self):
        self.keys = [('name',0), ('id',4), ('sex',5), ('bd',6), ('addr',7), ('zc',8), ('phone',19),
                     ('tel',20), ('fax',21), ('email',22), ('time',31), ('room',32)]

        self.coll = pymongo.MongoClient("192.168.0.9", 2015)['hotel']['guest']

        self.operator = {8:self.parse_8,33:self.parse_33}

    def preprocess(self, line):
        end     = -1
        replace = []
        while True:
            try:
                begin = line.index(u'\"', end+1)
                end   = line.index(u'\"', begin+1)
                old   = line[begin:end+1]
                new   = old.replace(u',', u'，')
                replace.append((old, new))
            except:
                break

        for item in replace:
            line = line.replace(item[0], item[1])

        return line

    def parse(self, line):
        line  = self.preprocess(line.decode('utf-8'))
        items = line.split(u',')

        try:
            json = self.operator[len(items)](items)
            #print ','.join(["%s:%s"%(k,v) for k,v in json.items()])
        except:
            print(line)

    def parse_8(self, items):
        json = {}
        for i in range(0, 5):
            key = self.keys[i]
            if len(items[key[1]])!=0:
                json[key[0]] = items[key[1]]
        return json

    def parse_33(self, items):
        json = {}
        for key in self.keys:
            if len(items[key[1]])!=0:
                json[key[0]] = items[key[1]]
        return json

    def save_to_mongo(self, line):
        self.coll.insert_one( self.parse(line) )

