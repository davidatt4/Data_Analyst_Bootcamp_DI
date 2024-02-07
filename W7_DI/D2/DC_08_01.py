from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Web scraping with Selenium and BeautifulSoup
url = 'https://www.bbc.com/weather/293397'

# Set up options to run Chrome in headless mode
options = Options()
options.add_argument('--headless')  # Comment this line if you want to see the browser while scraping

# Initialize the WebDriver with options
driver = webdriver.Chrome(executable_path='/Users/David/.Trash/chromedriver_mac64/chromedriver', options=options)

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

dates = [date.text for date in soup.select('.wr-date__long')]
temperatures = [temp.text for temp in soup.select('.wr-day-temperature__high')]

weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperatures})
driver.quit()

# Data Analysis with Pandas
weather_data['Temperature'] = pd.to_numeric(weather_data['Temperature'].str.extract('(\d+)')[0])

average_temp = weather_data['Temperature'].mean()
total_days = len(weather_data)

# Data Visualization with Seaborn and Matplotlib
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Temperature', data=weather_data)
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.show()

# Document Your Findings
print("Average Temperature:", average_temp)
print("Total Days:", total_days)
