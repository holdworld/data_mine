#!python
#-*- coding:utf-8 -*-

from person import Person

__author__ = 'altnti'

def excel_to_mongodb(path):
    excel = open(path, 'r')
    excel.seek(3)
    print(excel.readline())

    num    = 0
    person = Person()
    line   = excel.readline().strip('\n')
    while len(line)>0:
        num += 1
        person.save_to_mongo( line )
        line = excel.readline().strip('\n')

    print("total:%s"%num)


if __name__ == '__main__':
    excel_to_mongodb("K:\\mongodb\\1-200W.csv")
