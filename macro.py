from playwright.sync_api import sync_playwright
import random
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
delay = random.randint(80, 150)
page.goto('https://www.naver.com/')
page.wait_for_timeout(1000)
page.locator('a',has_text='스포츠').click()
page.wait_for_timeout(1000)
page.locator('a',has_text='스포츠홈').click()
page.wait_for_timeout(1000)
page.locator('a',has_text='해외축구').click()
page.wait_for_timeout(1000)
page.locator('a',has_text='이강인').click()
input("종료하려면 Enter 키를 누르세요.")
browser.close()
p.stop()