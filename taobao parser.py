from selenium import webdriver
from selenium.webdriver.common by import by
from selenium.webdriver.support.uni import WebDriver
from selenium.webdriver.support import 
from pyquery import PyQuery as pq
import json

driver = webdriver.Chrome("")
driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.5af911d99FQ5Bz&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F)

wait = WebDriverWait(driver, 10)

def search():
    try
        login = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#login > "))
        )

        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )

        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
        )
        input.send_keys("")
        submit.click()
    except TimeoutException:
        return search()

search()
get_product()

def get_product()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#manisrip_itemlist.items.item")
    html = driver.page_source
    doc = pq(html)
    items = doc("#manisrip_itemlist.items.item").items()

    for item in items:
        product = {
            "name": item.find(".J_ClickStat").text(),
            "price": item.find(".price").text(),
            "numbers of payments": item.find(".deal-cnt").text(),
            "location":item.find(".location").text(),
        }
        print(product)
        write_data(product)

def write_data(data):
    with open("./ .txt","a",encoding="utf-8") as f:
        f.write(json.dumps(data.ensure_ascii=False + "\n"))
