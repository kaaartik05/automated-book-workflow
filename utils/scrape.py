from playwright.sync_api import sync_playwright


def scrape_chapter():
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

    print("Scraping chapter content and taking screenshot...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Screenshot
        page.screenshot(path="chapter_screenshot.png", full_page=True)
        print("✅ Screenshot saved as 'chapter_screenshot.png'.")

        # Extract chapter text
        locator = page.locator("div#mw-content-text")
        locator.wait_for(timeout=10000)  # wait max 10s
        content = locator.inner_text()

        with open("chapter_text.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ Chapter text saved as 'chapter_text.txt'.")

        browser.close()
