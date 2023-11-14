from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to your application
driver.get("http://localhost")  # Adjust URL as needed

# Perform actions (e.g., filling out forms, clicking buttons)
search_box = driver.find_element_by_name("search")
search_box.send_keys("test query")
search_box.send_keys(Keys.RETURN)

# Assertions to validate the results
assert "Search Term: test query" in driver.page_source

# Close the browser
driver.quit()
