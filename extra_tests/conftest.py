import pytest, json, os
from playwright.sync_api import sync_playwright
from pathlib import Path


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

@pytest.fixture
def load_translations():
    def loader(locale):
        path = Path(f"extra_tests/i18n/{locale}.json")
        if not path.exists():
            raise FileNotFoundError(f"Translation file for locale '{locale}' not found at {path}")

        with path.open(encoding="utf-8") as f:
            return json.load(f)
    
    return loader