from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

s=Service('C:/Users/Yagiz/ChromeDriver/chromedriver.exe')## You should download chromedriver and you should copy where it is.
driver = webdriver.Chrome(service=s)
url = "https://www.n11.com/urun/rush-ace-rhx55-71-surround-titresimli-rgb-oyuncu-gaming-kulakligi-1605943?magaza=rush"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(driver.page_source, "html.parser")
## Now we have html parser and we create a list to collect all reviews
reviewlist = []
## We have all information we need inside this li class = comment
reviews = soup.find_all("li", {"class": "comment"})

for rev in reviews:
    ## We turned this into a string and then made string opearations to get only the float rating.
    rating_str = str(rev.find("div", {"class": "ratingCont"}))
    rating_str = rating_str.split()[4].replace("\"></span>", " ")
    rating_str = rating_str.replace("r", " ")

    review = {
        ## We collect all attributes of reviews into a dictionary for each element in reviews.
        "product": soup.title.text.replace("Fiyatları ve Özellikleri", "").strip(),
        "rating": float(rating_str),
        "body": rev.find("p").text.strip(),
    }
    ## We add this dictionaries into our list.
    reviewlist.append(review)

##Creating xlsx file with our data
df = pd.DataFrame(reviewlist)
df.to_excel("rush-ace-rhx55-71-reviews.xlsx", index=False)



