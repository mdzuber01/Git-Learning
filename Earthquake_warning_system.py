import pandas as pd 
import playsound as ps 
import time as t
#from pathlib import Path
#import vlc
a=4;secondpassed=3
#while(a<5):
df=pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv')#read csv file of EQ record
reqDF=df[['place','mag'][0:10:1]] # here we take only two column from the entire 22 columns named place and magnitude



ads=reqDF.describe()#This will find stastical value (i.e. mean,max,minetc) of numeric data.
#print(ads)

#print(pd.DataFrame(reqDF.head(9)))#This will take top 9 row. 
countrycontains=reqDF.place.str.contains('Alaska')#here we want to extract the place, named alaska.
#print(countrycontains)
dfofcountry=reqDF[countrycontains]#here we take the true-value of countrycontains(i.e Alaska named cell only) from reqDF
#print(dfofcountry)
#dfofSEQ=dfofcountry['mag']>4
#print(dfofSEQ)
def eqsiren (m):
        #enter threshold magnitude
    dfofSEQ=dfofcountry[dfofcountry['mag']>m]
    #for index,rows in dfofSEQ.iterrows(): #This will print dfofSEQ data one by one in rows wise.
        #print(index,rows)
    #print(dfofSEQ)
    rowsindfofSEQ=dfofSEQ.shape[0]
    print(f"\n  Earthquake occur in {rowsindfofSEQ} places in the last hour, updated every minutes and the place and magnitude of occurance is \n{dfofSEQ[['place','mag']]}\n")
    if(rowsindfofSEQ>0):
            
        print(f" i.e play siren for EARTHQUAKE warning for earthquake magitude greater than {m}\n")
        #audio=Path().cwd() / "siren_mp3.mp3"
        #audio_file=os.path.dirname(__file__) + '\siren_mp3.mp3'
        #ps(audio_file)
        #ps.playsound('siren_mp3')
        #media = vlc.MediaPlayer('C:/Users/ashra/OneDrive/Desktop/Python_Learning/siren_mp3.mp3')
        #media.play()
    else:
        print("no earthquake occurs in last hour in Alaska") 
    print(f'Monitoring for {secondpassed} sec.\n please press ctrl+c to stop')
    t.sleep(3) 
secondpassed=secondpassed+3
eqsiren(4)        
