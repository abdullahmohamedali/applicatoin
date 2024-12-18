from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_op = webdriver.ChromeOptions()
chrome_op.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_op)
for time in event_times_part_2:
    print(time.text)
driver.get("https://www.python.org/")

event_times_part_1 = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_times_part_2 = driver.find_elements(By.CSS_SELECTOR, ".event-widget time .say-no-more")for time in event_times_part_2:
    print(time.text)

for time in event_times_part_2:
    print(time.text)
for time in event_times_part_2:
    print(time.text)



