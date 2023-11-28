import requests
from bs4 import BeautifulSoup
url = "https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=nissan&maximum_distance=all&mileage_max=&models[]=nissan-gt_r&monthly_payment=&page_size=20&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip=60606"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
totalqty = soup.find("span", attrs={"class":"total-filter-count"})
blackqty = soup.find("label", attrs={"for":"exterior_colors_black"})
blueqty = soup.find("label", attrs={"for":"exterior_colors_blue"})
grayqty = soup.find("label", attrs={"for":"exterior_colors_gray"})
greenqty = soup.find("label", attrs={"for":"exterior_colors_green"})
orangeqty = soup.find("label", attrs={"for":"exterior_colors_orange"})
redqty = soup.find("label", attrs={"for":"exterior_colors_red"})
silverqty = soup.find("label", attrs={"for":"exterior_colors_silver"})
whiteqty = soup.find("label", attrs={"for":"exterior_colors_white"})
print(totalqty)
print(blackqty)
print(blueqty)
print(grayqty)
print(greenqty)
print(orangeqty)
print(redqty)
print(silverqty)
print(whiteqty)

