




import requests                 
from bs4 import BeautifulSoup   # Used for web scraping 
import pandas as pd

df=pd.read_csv('ds.csv')   # IT is the data set csv file take movie list and scrape its rating from the imdb 
movie=list(df['title'])


for i in range(0,30):      # Take 500 movie from all ott platform becuase to search 8000 it takes lot of time in scraping 
    try:
        f=open('disney.csv','a')  # open a csv file where scape data saved suppose from internet it got 6.6/10 then it takes 6.6 along with the ott platform
        
        movie_name=movie[i]
        if(',' in movie_name):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            d=movie_name.replace(',',' ')         # To solve error because comma have some sense in the csv file act as delimeter
            # So to remove the deleimeter with some logic 
            movie_name=d
        else:
            pass
        
        URL = "https://www.google.com/search?q="+movie_name+"rating+imbdb"   #  Web scraping URL 
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")   # Convet it in to the HTML parser 

        g=soup.find_all("span", class_="oqSTJd")   # Try to find a particular div where our magical rating number present 
        #print(g[0])  
        ls=str(g[0]).find('>')   # Try to solve issue releated to string manipulation comes unnder logic setion 

        es=str(g[0]).find('/')
        #print(es)
        rating=float(str(g[0])[ls+1:es])
        print(movie_name+"---------------->   + " ,rating)
        
        string_data=movie_name+","+str(rating)+','+'disney'    # Write data in to the csv file so comma is used here 
        f.write(string_data)
        f.write('\n')    # Used as a line break to further write from the next line 
        f.close()       # Close the file 
    except:                                          # If occuur any network issue program will not crash due to exception handling
        
        try:
            f.close()
        except:

            pass

        try:
            f=open('ds.csv','a')
            string_data=movie_name+","+str('NULL')+','+'disney'
            f.write(string_data)
            f.write('\n')
            f.close()
            
            
        except:

            print("some network issue come")
            try:
                
                f.close()
            except:

                
                print("check file ")


