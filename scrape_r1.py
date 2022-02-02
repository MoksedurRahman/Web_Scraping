import requests
from bs4 import BeautifulSoup
#pip install lxml

# Read THe Page
res = requests.get(r'https://www.tournymeyer.fr/offre/local-dactivites-5796m2-divisible-328-m2-minimum/')
page = BeautifulSoup(res.content,'lxml')

#First Part
for strong_tag in page.find_all('div', classs='price'):
    print(strong_tag.text)

# Second Part
for h2_content in page.find_all('h2', class_="equipment"):
    print(h2_content.text)

#Third Part
# Get All Content inside h2 Tag
h2_tag = page.find_all("h2", class_="equipment")
for ul_values in h2_tag:
    ul_sib= ul_values.find_next_siblings('ul')
    
    list =list(ul_sib)
    lis = []
    for ul in list:
        for li in ul.findAll('li'):
            if li.find('ul'):
                break
            lis.append(li)
   # print(lis)
    for lii in lis:
       print(lii.text)
       
    #print(ul_sib) #Équipements
    
    # Get all values after br tag
    for br_text in ul_values.find_next_siblings(text=True):
        print(br_text.strip())