#Telephone book database of N clients by using hash table
#By making use of two collision handaling techniques and compare them

import array as arr

def acceptData(n):
    l1=[]
    while(len(l1)<n):
        t=(input("Enter telephone nos of client:"))
        #print(n)
        if(len(t)==10)and(t.isdigit()):
            l1.append(t)
        else:
            print("\nvaild telephone no:")
    return(l1)

#example of linear probing
#n=int(input("Enter nos of clients:"))
#l1=acceptData(n)
l1=[1234567890, 1234567891, 1234567892, 1234567885, 1234567887,1234567871,1234567876, 1234567877, 1234567899, 1234567898]
def linearProbing(l1):
    n=len(l1)
    t1=[]
    for i in range(0,n):
        t1.append(0)
    coll=0
    ht=arr.array('i',t1)
    for i in l1:
        t=i%n
        coll=1
        if(ht[t]==0):
            ht[t]=i
            print('inserted key:',i,' at:',t, "with complexity:","O(",str(coll),")")
            coll=0
        else:
            #print(ht)
            print("Collision at index: ",t, " for ", i)
            print("Use probing:")
            #coll=0
            cnt=t
            while(1):
                cnt=(cnt+1)%n
                if(cnt==t):
                    print("Collision cannot be resolved or overflow")
                    break
                else:
                    if(ht[cnt]==0):
                        ht[cnt]=i
                        print('inserted key:',i,' at:',cnt, "with complexity:","O(",str(coll+1),")")
                        coll=0
                        break 
                    else:
                        coll+=1
    return(ht)
ht=linearProbing(l1)

#ht is a lookup table 
print(ht)

def search(key,ht):
    print("_"*60)
    print("Linear Probing:")
    coll=1
    n=len(ht)
    #print(n)
    t=key%n
    if(ht[t]==key):
        print("_"*60)
        print("Telephone no found at",t,"Complexity: O(1)"," key:",key)
        
    else:
        print("Search Using Linear Probing")
        coll=1
        cnt=t
        while(1):
            cnt=(cnt+1)%n
            if(cnt==t):
                print("_"*60)
                print("Telephone nos not found:",key)
                print("Telephone not found Complexity:O(",str(coll+1),") key:",key)
                break
            else:
                if(ht[cnt]==key):
                    print("_"*60)
                    print("Telephone no found at",cnt,"Complexity:O(",str(coll+1),") key:",key)
                    break
                else:
                    coll+=1
            
        
        
    
search(1234567891,ht)
search(1234567871,ht)
search(1234567870,ht)

#OUTPUT
inserted key: 1234567890  at: 0 with complexity: O( 1 )
inserted key: 1234567891  at: 1 with complexity: O( 1 )
inserted key: 1234567892  at: 2 with complexity: O( 1 )
inserted key: 1234567885  at: 5 with complexity: O( 1 )
inserted key: 1234567887  at: 7 with complexity: O( 1 )
Collision at index:  1  for  1234567871
Use probing:
inserted key: 1234567871  at: 3 with complexity: O( 3 )
inserted key: 1234567876  at: 6 with complexity: O( 1 )
Collision at index:  7  for  1234567877
Use probing:
inserted key: 1234567877  at: 8 with complexity: O( 2 )
inserted key: 1234567899  at: 9 with complexity: O( 1 )
Collision at index:  8  for  1234567898
Use probing:
inserted key: 1234567898  at: 4 with complexity: O( 7 )
array('i', [1234567890, 1234567891, 1234567892, 1234567871, 1234567898, 1234567885, 1234567876, 1234567887, 1234567877, 1234567899])
____________________________________________________________
Linear Probing:
____________________________________________________________
Telephone no found at 1 Complexity: O(1)  key: 1234567891
____________________________________________________________
Linear Probing:
Search Using Linear Probing
____________________________________________________________
Telephone no found at 3 Complexity:O( 3 ) key: 1234567871
____________________________________________________________
Linear Probing:





