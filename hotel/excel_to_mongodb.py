#!python
#-*- coding:utf-8 -*-

from person import Person

__author__ = 'altnti'

def excel_to_mongodb(path):
    excel = open(path, 'r')
    excel.seek(3)
    print(excel.readline())

    person = Person();
    line = excel.readline().strip('\n')
    person.save_to_mongo(line)
    #while len(line)>0:
        #person.parse( excel.readline().decode('utf-8').split(u',') )
        #line = excel.readline()

if __name__ == '__main__':
    excel_to_mongodb("K:\\mongodb\\1-200W.csv")
