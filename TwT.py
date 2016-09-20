#!/usr/bin/env python

import CRFPP


"""
input: string
ouput: seq list
"""
class Seg2List:

    modeldir = ""
    inputstr = ""

    def __init__(self, crfmodel, mstr):
        self.modeldir = crfmodel
        self.inputstr = mstr

    def seg(self):
        tagger = CRFPP.Tagger("-m " + self.modeldir + " -v 3 -n2")
        for word in self.inputstr.strip():
            tagger.add(word)
        tagger.parse()

        size = tagger.size()
        xsize = tagger.xsize()

        mlist = []
        mstr = ""
        for i in range(0, size):
            for j in range(0, xsize):
                char = tagger.x(i, j)
                tag = tagger.y2(i)

                if tag == 'B':
                    mstr += char
                elif tag == 'M':
                    mstr += char
                elif tag == 'E':
                    mstr += char
                    mlist.append(mstr)
                    mstr = ""
                else:  # tag == 'S'
                    mlist.append(char)
        return mlist