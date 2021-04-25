#!/usr/bin/env python
# coding: utf-8

# In[167]:


import json
import requests
import math


# In[168]:


url = "https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json"
r = requests.get(url)
dataset = r.json()


# In[169]:


topPopulation = []
for country in dataset:
    if country['population']>=847000:
        topPopulation.append(country)


# In[170]:


print(len(topPopulation))
def myFunc(e):
    return e['population']
# topPopulation.sort(reverse=True, key=myFunc)
requiredList = topPopulation[0:20]


# In[171]:


R = 6371; 
totalDistance = 0
for country in requiredList:
    if requiredList.index(country) <len(requiredList) -1:    
        
        for otherCountry in requiredList[requiredList.index(country)+1:len(requiredList)]:
            if 'latlng' in country:
                lat1 = (country['latlng'][0])
                lon1 =  (country['latlng'][1])
            else:
                lat1 =  (0.000)
                lon1 =  (0.000)
            if 'latlng' in otherCountry:
                lat2 =  (otherCountry['latlng'][0])
                lon2 =  (otherCountry['latlng'][1])
            else:
                lat2 =(0.000)
                lon2 = (0.000)
            φ1 = lat1 * math.pi/180; 
            φ2 = lat2 * math.pi/180;
            Δφ = (lat2-lat1) * math.pi/180;
            Δλ = (lon2-lon1) * math.pi/180;

            a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2);
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

            d = R * c; 
            totalDistance = round(totalDistance,2)+round(d,2)


# In[172]:


print(round(totalDistance,2))


# In[ ]:





# In[ ]:





# In[ ]:




