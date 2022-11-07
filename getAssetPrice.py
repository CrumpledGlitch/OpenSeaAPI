import requests
from bs4 import BeautifulSoup

contract="0x209e639a0ec166ac7a1a4ba41968fa967db30221"
assetNo= "1231"
network = "ethereum"
url = f"https://opensea.io/assets/{network}/{contract}/{assetNo}"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(url, headers=agent)
soup = BeautifulSoup(page.content, 'html.parser')


body = soup.body.main
content = body.decode()
priceString=content.find("Price--amount")
if (priceString==-1):
    print("Not found")
else:
    endAmount=content.find("<!",priceString+15)
    startAmount=content.find('">',priceString+15)
    print(content[startAmount+2:endAmount])






