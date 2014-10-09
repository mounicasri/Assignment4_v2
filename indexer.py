import pickle
import data_load
#Preprocess the data
def preprocess(str_set):
    
    f=open("web_content",'br')
    dict1={}
    dict2={}
    dict1=pickle.load(f)
    f.close()
    for word in str_set:
        s1=[]
        for key,value in dict1.items():
                if(word in key):
                        s1.append([key,value])
        dict2[word]=s1
    
    f=open("web_content",'wb')
    pickle.dump(dict2,f)
    f.close()

    
        
       
      
               




