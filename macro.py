from playwright.sync_api import sync_playwright
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto('https://chatgpt.com/')
page.wait_for_timeout(2000)
page.locator('p.placeholder').fill('오늘의 업계 트렌드')
page.wait_for_timeout(1000)
page.locator('button#composer-submit-button').click()
input("종료하려면 Enter 키를 누르세요.")
browser.close()
p.stop()