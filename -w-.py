# !/usr/bin/env python
# encoding=utf-8
import json
import jieba
import jieba.posseg
import jieba.analyse
import traceback


class Analysis:
    _dataSegment = []

    @staticmethod
    def filter(input_iter):
        for token in input_iter:
            if token not in ",.?;'[]()`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“、\"… ":
                yield token

    def naive_text_segmentation(self, data_json):
        _mFile = open("Analysis_Segmentation_test.json", 'w+')
        
        for element in data_json:

            _mdata = dict()
            _mdata["content"] = element["content"]
            try:
                _mdata["Segmentation"] = list(self.filter(jieba.cut(element["content"], cut_all=False)))
            except KeyError:
                traceback.print_exc()
            self._dataSegment.append(_mdata)
            # print(self.dataSegment)
        json_str = json.dumps(self._dataSegment, ensure_ascii=False, indent=2)
        _mFile.write(json_str)
        _mFile.close()


if __name__ == "__main__":    
    with open("data.json", "r") as jsonFile:
        data = jsonFile.read()
        # print(data)
        dataJson = json.loads(data)
        A = Analysis()
        A.naive_text_segmentation(dataJson)
    jsonFile.close()
