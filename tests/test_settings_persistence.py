import pytest
from playwright.sync_api import expect
from pages.translator import TranslatorPage, SOURCE_LANG, TARGET_LANG


@pytest.mark.translator_settings_persistence
def test_settings_persistence(page):

    page.goto("https://www.languagewire.com/products/languagewire-translate/")
    expect(page).to_have_title("LanguageWire\u2028Translate | LanguageWire") #<-- U+2028 line separator (LS)

    lw_translator = TranslatorPage(page)

    expect(lw_translator.source_input_field).to_be_visible(timeout=10_000)

    lw_translator.select_languages()

    page.reload()

    expect(lw_translator.source_input_field).to_be_visible(timeout=10_000)

    source, target = lw_translator.get_languages()

    assert source == SOURCE_LANG
    assert target == TARGET_LANG



    


    





