from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.rottentomatoes.com/browse/cf-dvd-streaming-all"
driver.get(url)



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#4
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict

# Set up Chrome WebDriver (you should have chromedriver installed and its path specified)
chrome_driver_path = "https://www.bbc.com/news/technology"
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Navigate to the Technology section of BBC News
url = "https://www.bbc.com/news/technology"
driver.get(url)

# Wait for the page to fully load (you may need to adjust the wait time)
driver.implicitly_wait(5)

# Extract HTML content after it's fully loaded
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract news article titles and publication dates
article_elements = soup.find_all("div", class_="gs-c-promo-body gel-1/2@l gel-1/1@m gel-1/1@xl")
article_data = defaultdict(list)

for article_element in article_elements:
    title = article_element.find("h3", class_="gs-c-promo-heading__title").text.strip()
    date = article_element.find("time")['data-datetime']

    # Categorize articles by their publication month
    month = date.split()[1]  # Assuming the date format is like '1 January 2022'
    article_data[month].append((title, date))

# Print the categorized lists of articles
for month, articles in article_data.items():
    print(f"Articles published in {month}:")
    for article in articles:
        print(f"Title: {article[0]} | Date: {article[1]}")
    print("-" * 40)

#5
from selenium import webdriver
from bs4 import BeautifulSoup
from statistics import mean
from collections import Counter
chrome_driver_path = "https://www.accuweather.com/en/fr/marseille/170960/weather-forecast/170960"
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
city_url = "https://www.accuweather.com/en/fr/marseille/170960/weather-forecast/170960"
driver.get(city_url)
driver.implicitly_wait(5)
html_content = driver.page_source
driver.quit()
soup = BeautifulSoup(html_content, 'html.parser')
temperature_elements = soup.find_all("span", class_="CurrentConditions--tempValue--3KcTQ")
condition_elements = soup.find_all("div", class_="CurrentConditions--phraseValue--2xXSr")
humidity_elements = soup.find_all("div", class_="WeatherDetailsListItem--wxData--23DP5")
temperatures = [int(temp.text) for temp in temperature_elements]
conditions = [condition.text.strip() for condition in condition_elements]
humidity_values = [int(humidity.text.strip().strip('%')) for humidity in humidity_elements]
average_temperature = mean(temperatures)
most_common_condition = Counter(conditions).most_common(1)[0][0]
print(f"Average Temperature: {average_temperature}°F")
print(f"Most Common Weather Condition: {most_common_condition}")
print("-" * 40)
