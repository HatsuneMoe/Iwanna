#!/usr/bin/env python
# encoding=utf-8

import re
import traceback


class ReQuQ:
    @staticmethod
    def word2trainset(_str, _file):
        restr = '(\S*)/[a-z]?.'
        reformat = re.compile(restr)
        resultlist = re.findall(reformat, _str)

        if len(resultlist) > 0:
            for s in resultlist:
                if len(s) > 1:
                    _file.write(s[0] + '\tB\n')
                    for i in s[1:len(s)-1]:
                        _file.write(i + '\tM\n')
                    _file.write(s[len(s)-1] + '\tE\n')
                else:
                    _file.write(s + '\tS\n')
        else:
            print("word empty")
            return

    def pd2crfsuite(self):
        try:
            with open("convtest.txt", "r", encoding="utf=8") as text:
                try:
                    with open("convtest_trans.txt", "a", encoding="utf=8") as _file:
                        _file.truncate(0)

                        for line in text.readlines():
                            _mlist = line.split()[1:]
                            for _str in _mlist:
                                self.word2trainset(_str, _file)

                except IOError:
                    traceback.print_exc()
        except FileNotFoundError:
            traceback.print_exc()
            print('File not found')

        print("complete!")

if __name__ == '__main__':
    A = ReQuQ()
    A.pd2crfsuite()