import pytest
from playwright.sync_api import expect

@pytest.mark.test_homepage
@pytest.mark.parametrize("locale", ["en", "fr-fr", "es-es", "da", "de"])
def test_homepage(locale, browser, load_translations):
    translations = load_translations(locale)

    page = browser.new_page()
    page.goto(f"https://languagewire.com/{locale}", wait_until="domcontentloaded")

    # Locators
    cookies_banner_title = page.get_by_text(translations["cookies_banner_title"])
    accept_cookies_btn = page.get_by_role("button", name=translations["accept_cookies_btn"])
    demo_btn = page.get_by_role("link", name=translations["demo_btn"], exact=True)
    contact_btn = page.locator("#main-header").get_by_role("link", name=translations["demo_btn"])

    expect(cookies_banner_title).to_be_visible(timeout=15_000)

    expect(cookies_banner_title).to_contain_text(translations["cookies_banner_title"])

    accept_cookies_btn.click()

    if contact_btn.is_visible():
        contact_btn.click()
    elif demo_btn.is_visible():
        demo_btn.click()
    else:
        raise Exception("Neither the main nor alternative demo button was found")

    page.screenshot(path="screenshots//"f"demo_page_{locale}.jpg")
    
    page.close()

        
