from bs4 import BeautifulSoup
import requests


#List of urls
article_urls = [
    'https://www.investing.com/analysis/gold-stocks-good-times-could-be-here-already-200647703',
    'https://www.investing.com/analysis/stocks-bounce-oil-dives-whats-next-200647844',
    'https://www.investing.com/analysis/gold-overbought-tempered-geopolitical-fears-rising-yields-could-spook-the-bulls-200647831',
    'https://www.investing.com/analysis/silver-rally-nears-important-breakout-price-resistance-200647810',
    'https://www.investing.com/analysis/gold-silver-will-soar-when-stocks-crash-200647811',
    'https://www.investing.com/analysis/gold-dips-equities-rebound-in-a-week-of-financial-whiplash-200647854',
    'https://www.investing.com/analysis/new-opportunities-emerge-in-commodities-as-wheat-natural-gas-sugar-prices-bottom-200647851',
    'https://www.investing.com/analysis/us-dollar-looks-to-extend-rise-eurusd-aims-for-parity-usdjpy-at-tipping-point-200647833',
    'https://www.investing.com/analysis/us-dollar-looks-to-extend-rise-eurusd-aims-for-parity-usdjpy-at-tipping-point-200647833',
    'https://www.investing.com/analysis/weekly-market-recap-us-dollar-slows-down-a-bit-but-not-bearish-yet-200647827',
    'https://www.investing.com/analysis/gold-drops-on-hawkish-fed-comments-euro-rises-200647830'
    ]

#Function to scrape article content
def scrape_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape the title of the article
        title = soup.find('h1', class_='mb-2 text-xl font-bold md:mb-4 md:text-[42px] md:leading-[60px]').text
        content = soup.find('div', class_='article_WYSIWYG__O0uhw').text
        return {'title': title, 'content': content}
    
    else:
        print(f"Failed to scrape {url}: HTTP {response.status_code}")
        
        
# Itrate over each URL and scrape the article
for url in article_urls:
    article_data = scrape_article(url)
    if article_data:
        print(f"Scraped article '{article_data['title']}'")
        print(f"Content:\n{article_data['content']}\n")
