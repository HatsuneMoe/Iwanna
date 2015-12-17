#-*- coding: utf-8 -*-
from nltk import *
import json

if __name__ == "__main__":
    Text = []
    with open("Analysis_Segmentation_test.json", "r") as jsonFile:
        data = jsonFile.read()
        dataJson = json.loads(data)
    for element in dataJson:
        #print(element["content"] + "\n")
        Text.extend(element["Segmentation"])
    fdist1 = FreqDist(Text)
    fdist1.plot(50, cumulative = True)
    #vocabulary1 = fdist1.keys()
    #print(vocabulary1)
    #print(fdist1["喵"])
    jsonFile.close()      
