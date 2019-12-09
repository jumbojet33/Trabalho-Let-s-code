# projeto:
# fazer webscraping de ROE (yahoo finance)
#Dividend (dividend.com)
#Last closing price (yahoo finance)
#Beta (yahoo finance)
#P\e (yahoo finance)
#net worth (yahoo finance)
from bs4 import BeautifulSoup
import requests
import time


Perfil1 = input("In a scale from 1-10, how would you say you deal with risk? One being I am literally scared of everything and 10 means you eat fear: ")

if Perfil1 > "6":
	print("Risk it is")
else:
	print("Lets take is slow")

Perfil2 = input("Do you have any preference in market/index?(Y/N)")

if Perfil2 == "Y":
	input("Select One:")
else:
	print("Lets go")







empresa = input("nome da empresa:")
url1 = f"https://finance.yahoo.com/quote/{empresa}?p={empresa}&.tsrc="
r = requests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
last = soup.find("td",{"data-test":"PREV_CLOSE-value"})
opn = soup.find("td",{"data-test":"OPEN-value"})
PE = soup.find("td",{"data-test":"PE_RATIO-value"})
beta = soup.find("td",{"data-test":"BETA_3Y-value"})
div = soup.find("td",{"data-test":"DIVIDEND_AND_YIELD-value"})
print(f"forward dividend & yield =  {div.text}")
print(f"previous close           =  {last.text}")
print(f"price earnings           =  {PE.text}")
print(f"beta                     =  {beta.text}")	
print(f"open                     =  {opn.text}")
#dontpad (link=sublimelc)
#adicionar os mesmos critérios do S&P por setor, adicionar lista de empresas separadas por setor, comparar a empresa em questão
#com resto do S&P e lista.


#defining o portifolio


Index = ("S&P500, NASDAQ, DOW30, RUSSEL2000")


print("Give us a moment to analyse...")
print()
time.sleep(2)


if float(beta.text) > 1:
	print("Your stock is High Volatile")
else:
	print("Your stock is stable")

time.sleep(3)
print()

if float(PE.text) > 25:
	print("Your stock has a favourable Price to Earnings Ratio")
else:
	print("Your Stock has a low/medium Price to Earnings Ratio")


time.sleep(3)
print()

if float(div.text) > 1:
	print("Your stock has a good dividend yield")
else:
	print("Your stock has a low dividend yield")




#HIGHRISK = (High Beta, Low PE, Average - Low Divdend)
#LOWRISKS = (Low Beta, High PE, High Dividend)
