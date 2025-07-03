import pytest, re
from playwright.sync_api import expect
from pages.translator import TranslatorPage, SOURCE_LANG, TARGET_LANG


@pytest.mark.translator_swap_languages
def test_swap_languages(page):

    page.goto("https://www.languagewire.com/products/languagewire-translate/")
    expect(page).to_have_title("LanguageWire\u2028Translate | LanguageWire") #<-- U+2028 line separator (LS)

    lw_translator = TranslatorPage(page)
    
    expect(lw_translator.source_input_field).to_be_visible(timeout=10_000)

    lw_translator.select_languages()

    lw_translator.swap_languages()

    new_source, new_target = lw_translator.get_languages()
    
    # Only get the base language name without any parenthetical suffix, and without trailing spaces.
    assert re.match(r'^[^\(]+', new_source).group().strip() == re.match(r'^[^\(]+', TARGET_LANG).group().strip()
    assert re.match(r'^[^\(]+', new_target).group().strip() == re.match(r'^[^\(]+', SOURCE_LANG).group().strip()

    

    
