import searcher
import data_load
import indexer
import weather
#the functions will be called here in order to perform search_engine operations


str_set=data_load.main()
indexer.preprocess(str_set)
print("Please enter the word")
query=input()
while(query!="q"):
    weather.weatherInfo()
    s1=searcher.search(query)
    print("Search Results: ")
    for x in s1:
        print(x[0])
    print("Please enter any word other than 'q' to continue")
    query=input()
#Output1
    
#Please enter the word
#VIP
#weather Conditions :  Rain
#Performing search operation for  {'VIP'}
#Search Results: 
#www.newhaven.edu/admissions/VIP/
#Please enter any word other than 'q' to continue
#admissions and ugrad
#weather Conditions :  Rain
#Performing search operation for  {'admissions', 'ugrad'}
#Search Results: 
#www.newhaven.edu/admissions/ugrad/opportunities/virtual/
#www.newhaven.edu/admissions/ugrad/
#www.newhaven.edu/admissions/ugrad/opportunities/openhouse/
#Please enter any word other than 'q' to continue
#ugrad or VIP
#weather Conditions :  Rain
#Performing search operation for  {'VIP', 'ugrad'}
#Search Results: 
#www.newhaven.edu/admissions/VIP/
#www.newhaven.edu/admissions/ugrad/opportunities/virtual/
#www.newhaven.edu/admissions/ugrad/
#www.newhaven.edu/admissions/ugrad/opportunities/openhouse/
#Please enter any word other than 'q' to continue
#q
#>>> 
