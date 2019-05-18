import re
import sys

filename1=sys.argv[1]
filename2=sys.argv[2]
bigList1=[]
bigList2=[]

class myMethod:
    def __init__(self, methodName, listOfOpcodes):  
        self.methodName=methodName
        self.listOfOpcodes=listOfOpcodes

with open(filename1) as f1:
    for line1 in f1:
        word1=line1.split()
        if(len(word1) >= 2):
            llist=[]
            if((word1[0]=="#")&(word1[1]=="{method}")):
                m=myMethod(word1[3], llist)
                #m.methodName=word1[3]
                bigList1.append(m)
                #print(m.listOfOpcodes)
            
            if(word1[0].startswith("0x")):
                m.listOfOpcodes.append(word1[1])
                #print(m.listOfOpcodes)
                

with open(filename2) as f2:
    for line2 in f2:
        word2=line2.split()
        if(len(word2) >= 2):
            llist=[]
            if((word2[0]=="#")&(word2[1]=="{method}")):
                m=myMethod(word2[3], llist)
                #m.methodName=word1[3]
                bigList2.append(m)
                #print(m.listOfOpcodes)
            
            if(word2[0].startswith("0x")):
                m.listOfOpcodes.append(word2[1])
                #print(m.listOfOpcodes)


'''print('PGO OFF methods')
for obj in bigList1:
    print(obj.methodName)
    print(obj.listOfOpcodes)
print('PGO ON methods')
for obj in bigList2:
    print(obj.methodName)
    print(obj.listOfOpcodes)'''

print('PGO OFF, number of method calls:',len(bigList1))
print('PGO ON, number of method calls:', len(bigList2))
count=0
not_matched=0
matched=0
for obj1 in bigList1:
    for obj2 in bigList2:
        if(obj1.methodName == obj2.methodName):
            #print('Matched method', obj1.methodName)
            count+=1
            if(obj1.listOfOpcodes == obj2.listOfOpcodes):
                #print('has same assembly ops')
                matched+=1
            else:
                print(obj2.methodName,'does not have same assembly ops')
                not_matched+=1
    print(obj1.methodName, 'matched', count, 'time(s)')
    count=0
            #break

print('Affected:',not_matched, 'Total:',len(bigList2),'(',(not_matched/len(bigList2))*100,'%)')

added=False
for obj2 in bigList2:
    for obj1 in bigList1:
        if(obj2.methodName==obj1.methodName):
            added=True
            #print('found')
        #else:
            #print('not found')
    if(added==False):
        print('Method', obj2.methodName, 'is an additional method')
