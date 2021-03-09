from selenium import webdriver

PATH = "/PATH_GOES_HERE/chromedriver"
driver = webdriver.Chrome(PATH)

courses = ["AWS Concepts", "Introduction to Cloud Computing", "Hadoop Starter Kit", "Start Kali Linux, Ethical Hacking and Penetration Testing!"]
driver.get("https://udemyfreecourses.org/category/all-it-and-software")

for i in courses:
    link = driver.find_element_by_link_text(i)
    link.click()

