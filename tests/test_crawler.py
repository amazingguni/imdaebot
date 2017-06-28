from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import tempfile

class TestCrawler:
    def test_crawl(self, crawler):
        crawler.crawl()

    def test_spike(self):
        driver = webdriver.Chrome()
        try:
            driver.set_window_size(1000, 1400)
            driver.get('https://www.myhome.go.kr/hws/portal/sch/selectRsdtRcritNtcView.do')
            
            time.sleep(2)
            self.click_area(driver, '경기도')
            time.sleep(2)
            self.click_progress_saling(driver)
            time.sleep(2)
            self.click_search_button(driver)
            time.sleep(2)
            screenshot_temp_file = tempfile.NamedTemporaryFile(suffix='.png', prefix='imdaebot_', delete=False)
            print(screenshot_temp_file.name)
            self.capture_screenshot_notice_table(driver, screenshot_temp_file.name)
            time.sleep(10)
        finally:
            driver.close()

    def click_area(self, driver, area):
        selector = 'div.region [alt={}]'.format(area)
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            ).click()
    def click_search_button(self, driver):
        selector = '.searchBtn'
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            ).click()
    
    def click_progress_saling(self, driver):
        selector = '#srchPrgrStts_1'
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            ).click()
    
    def capture_screenshot_notice_table(self, driver, screenshot_path):
        selector = '#schTbody tr:last-child'
        notice_table_element = driver.find_element_by_css_selector(selector)
        ActionChains(driver).move_to_element(notice_table_element).perform()
        driver.get_screenshot_as_file(screenshot_path)
