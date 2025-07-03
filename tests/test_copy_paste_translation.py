import pytest
from playwright.sync_api import expect
from pages.translator import TranslatorPage, TARGET_TEXT


@pytest.mark.translator_copy_paste
def test_copy_paste_translation(page):

    page.goto("https://www.languagewire.com/products/languagewire-translate/")
    expect(page).to_have_title("LanguageWire\u2028Translate | LanguageWire") #<-- U+2028 line separator (LS)

    lw_translator = TranslatorPage(page)

    expect(lw_translator.source_input_field).to_be_editable(timeout=10_000)

    lw_translator.select_languages()
    
    lw_translator.input_source_text()

    expect(lw_translator.target_output_field).to_have_text(TARGET_TEXT, ignore_case=False)
