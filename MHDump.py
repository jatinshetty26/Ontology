from xmindparser import xmind_to_dict
import configparser
from owlready2 import *
import MHUtils


# def createOntStructure(eachOne):
#     with onto:
#         class eachOne(Thing):
#             pass



# Read and load Properties
config = MHUtils.readProps()
onto = MHUtils.loadOwl((config.get('Protege', 'protege.owlPath')))


print('Onto : ',onto)
listThis = ['BodyFunction', 'MindFunction', 'PhysicalFunction']



# songClasses = []
# for name in listThis:
#     with onto:
#         type(name, (), {})(Thing)

class Song(Thing):
    def __init__(self, name):
        self.name = name

songs = []
for name in listThis:
    with onto:
        Song(name)

onto.save()

print('END')