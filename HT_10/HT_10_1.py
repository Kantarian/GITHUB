 #За допомогою Selenium зайти на сайт ОЛХ, ввести в пошук будь-який запит, дочекатись отримання результатів і зберегти скріншот сторінки.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChrOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

wd = webdriver.Chrome(executable_path ='D:\Python\Geekhub\HT_10\chromedriver.exe')

window_size = {'width': 2600, 'height': 1024}
window_possition = {'x': 0, 'y': 25}
wd.set_window_rect(**window_possition, **window_size)
time = 10
wait = WebDriverWait (wd, time)

wd.get('https://www.olx.ua/')

search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headerSearch")))
search = wd.find_element_by_id("headerSearch")
search.send_keys('Велосипед')
search.send_keys(Keys.RETURN)
wd.save_screenshot('SearchPage.png')


if __name__ == '__main__':
    pass