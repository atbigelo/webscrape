import requests
from bs4 import BeautifulSoup
URL = "https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=nissan&maximum_distance=all&mileage_max=&models[]=nissan-gt_r&monthly_payment=&page_size=20&sort=best_match_desc&stock_type=used&year_max=&year_min=&zip=60606"
page = requests.get(URL)
soup = BeautifulSoup(page, 'html.parser')

