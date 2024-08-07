from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")


# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Wait for the page to load
    time.sleep(2)

    # Find the search bar and input search query
    search_box = driver.find_element(By.NAME, "search_query")
    search_query = "Python Selenium tutorial"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(3)

    # Click on the first video result
    first_video = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
    first_video.click()

    # Wait for the video to load and play for a few seconds
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()


