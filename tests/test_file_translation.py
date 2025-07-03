import pytest, os, re, docxpy
from playwright.sync_api import expect
from pages.translator import TranslatorPage, TARGET_TEXT, SOURCE_DOC
from time import perf_counter

MAX_TRANSLATION_TIME = 30 #seconds

@pytest.mark.translator_file
@pytest.mark.flaky(retries=3, delay=5)
def test_file_translation(page):

    # Start measuring time
    start_time_p = perf_counter()
    print("\nLoading page...")

    page.goto("https://www.languagewire.com/products/languagewire-translate/")
    expect(page).to_have_title("LanguageWire\u2028Translate | LanguageWire") #<-- U+2028 line separator (LS)

    # Stop measuring and display elapsed time
    end_time_p = perf_counter() - start_time_p
    print(f"Page loaded... in {round(end_time_p, 2)} seconds")

    lw_translator = TranslatorPage(page)
    
    expect(lw_translator.browse_btn).to_be_visible(timeout=10_000)

    lw_translator.select_languages()

    # Start waiting for the file chooser
    with page.expect_file_chooser() as fc_info:
        # Perform the action that opens file chooser
        lw_translator.browse_btn.click()
        file_chooser = fc_info.value
        file_chooser.set_files(SOURCE_DOC)
        
        # Start measuring time
        print("\nTranslating text...")
        start_time_t = perf_counter()


    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download (no need to click on the 'Download' button since it happens automatically)
        lw_translator.translate_btn.click()
    
        # Wait for the download button to appear. Disabling timeout to handle large files.
        lw_translator.download_btn.wait_for(timeout=0)
        
        # Stop measuring
        end_time_t = perf_counter() - start_time_t
        
        # Assert time
        assert end_time_t <= MAX_TRANSLATION_TIME, (
            f"Translation took too long: {round(end_time_t, 2)}s "
            f"(expected <= {MAX_TRANSLATION_TIME}s)"
        )

        # Display elapsed time
        print(f"Text translated... in {round(end_time_t, 2)} seconds")

        download = download_info.value

        # Verify file name
        assert re.match(r"source_text-[A-Za-z-]+\.docx", download.suggested_filename)
        
        file_name = download.suggested_filename #<-- maintaining original file name for verification
        destination_folder_path = "test_files"
        file = (os.path.join(destination_folder_path, file_name))
        download.save_as(file)
    
    # Extract text from the downloaded doc
    target_doc_text = docxpy.process(file)

    # Assert text
    assert target_doc_text == TARGET_TEXT