import itertools

def findmint(k,mterms):
    l=[]
    p=[]
    st=""
    for j in range(len(mterms)):
        l=[]
        for i in range(len(k)):
            if k[i]=='2':
                st=st+mterms[j][i]
            elif ((mterms[j][i]=='0' and k[i]=='0') ):
                st=st+'0'
            elif ((mterms[j][i]=='1' and k[i]=='1')):
                st=st+'1'

            l.append(st)
    
            st=""
        if '' in l:
            pass
        else:
            p.append(''.join(l))
    return p
                
                    
                
            
def ifempty(T):
    if len(T)==0:
        return True
    else:
        flag=0
        for i in T:
            if i:
                flag+=1
        if flag==0:
            return True
    return False
def compare(str1,str2):
    count = 0
    pos = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count+=1
            pos = i
    if count == 1:
        return True, pos
    else:
        return False, None

    
def combinePairs(T, unticked):
    l = len(T) -1
    ticked = []
    next_group = [[] for x in range(l)]

    for i in range(l):
        for elem1 in T[i]:
            for elem2 in T[i+1]:
                b, pos = compare(elem1, elem2)
                if b == True:
                    #append the ones used in check list
                    ticked.append(elem1)
                    ticked.append(elem2)
                    #replace the different bit with '2'
                    new_elem = list(elem1)
                    new_elem[pos] = '2'
                    new_elem = "".join(new_elem)
                    next_group[i].append(new_elem)
    for i in T:
        for j in i:
            if j not in ticked:
                unticked.append(j)

    return next_group, unticked

def compBinarySame(term,number):
    for i in range(len(term)):
        if term[i] != '2':
            if term[i] != number[i]:
                return False

    return True

def binary_to_letter(s):
    out = ''
    c = 'a'
    more = False
    n = 0
    for i in range(len(s)):
        #if it is a range a-zA-Z
        if more == False:
            if s[i] == '1':
                out = out + c
            elif s[i] == '0':
                out = out + c+'\''

        if more == True:
            if s[i] == '1':
                out = out + c + str(n)
            elif s[i] == '0':
                out = out + c + str(n) + '\''
            n+=1
        #conditions for next operations
        if c=='z' and more == False:
            c = 'A'
        elif c=='Z':
            c = 'a'
            more = True

        elif more == False:
            c = chr(ord(c)+1)
    return out


#remove redundant lists in 2d list
def remove_redundant(T):
         
    new_group = []
    for j in T:
        new=[]
        for i in j:
            if i not in new:
                new.append(i)
        new_group.append(new)
    return new_group



#ACCEPTING terms
n=int(raw_input("Enter the number of variables in the minterm expression : "))
terms = raw_input("Enter the terms  : ").split()
terms= map(int, terms)
dec=terms

#make a T list
T=[[] for x in range(n+1)]

for i in range(len(terms)):

    terms[i] = bin(terms[i])[2:] #Slicing the string by [2:] since in-built bin() function returns 0b<binary_value> 
    mterms=terms
    if len(terms[i]) < n:
        for j in range(n - len(terms[i])):
             terms[i] = '0'+ terms[i]  #to add zeroes to fill empty bit spaces in the front
    onecount = terms[i].count('1')
    T[onecount].append(terms[i])  #creating table T0
all_group=[]
unticked = []
    #combine the pairs in series until nothing new can be combined
while ifempty(T) == False:
    all_group.append(T)
    next_group, unticked = combinePairs(T,unticked)
    T = remove_redundant(next_group)
print("Prime Cubes")
s=""
for i in unticked:
    s= s+ binary_to_letter(i) + " + "
print s[:(len(s)-3)]
#print unticked


dict1={} ###
for i in range(len(unticked)):
    dict1[unticked[i]]=findmint(unticked[i],mterms)
#print dict1
dict2=dict1
essp=dict1.values()
finalessp1=[]
finalessp2=[]
flat_list = [item for sublist in essp for item in sublist]
for i in flat_list:
    if flat_list.count(i)==1:
        finalessp1.append(i)
for i in finalessp1:
    for exp, li in dict1.iteritems():
        if i in li:
            finalessp2.append(exp)
finalessp2=list(set(finalessp2)) #to remove multiple occurences
for i in finalessp2:
    del dict2[i]
#print dict2
last=[]
d2val=dict2.values()
flat_list2 = [item for sublist in d2val for item in sublist]
#print flat_list2
m=[]
for i in flat_list2:
    if flat_list2.count(i)>1:
        last.append(i)
for g in dict2:
    if set(dict2[g])==set(last):
        #print dict2[g]
        for ke,va in dict2.iteritems():
            if dict2[g] == va:
                m.append(ke)
#print m


print("Selective prime cubes")
s=""
for i in m:
    s= s+ binary_to_letter(i) + " + "

print s[:-2] #[:(len(s)-3)]
        
        
#print finalessp2

print("Essential prime cubes")
s1=""
for i in finalessp2:
    s1=s1+binary_to_letter(i)+"+"
print s1[:-1] #[:(len(s)-3)]
new=""
print("Minimised expression : ")
new=s1+s
new=new[:-2]
print new



            

