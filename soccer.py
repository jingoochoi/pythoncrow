from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(headless=True)
    pa=b.new_page()
    pa.goto('https://www.kleague.com/record/team.do')
    t1=pa.locator('table#t1>tbody>tr').first.locator('td').nth(3).text_content()
    m=pa.locator('table#t1>tbody>tr').nth(1).locator('td').nth(2).text_content()
    s=pa.locator('table#t1>tbody>tr').nth(1).locator('td').nth(3).text_content()
    t2=(38-int(m))*3+int(s)
    v=int(int(t1)/t2*100)
    print(f'victory probability:{v}%')