from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

from time import sleep
# chrom = webdriver.ChromeOptions()
# chrom.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get("https://www.monster.be/nl/")

sleep(3)

cookies = driver.find_element(By.ID,"onetrust-accept-btn-handler")
cookies.click()

sleep(3)

job_search = driver.find_element(By.ID,"horizontal-input-one-undefined")
job_search.click()
job_search.send_keys("java")
sleep(3)


job_location = driver.find_element(By.ID,"horizontal-input-two-undefined")
job_location.click()
job_location.send_keys("remote")

# button = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/section[1]/div/div/div/div[1]/div/span/div/div/div[1]/form/div/button[2]")
button = driver.find_element(By.XPATH,"//button[@data-testid='searchbar-submit-button-desktop']")

button.click()
sleep(5)


job_list = driver.find_elements(By.XPATH,"//li[@class='sc-blKGMR etPslv']")
print(len(job_list))
for jobs in job_list:
    try:
        job_title = jobs.find_element(By.TAG_NAME,'a').text
        print(job_title)
    except BaseException as e:
        print("Not Enough")