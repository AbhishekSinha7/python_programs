from selenium import webdriver

path = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)


driver.get("https://esports.battlegroundsmobileindia.com/teamvote")

driver.find_element_by_xpath(
    '//*[@id="quick-poll-n3"]/div[2]/div[2]').click()
