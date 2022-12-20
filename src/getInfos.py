# Carregar Libs
import os
import sys
#absolute_path = os.path.abspath(__file__+"/../Lib/site-packages")
#sys.path.insert(0, absolute_path)

import requests
from bs4 import BeautifulSoup
import csv

# VARIAVEIS
dataF=[]
count=0

# INPUT TXT
try:
    with open('urls.txt') as f:
        urls = f.readlines()
except:
    input("Problema com arquivo urls.txt, favor verificar\n Clique enter para sair")

for i in range(len(urls)):
    urls[i]=urls[i].replace('\n','').replace(',','')

# GET INFOS
burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Connection": "close"}

for url in urls:
    try:
        r=requests.get(url, headers=burp0_headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        nome=soup.find(id='titulo-produto').get_text().replace(',','')
        #preco1=soup.find(class_='risco-produto risco-produto-mob').get_text()[3:].replace(' ','')
        preco2=soup.find(class_='desconto-produto desconto-produto-mob').get_text().replace('\n','').replace('\t','').replace('.','').replace(',','.').replace(' ','')
        nome=nome+" por "+preco2
        data=[nome,url]#,preco2]
        dataF.append(data)
        count+=1
        print(count,len(urls),sep="/")
    except:
        print("URL",count+1,"inválida")
        count+=1
#DEBUG
#print(dataF)

# OUTPUT CSV
header = ['Nome', 'Link']

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(dataF)

a=input("Finalizado, arquivo output.csv gerado\n Clique enter para sair")
