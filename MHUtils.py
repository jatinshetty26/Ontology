from xmindparser import xmind_to_dict
import configparser
from owlready2 import *
import owlready2 as owl

def readProps():
    config = configparser.RawConfigParser()
    config.read('MHConfig.properties')
    return config

def loadOwl(owlPath):
    onto_path.append(owlPath)
    onto = get_ontology(owlPath)
    onto.load()
    return onto

def xmindTodict(fileName):
    return xmind_to_dict(fileName)

def extractFunction(xMindDict):
    functionList = []
    for eachDic in xMindDict:
        for eachSub in (eachDic['topic']['topics']):
            functionList.append(eachSub['title'])
    return functionList