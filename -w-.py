# encoding=utf-8
import json
import jieba

class Analysis():
    dataSegment = []
    def NaiveTextSegmentation(self, dataJson):
        mFile = open("Analysis_Segmentation.json", 'w+')
        
        for element in dataJson:
            data = {}
            data["context"] = element["context"]
            
            data["Segmentation"] = list(jieba.cut_for_search(element["context"]))
            #print(data["Segmentation"])
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
    
