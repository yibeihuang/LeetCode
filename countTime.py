__author__ = 'yibeihuang'

import sys

class Solution(object):
    def CountTime(self):
        total, connect = 0, 0
        flag = 0
        for line in sys.stdin:
            currtime = line.split('::')[0]
            status = line.split('::')[1]
            if status=='START':
                starttime = currtime
            elif status=='SHUTDOWN':
                endtime = currtime
                total = endtime-starttime
                if flag==1: connect=connect+(endtime-conntime)
            elif status=='CONNECTED':
                if flag==0: conntime, flag = currtime, 1
                else: continue
            elif status=='DISCONNECTED':
                if flag==0: continue
                else:
                    disconntime, flag = currtime, 1
                    connect = connect+(disconntime-conntime)
        rst = connect/total
        return  rst
