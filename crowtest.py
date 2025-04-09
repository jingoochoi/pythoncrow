from datetime import date,timedelta
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)#false=open real browser
    page=browser.new_page()
    page.goto('https://www.kvca.or.kr/Program/user_board/list.html?a_gb=board&a_cd=7&a_item=0&sm=3_2')
    temp=page.locator('table tbody tr').first.text_content()
    print(temp)
    data=page.locator('table tbody tr').first.locator('td').last.text_content()