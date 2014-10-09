import pickle
import os
import fnmatch


#search for the word input by the user
def search(query):
    f=open("web_content",'br')
    dict1={}
    s1=[]
    
    #Retrieves the data from file and place the data to dictionary
    dict1=pickle.load(f)  
    f.close()
    cond=2
    
        
    #print("Please enter word")
    #query=input()
    s=set()
    s=set(query.split(' '))
    
    s1=[]
    if ("or" in s) and (cond!=1):
        s.remove("or")
        cond=0
    if "and" in s:
        s.remove("and")
        cond=1
    print("Performing search operation for ",s)
    #Searches for a word in the dictionary
    s2=[]
    for word in s:
        if(word in dict1.keys()) and ((cond==0)or (cond==2)):
                s_list=dict1[word]
                for x in s_list:
                    if(x[0] not in s1):
                        s1.append(x)
        if(word in dict1.keys()) and (cond==1):
            if(len(s2)!=0):
                 
                 
                 for x in dict1[word]:
                     for y in s2:
                         for z in y:
                            
                             if(z[0]==x[0]):
                                
                                 s1.append(x)
                             
            else:
                s2.append(dict1[word])

    return s1 
    
  




