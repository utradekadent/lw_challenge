from playwright.sync_api import Page

# Specify language pair
SOURCE_LANG = "English"
TARGET_LANG = "Danish"

# Specify source text and expected target text
SOURCE_TEXT = "Nice to meet you!"
TARGET_TEXT = "Godt at møde dig!"

# Specify the source text doc file
SOURCE_DOC = "test_files/source_text.docx"


class TranslatorPage:
    def __init__(self, page: Page):

        self.page = page

        frame_locator = page.locator("#lwt-widget").content_frame

        self.accept_cookies_btn = page.get_by_role("button", name="Accept cookies")

        self.source_lang_dropdown_btn = frame_locator\
        .get_by_role("button")\
        .filter(has_text="keyboard_arrow_down").first
        
        self.source_lang_btn = frame_locator\
        .get_by_role("menuitem", name=SOURCE_LANG)

        self.target_lang_dropdown_btn = frame_locator.\
        get_by_role("button")\
        .filter(has_text="keyboard_arrow_down").nth(1)
        
        self.target_lang_btn = frame_locator\
        .get_by_role("menuitem", name=TARGET_LANG)

        self.source_input_field = frame_locator\
        .locator("//textarea[@name='translation-input']")

        self.target_output_field = frame_locator\
        .locator("//div[@class='lw-output-text__text']")

        self.browse_btn = frame_locator\
        .locator("//span[normalize-space()='Browse file']")

        self.source_doc_info_item = frame_locator\
        .locator("//div[@class='lw-source-document__document-info-item']")
        
        self.target_doc_info_item = frame_locator\
        .locator("//div[@class='lw-output-document__document-info-item']")
        
        self.translate_btn = frame_locator\
        .locator("//span[@class='lw-source-document__translate-document-button-text']")

        self.download_btn = frame_locator\
        .locator("//span[contains(@class, 'mdc-button__label') and text() = 'Download']")
        
        self.swap_btn = frame_locator\
        .get_by_role("button").filter(has_text="sync_alt")

        # To determine source language
        self.source_language_label = frame_locator\
        .locator("//lw-language-select[@searchtitle='Search source language']//button[contains(@class, 'lw-language-select__button--selected')]/span[@class='mdc-button__label']")

        # To determine target language
        self.target_language_label = frame_locator\
        .locator("//lw-language-select[@searchtitle='Search target language']//button[contains(@class, 'lw-language-select__button--selected')]/span[@class='mdc-button__label']")

   
    # Get language pair based on the 'language_label' locator    
    def get_languages(self):
        source = self.source_language_label.inner_text()
        target = self.target_language_label.inner_text()
        return source, target

    # Select language pair by selecting them from dropdown menu
    def select_languages(self):
        self.source_lang_dropdown_btn.click()
        self.source_lang_btn.click()
        self.target_lang_dropdown_btn.click()
        self.target_lang_btn.click()

    # Paste source text
    def input_source_text(self):
        self.source_input_field.fill(SOURCE_TEXT)

    # Swap languages
    def swap_languages(self):
        self.swap_btn.click()
    


        


    

    

 

   

    
    



   

