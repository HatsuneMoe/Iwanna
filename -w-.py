# encoding=utf-8
import json
import jieba
import jieba.posseg
import jieba.analyse
import traceback  

class Analysis():
    dataSegment = []

    def Filter(self, input_iter):
        for token in input_iter:
            if token not in ",.?;'[]()`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“、\"… ":
                yield token
        
    def NaiveTextSegmentation(self, dataJson):
        mFile = open("Analysis_Segmentation_test.json", 'w+')
        
        for element in dataJson:
            data = {}
            data["content"] = element["content"]
            try:
                data["Segmentation"] = list(self.Filter(jieba.cut(element["content"], cut_all=False)))
            except:
                traceback.print_exc()
            self.dataSegment.append(data)
            #print(self.dataSegment)
        jsonStr = json.dumps(self.dataSegment, ensure_ascii = False, indent=2)
        mFile.write(jsonStr)
        mFile.close()
    

if __name__ == "__main__":    
    with open("絮絮雨.json", "r") as jsonFile:
        data = jsonFile.read()
        #print(data)
        dataJson = json.loads(data)
        A = Analysis()
        A.NaiveTextSegmentation(dataJson)

    jsonFile.close()
    
