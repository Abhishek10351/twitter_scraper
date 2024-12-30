import os
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType


def get_random_proxy():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    port = random.randint(1000, 9999)
    proxy = f"{ip}:{port}"
    return proxy


def get_driver(headless=True):

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.page_load_strategy = "eager"
    proxy = get_random_proxy()
    options.proxy = Proxy({"proxyType": ProxyType.MANUAL, "httpProxy": proxy})

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://x.com/explore/tabs/for-you")
        return driver
    except Exception as e:
        print(e)
        return None


def twitter_login(driver):
    driver.implicitly_wait(100)
    driver.get("https://x.com/i/flow/login")


driver = get_driver(headless=False)


twitter_login(driver)


def get_trending_topics(driver, cookies) -> list[str]:
    driver.get("https://x.com/explore/tabs/for-you")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    # wait for the page to load
    driver.implicitly_wait(200)

    trending_topics = driver.find_elements(
        By.CSS_SELECTOR,
        'div[aria-label="Timeline: Explore"] div[role="link"]>div>div:nth-of-type(2)>span',
    )

    topics = [topic.text for topic in trending_topics]
    return topics


def change_proxy(driver, proxy, cookies=[]):
    # driver.quit()
    # if driver is not closed ,close it
    if driver is not None:
        driver.quit()
    driver = get_driver(proxy)
    return driver
