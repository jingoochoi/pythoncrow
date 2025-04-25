from playwright.sync_api import sync_playwright
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto('https://www.naver.com/')
page.wait_for_timeout(2000)
page.locator('a',has_text='엔터').click()
page.wait_for_timeout(1000)
page.locator('a',has_text='엔터홈').click()
input("종료하려면 Enter 키를 누르세요.")
browser.close()
p.stop()