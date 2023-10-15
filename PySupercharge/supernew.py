# -*- coding: utf-8 -*-
# Author: Nguyen Minh Hieu


import math
import bisect
import random
# from Bio.SeqUtils.ProtParam import ProteinAnalysis

from matplotlib import style
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


#-------------Supercharging Standalone Backend--------------

#Global variables
#Charge list of amino acids
chargeDict={'D': -1, 'T': 0, 'S': 0, 'E': -1, 'P': 0, 'G': 0, 'A': 0,\
            'C': 0, 'V': 0, 'M': 0, 'I': 0, 'L': 0, 'Y': 0,'F': 0,\
            'H': 0.1, 'K': 1, 'R': 1, 'W': 0, 'Q': 0, 'N': 0}


#Amino acid list
aaList=['D', 'T', 'S', 'E', 'P', 'G', 'A', 'C', 'V', 'M',
    'I', 'L', 'Y', 'F', 'H', 'K', 'R', 'W', 'Q', 'N']

#matplotlib style
style.use("seaborn-notebook")


#Class 
class superSeq(object):

    def __init__(self, seqRaw, filename='', name='protein',formated=False):
        if formated==False:
            self.seqStr = self.formatStr(seqRaw)
            self.seq = self.formatSeq(seqRaw)
        else:
            self.seqStr = seqRaw
            self.seq = list(seqRaw)
        self.name = name
        self.location = filename

    def __str__(self):
        return self.seqStr

    def __eq__(self, sSeq_):
        assert type(sSeq_) == superSeq
        return self.seqStr == sSeq_.seqStr

    def __len__(self):
        return len(self.seqStr)

    def __add__(self, sSeq_, name_=''):
        assert type(sSeq_) == superSeq
        newSeqRaw = self.seqStr + sSeq_.seqStr
        self = superSeq(newSeqRaw,name='',formated=True)

    def showLCD(self):
        charge = self.getChargePool(self.seqStr)

        x = range(len(charge))
        y = charge

        plt.plot(x, y)
        plt.axhline(4, 0, 1, alpha=0.6, color="orange")
        plt.xlabel("Window Index")
        plt.ylabel("Charge Index")
        plt.suptitle(self.name, fontsize=20)

        plt.show()

    def compareLCD(self, sSeq, threshold=4):
        assert type(sSeq) == superSeq
        x = range(len(self.getChargePool(self.seqStr)))
        y1 = sSeq.getCharge(self.seqStr)
        y2 = sSeq.getCharge(sSeq.seqStr)

        title = self.name + " normal(blue) vs charged(orange)"

        plt.plot(x, y1, color='blue')
        plt.plot(x, y2, color='orange')
        plt.axhline(threshold, 0, 1, alpha=0.6, color="#00F481")
        plt.xlabel("Window Index")
        plt.ylabel("Charge Index")
        plt.suptitle(title, fontsize=15)

        plt.show()

    def compareSeq(self, sSeq):
        assert len(self) == len(sSeq)
        diff_arr = []

        for i, aa in enumerate(sSeq.seq):
            pass
    
    @staticmethod
    def formatStr(seqRaw):
        assert type(seqRaw) == str
        seqStr = ''
        seqRaw = seqRaw.upper()
        
        for i in seqRaw:
            if i in aaList:
                seqStr += i

        return seqStr

    #format the string and remove characters that are not aminoacid
    @staticmethod
    def formatSeq(seqRaw):
        assert type(seqRaw) == str
        seqArray = []
        seqRaw = seqRaw.upper()
        
        for i in seqRaw:
            if i in aaList:
                seqArray.append(i)

        return seqArray
                    
    @staticmethod
    def getChargeArray(sStr):
        return [chargeDict[i] for i in sStr]

    #return the sequence which yield the charge of the input superSeq object
    #w stands for window size of the input
    @staticmethod
    def getChargePool(sStr, w=20):
        chargeArray = []

        for i in range(len(sStr)-(w-1)):
            chargeArray.append(round(sum([chargeDict[j] for j in sStr[i:i+w]]),1))

        return chargeArray

    @staticmethod
    def chargeArraytoPool(chArray, w=20):
        chargeArray = []

        for i in range(len(chArray)-w+1):
            chargeArray.append(round(sum([j for j in chArray[i:i+w]]),1))

        return chargeArray

    @staticmethod
    def getChargeSingle(seq,formated=True):
        if formated==False:
            seq = superSeq.formatStr(seq)

        return sum(round([chargeDict[i] for i in seq],1))



    @staticmethod
    def consurfReader(filename):
        if type(filename) != str or filename[-6:] != 'grades':
            print('please import again')
            return None
        # if type(filename) != str:
        #     print('please import again')
        #     return None
        else:
            if filename == "":
                return None

            scores,exposures,seqStr = [],[], ''

            with open(filename, "r") as f:
                flag = False
                for i, line in enumerate(f):
                    if i>15:
                        if flag and line == '\n': break
                        lineList = line.split()
                        if len(lineList)==0: continue
                        if lineList[0] == '1': flag=True 
                        if not flag: continue

                        try: float(lineList[2])
                        except: lineList.pop(2)
                        
                        scores.append(lineList[3])
                        seqStr += lineList[1]
                        if ','==lineList[4][-1]:
                            exposures.append(line.split()[7])    
                        else: exposures.append(line.split()[6])

            for i, score in enumerate(scores):
                if score[-1]=='*':
                    scores[i] = scores[i][:-1]
                scores[i] = int(scores[i])

            return scores,exposures,seqStr

    @staticmethod
    def formatSite(site):
        if site == None or site == '': return []
        # format: #1-#2+#3 (from #1 to #2 add #3)
        # output (tuple): (#1,...,#2,#3)

        siteList = site.split('+')
        newList = []

        for i in siteList:
            try: newList.append(int(i))
            except ValueError:
                op,ed = map(int, i.split('-'))
                for j in range(op,ed+1):
                    newList.append(j)
            

        return tuple(newList)
    

    def getSuperExhaustive(self,consurf=[], threshold=4, limit=-1, window=20,\
                           exclude=[], include=[],incl=False,target={'R','K'},standin=['D','E'], scores={}):
        charge = superSeq.getChargeArray(self.seqStr)
        aaseq = list(self.seqStr[:])
        n = len(charge)

        mutated = []
        mutatedScores = []

        for i in range(n-window):
            if round(sum(charge[i:i+window]),1) > threshold:
                for j in range(20)[::-1]:
                    if aaseq[i+j] in target and (i+j) not in exclude:
                        if (i+j) in include:
                            aaseq[i+j] = random.choice(standin)
                            charge[i+j] = chargeDict[aaseq[i+j]]
                            mutated.append(i+j)  
                            mutatedScores.append(scores[i+j])
                    if round(sum(charge[i:i+window]),1) < threshold:
                        break
                            
        return mutated, mutatedScores, charge, aaseq


    def superGraph(self,thres=4,limit=-1,w=20,excl={},incl={},tar={'R','K'},stand=['D','E'], scores={}):

        y1 = self.getChargePool(self.seqStr)
        
        mutated,mutatedScores,y2,newSeq = self.getSuperExhaustive(threshold=thres,window=w,exclude=excl, include=incl,target=tar,standin=stand,scores=scores)

        y2 = self.chargeArraytoPool(y2)

        x = range(len(y1))
        print(mutated)
        print(mutatedScores)

        return x,y1,y2,newSeq, mutated, mutatedScores


#----------------Unit Testing---------------

def test(sSeq):
    sSeq = superSeq(sSeq)
    charge = superSeq.getChargePool(sSeq.seqStr)

    x = range(len(charge))
    y = charge

    print(x, y)

# print(superSeq.consurfReader('G:\\OneDrive - xKx\\• Research R&E\\Supercharge\\new supercharging\\consurf.grades'))

# test("MLPGVGLTPS AAQTARQHPK MHLAHSTLKP AAHLIGDPSK QNSLLWRANT\
#         DRAFLQDGFS LSNNSLLVPT SGIYFVYSQV VFSGKAYSPK ATSSPLYLAH\
#         EVQLFSSQYP FHVPLLSSQK MVYPGLQEPW LHSMYHGAAF QLTQGDQLST\
#         HTDGIPHLVL SPSTVFFGAF AL")
