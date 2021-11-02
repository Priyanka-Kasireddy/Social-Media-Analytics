# fromString="From: Stephanie Rosenthal (Professor from Pennsylvania)"

# def parseName(fromString):
#     for line in fromString.split("\n"):
#         start=line.find(" ")
#         line=line[start:]
#         end=line.find("(")
#         line=line[:end]
#         line=line.strip()
#     return line
# print(parseName(fromString))

# def parsePosition(fromString):
#     for line in fromString.split("\n"):
#         start=line.find("(")+len("(")
#         line=line[start:]
#         end=line.find(" ")
#         line=line[:end].strip()
#     return line
# print(parsePosition(fromString))

# def parseState(fromString):
#     for line in fromString.split("\n"):
#         start=line.find("from")+len("from ")
#         line=line[start:]
#         end=line.find(")")
#         line=line[:end].strip()
#     return line
# print(parseState(fromString))

# message="I am so #excited to watch #TheMandalorian! #starwars"
# def findHashtags(message):
#     for line in message.split("\n"):
#         start=line.find("#")
#         line=line[start:]
#         end=line.find(" ")
#         line=line[:end].strip()
#     return line
# print(findHashtags(message))
# print("#excited", "#TheMandalorian", "#starwars")

# import re 
# x=re.findall("#\w", message)
# print(x)

# endChars = [ " ", "\n", "#", ".", ",", "?", "!", ":", ";", ")" ]
# def findHashtags(message):
    # print(message)
    # lst=[]
    # m=message.split("#")
    # # print(m)
    # for x in m[1:len(m)]:
    #     string=""
    #     print(x)
    #     for y in x:
    #         if y not in endChars:
    #             string+=y
    #             # print(y)
    #         else:
    #             break
    #     string="#"+string
    #     lst.append(string)
    # return lst
# print(findHashtags(message))

def addColumns(data, stateDf):
    names=[]
    positions=[]
    states=[]
    regions=[]
    hashtags=[]
    for index, row in data.iterrows():
        labelvalue=data["label"].loc[index] 
        pN=parseName(labelvalue) 
        pP=parsePosition(labelvalue) 
        pS=parseState(labelvalue) 
        RFS=getRegionFromState(stateDf,state) 
        textvalue=data["text"].loc[index] 
        Htag=findHashtags(textvalue) 
        names.append(pN) 
        positions.append(pP) 
        states.append(pS) 
        regions.append(RFS) 
        hashtags.append(Htag) 
        data["pN"]=names 
        data["pP"]=positions 
        data["pS"]=states 
        data["RFS"]=regions 
        data["Htags"]=hashtags 
    return None

