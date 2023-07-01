from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# send keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# BS4
from bs4 import BeautifulSoup
# Json & Pandas}
import json
import pandas as pd
# Timeout
import time


# Browser Profil
username = "Rex"
profil = "Profile 1"


class TargetLink:
    def __init__(self, param_url, param_timeout):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument(f"user-data-dir=C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
        options.add_argument(f"--profile-directory={profil}")
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)
        self.url = param_url
        self.timeout = param_timeout

    def start(self):
        driver = self.browser
        driver.set_window_size(600, 800)
        try:
            driver.get(self.url)
        except:
            pass

        # Timeout
        wait = WebDriverWait(driver, self.timeout)

        '''
        Search element with Selenium
        '''
        # try:
        #     wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Instagram']")))
        # except ValueError:
        #     print(ValueError)
        #     driver.quit()

        '''
        Get page source and use BS4 for Scraping
        '''
        # source = driver.page_source
        # soup = BeautifulSoup(source, 'html.parser')
        # header = soup.find('header', '')

        '''
        Scroll down page
        '''
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)

        '''
        Click Element with javascript
        '''
        # button = driver.find_element(By.XPATH, "")
        # driver.execute_script("arguments[0].click();", button)
        # time.sleep(2)

        '''
        Result Scraping
        '''
        # Json Result
        # with open('../result/post/detailed_post.json', 'w+') as json_data:
        #     json.dump(param_data, json_data)
        #     print('detailed_post.json Created')
        #

        # Excel Result
        # df = pd.DataFrame(param_data)
        # df.to_excel('../result/post/detailed_post.xlsx', index=False)
        # print('detailed_post.xlsx Created')

        print('Finished')


if __name__ == '__main__':
    #  Parameter
    url = "https://google.com"
    timeout = 50

    TargetLink(url, timeout).start()
