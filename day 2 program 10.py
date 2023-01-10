sent1=input("enter the sent1: ")
sent2=input("enter the sent2: ")
def commonwords(sent1,sent2):
    sent1=set(sent1)
    sent2=set(sent2)
    common=list(sent1.intersection(sent2))
    return common
def removecommonwords(sent1,sent2):
    sent1=list(sent1.split())
    sent2=list(sent2.split())
    commonlist=commonwords(sent1,sent2)
    word=0
    for i in range(len(sent1)):
        if sent1[word]in commonlist:
            sent1.pop(word)
            word=word-1
        word+=1
    word=0
    for i in range(len(sent2)):
        if sent2[word]in commonlist:
            sent2.pop(word)
            word=word-1
        word+=1
    print(*sent1)
    print(*sent2)
commonwords(sent1,sent2)
