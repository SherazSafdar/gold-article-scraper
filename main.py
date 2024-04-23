from bs4 import BeautifulSoup
import requests

url = 'https://www.investing.com/analysis/gold-stocks-good-times-could-be-here-already-200647703'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the title of the article
title = soup.find('h1', class_='mb-2 text-xl font-bold md:mb-4 md:text-[42px] md:leading-[60px]')
article_title = title.text.strip()
print("Article Title:", article_title)

# Scrape the text content enclosed within the <em> tags
em_element = soup.find('em')
em_text = em_element.get_text(strip=True)
print("Text content enclosed within <em> tags:", em_text)


# Scrape the text content within the <div> element with class 'article_WYSIWYG__O0uhw'
div_element = soup.find('div', class_='article_WYSIWYG__O0uhw')
div_text = div_element.get_text(strip=True)
print("Text content within <div> element with class 'article_WYSIWYG__O0uhw':", div_text)