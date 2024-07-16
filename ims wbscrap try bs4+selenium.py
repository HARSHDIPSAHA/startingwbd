import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
#from ironpdf import *

# URL of the page to be scraped
url = "https://www.imsnsit.org/imsnsit/notifications.php"

# Create a selenium webdriver instance
driver = webdriver.Chrome()  # or Firefox, etc.

# Visit the website
driver.get(url)


soup = BeautifulSoup(driver.page_source, "html.parser")
first_pdf_link = None
links=soup.find_all('a', href=True)

first_pdf_link = links[2]["href"]
# Find the link that requires a click to open
link = first_pdf_link

# Click on the link using selenium
driver.find_element(By.LINK_TEXT, link).click()

# Get the new page content after clicking the link
new_page_content = driver.page_source
print(new_page_content)
# Parse the new page content using BeautifulSoup

# Close the selenium webdriver instance
driver.quit()
