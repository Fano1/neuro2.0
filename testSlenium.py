from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
link = r"https://emochi.com/chat?query=%7B%22promptId%22%3A%22dVfc2eV2CrDduXKl8XPbk%22%2C%22title%22%3A%22Akira+%7CZombie+Apocalypse%7C%22%2C%22from%22%3A%22chatted%22%2C%22avatar%22%3A%22https%3A%2F%2Fimage-cdn.flowgpt.com%2Ftrans-images%2F1736439526704-480e702e-55cc-4eca-81ad-7507eef9c1b2.default.webp%22%2C%22isFollowed%22%3Atrue%7D"
# link = r"https://emochi.com/chat?query=%7B%22promptId%22%3A%22dVfc2eV2CrDduXKl8XPbk%22%2C%22title%22%3A%22Akira+%7CZombie+Apocalypse%7C%22%2C%22from%22%3A%22chatted%22%2C%22avatar%22%3A%22https%3A%2F%2Fimage-cdn.flowgpt.com%2Ftrans-images%2F1736439526704-480e702e-55cc-4eca-81ad-7507eef9c1b2.default.webp%22%2C%22isFollowed%22%3Atrue%7D"
driver.get(link)


name = "css-175oi2r"
elem = driver.find_element(By.CLASS_NAME, name)
print(elem.text)