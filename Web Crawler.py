#!/usr/bin/env python
# coding: utf-8

# # Instructions on execution
# Step 1 — Install and Imports
# Install packages
# Access WebDriver

# #Chrome WebDriver
# The Selenium API (described above) requires the WebDriver protocol to control a web browser, like Chrome, Firefox, or Safari. WebDriver provides a platform and language-neutral wire protocol as a way for out-of-process programs to instruct the behavior of web browsers remotely. 
# I utilized the Chrome WebDriver since Chrome is one of the most popular browsers around. link to download
# https://chromedriver.chromium.org/downloads
# 
# Chrome environamt 
# Supports Chrome version 99
# ChromeDriver 99.0.4844.51

# In[24]:


#pip install requests
#pip install beautifulsoup4
#pip install selenium
#pip install pandas


# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#pandas
import pandas as pd
import time

import requests

#BeautifulSoup

from bs4 import BeautifulSoup
import requests


# In[2]:


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


# # Access Website Via Python
# ## url - web url

# In[3]:


driver = webdriver.Chrome('C:/Users/gowth/Downloads/company project/se/chromedriver_win32/chromedriver.exe')
url = 'https://siccode.com/search-business/sic:3612'
driver.get(url)


# # Information  Scraping
# ## Extracting full xpath for each company title and  href 

# In[4]:


li_list=[]
div_part1='/html/body/div[1]/section/div/div/div['
div_part2=']/ul/li[1]/a'
for i in range(1,21,2):
    div=div_part1+str(i)+div_part2
    li_part1=div[:-4]
    li_part2=div[-3:]
    for j in range(1,11):
        li=li_part1+str(j)+li_part2 
        link=driver.find_element_by_xpath(li).get_attribute('href')
        li_list.append(link)
        
print(li_list)             
     




# Crating list for each variable

# In[5]:


BName=[]
cat=[]
scode=[]
sicdes=[]
ncode = [] 
naicsdes = []
city_list = []
state_list =[]
zipcode_list = []
rev =[]
CompSize=[]




# In[26]:


#Scraping required variabels  


# In[6]:


sleeptime=2
for l in li_list:
    try:
        driver.get(l)
        BusinessName =  driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/h1").text
        BName.append(BusinessName)

        category = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/p/span[1]").text
        cat.append(category)

        siccode = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[2]/div[2]/div/div/a[1]/span").text
        scode.append(siccode)

        sicdescription = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[2]/div[2]/div/div/a[1]").text
        sicdes.append(sicdescription)

        naicscode = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[2]/div[2]/div/div/a[2]/span").text
        ncode.append(naicscode)


        naicsdescription = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[2]/div[2]/div/div/a[2]").text
        naicsdes.append(naicsdescription)

        city = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[3]/div[2]/div[1]/span[2]").text
        city_list.append(city)

        state = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[3]/div[2]/div[3]/span[2]").text
        state_list.append(state)

        zipcode = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[3]/div[2]/div[5]/span[2]").text
        zipcode_list.append(zipcode)

        revenue = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[3]/div[3]/div[1]/span[2]").text
        rev.append(revenue)

        CompanySize = driver.find_element_by_xpath("/html/body/div[1]/div/section[2]/div/div/div[3]/div[3]/div[3]/span[2]").text
        CompSize.append(CompanySize)
        
       

  
        
    except:
        print("not loading")
        continue

    


# ## Data cleaning
# category - Upper case for each word <br>
# SICCode - extracted only code( number)<br>
# SICDescription - spliting and removing SIC Code<br>
# NAICS Code - extracted only code( number)<br>
# NAICSDescription - spliting and removing NAICS Code<br>
# Revenue - Replacing Medium with '$' symbols<br>
# CompanySize - Space trimming<br>
# 
# 

# In[7]:


import string
category=[]
for c in cat:
    c=string.capwords(c)
    #c=c.capitalize()
    category.append(c)
print(category)


# In[8]:


SICCode=[]
for s in sicdes:
    sc=s.split(" ")[2]
    SICCode.append(sc)
print(SICCode)


# In[9]:


SICDescription=[]
for s in sicdes:
    sd=s.split("- ")[1]
    SICDescription.append(sd)
print(SICDescription)


# In[11]:


NAICSCode=[]
for n in ncode:
    nc=n.split(" ")[2]
    NAICSCode.append(nc)
print(NAICSCode)


# In[14]:


NAICSDescription=[]
for n in naicsdes:
    nd=n.split("- ")[1]
    NAICSDescription.append(nd)
print(NAICSDescription)


# In[17]:


Revenue=[]
for r in rev:
    x = r.replace("  Medium", "$$")
    Revenue.append(x)
print(Revenue)


# In[19]:


CompanySize=[]
for c in CompSize:
    c=c.strip()
    CompanySize.append(c)
print(CompanySize)


# ## Exporting Data set
# 
# ### Dataset  contain only 100 rows
# 
# ### File Formate : CSV
# 

# Headers Used
# BName,category, SICCode, SICDescription, NAICSCode, NAICSDescription, city_list, state_list, zipcode_list, Revenue, CompanySize
# Pands is used to export data

# In[20]:


data_tuples = list(zip(BName,category, SICCode,
                       SICDescription, NAICSCode, NAICSDescription, 
                       city_list, state_list, zipcode_list, Revenue, CompanySize))


# ### Renaming Headers 
# Business Name, Category, SIC Code, SIC description, NAICS Code, NAICS description, City, State, Zip Code, 
# Est. Annual Revenue, Est. Company Size

# In[21]:


fin_df=pd.DataFrame(data_tuples, columns=["Business Name","Category","SIC Code","SIC description",
                                          "NAICS Code","NAICS description","City","State","Zip Code",
                                          "Est. Annual Revenue","Est. Company Size"])


# In[22]:


fin_df


# In[27]:


fin_df.to_csv("Final_Dataset.csv", index=False)


# In[ ]:




