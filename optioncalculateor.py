# -*- coding:utf-8 -*-
#@author: naiveyueya
__version__ = '0.0.1'
import numpy as np

def pricetree(layer,u,d,price0, outerlist = [[1]]):
    if layer>0:
        temp = []
        for k in outerlist[-1]:
            temp.append(k*u)
        temp.append(outerlist[-1][-1]*d)
        outerlist.append(temp)
        pricetree(layer-1,u,d,price0,outerlist)
    return list(np.array(outerlist) * price0)

def premiumtree(layer, lastprice, K, up):
    if len(lastprice)!=layer+1:
        return False
    lastrow = list(map(lambda x: max(x-K, 0), lastprice))
    def part(layer2,indexlist):
        if layer2 >= 0 :
            temp = []
            for i in range(len(indexlist[-1])-1):
                temp.append(indexlist[-1][i] * up+indexlist[-1][i+1] * (1-up))
            indexlist.append(temp)
            part(layer2-1,indexlist)
        return indexlist
    result = part(layer-1,[lastrow])
    return result[::-1]



