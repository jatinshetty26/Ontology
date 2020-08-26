import MHUtils

# Read and load Properties
config = MHUtils.readProps()
onto = MHUtils.loadOwl((config.get('Protege', 'protege.owlPath')))

# Convert xMind file to dict
xMindDict = MHUtils.xmindTodict((config.get('XmindFile', 'xmind.filelocation')))

# Extract Functions
xMind_Func_List = MHUtils.extractFunction(xMindDict)
print("Level One Functions are {} ".format(xMind_Func_List))

# for eachfunc in xMind_Func_List:
#     getParts(eachfunc)

