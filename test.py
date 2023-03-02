from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
print("chromedriver_binary.chromedriver_filename",chromedriver_binary.chromedriver_filename)

driver = webdriver.Chrome(executable_path=chromedriver_binary.chromedriver_filename)
driver.get("http://www.python.org")
assert "Python" in driver.title