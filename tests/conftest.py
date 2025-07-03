import pytest
from playwright.sync_api import sync_playwright
from pages.translator import TranslatorPage


@pytest.fixture(params=["chromium"], scope="function")
def browser(request):
    browser_type = request.param

    with sync_playwright() as playwright:
        launch_args = {
            "headless": False,
            # "slow_mo": 500
            }

        launchers = {
            "chromium": lambda: playwright.chromium.launch(**launch_args),
            "firefox": lambda: playwright.firefox.launch(**launch_args),
            "chrome": lambda: playwright.chromium.launch(channel="chrome", **launch_args),
            "msedge": lambda: playwright.chromium.launch(channel="msedge", **launch_args),
            "webkit": lambda: playwright.webkit.launch(**launch_args),
        }

        if browser_type not in launchers:
            raise ValueError(f"Unsupported browser: {browser_type}")

        browser = launchers[browser_type]()
        
        yield browser
        browser.close()
        

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        permissions=['notifications']
        )
    page = context.new_page()
    lw_translator=TranslatorPage(page)
    #page.goto("https://www.languagewire.com/products/languagewire-translate/", wait_until="domcontentloaded")
    #expect(page).to_have_title("LanguageWire\u2028Translate | LanguageWire") #<-- U+2028 line separator (LS)
    ## Dismiss the cookies dialogue
    page.add_locator_handler(
        page.get_by_text('We value your privacy'),
        lambda: lw_translator.accept_cookies_btn.click()
        )
    yield page
    page.close()
    context.close()


