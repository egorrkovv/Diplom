from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import allure

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(15)



def test_choose_a_tour():
    driver.get("https://fstravel.com/")
    
    driver.find_element(By.CSS_SELECTOR, '[class="v-expert v-header-left-link trslt"]').click()

    email = driver.find_element(By.CSS_SELECTOR, '[class="name__field form__field"]').is_enabled()

    assert email == True


def test_review():
    driver.get("https://fstravel.com/")

    driver.find_element(By.XPATH, "//*[@id='uxs_cepveveb27f1by13h327kin5']/img").click()

    review_smiles = driver.find_element(By.CSS_SELECTOR, '[class="uxs-13AIcIcOf2 uxs-1gpk5ge uxs-3YvDR443pV"]').is_displayed()

    assert review_smiles == True



def test_press_hot_tour():
    driver.get("https://fstravel.com/")

    driver.find_element(By.CSS_SELECTOR, '[class="links__link hot-tour-tab"]').click()
    
    active_hot_tour_button = driver.find_element(By.CSS_SELECTOR, '#app > div > header > div.search-menu.new-header__container.container > div > nav > a.links__link.hot-tour-tab').is_displayed()

    assert active_hot_tour_button == True


def test_profile():
    driver.get("https://fstravel.com/")

    driver.maximize_window()
    
    driver.find_element(By.CSS_SELECTOR, '[class="popmechanic-btn popmechanic-btn-second"]').click()

    driver.find_element(By.CSS_SELECTOR, '[class="v-account-block"]').click()
  
    email2 = driver.find_element(By.CSS_SELECTOR, '[name="email"]').is_displayed()
    
    assert email2 == True
    


driver.quit()