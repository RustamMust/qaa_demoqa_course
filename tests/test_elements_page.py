import allure
import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:

    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_page(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'Full name does not match'
            assert email == output_email, 'Email name does not match'
            assert current_address == output_current_address, 'Current address name does not match'
            assert permanent_address == output_permanent_address, 'Permanent address name does not match'

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    @allure.feature('RadioButton')
    class TestRadioButton:

        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_radio_button_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_radio_button_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_radio_button_result()
            assert output_yes == 'Yes', 'Yes have not been selected'
            assert output_impressive == 'Impressive', 'Impressive have not been selected'
            assert output_no == 'No', 'No have not been selected'

    @allure.feature('WebTable')
    class TestWebTable:

        @allure.title('Check WebTable and Person')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, 'New person not in table result'

        @allure.title('Check WebTable SearchPerson')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'Person not found in the table'

        @allure.title('Check WebTable UpdatePersonInfo')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'Person card has not been changed'

        @allure.title('Check WebTable DeletePersonInfo')
        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted_info()
            assert text == 'No rows found', 'Person info has not been deleted'

        @allure.title('Check WebTable ChangeRowCount')
        def test_web_table_change_row_count(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], ('Number of rows in the table has not been changed or has '
                                                       'changed incorrectly')

    @allure.feature('ButtonsPage')
    class TestButtonsPage:

        @allure.title('Check ButtonsPage')
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', 'Double button has not been clicked'
            assert right == 'You have done a right click', 'Right button has not been clicked'
            assert click == 'You have done a dynamic click', 'Click button has not been clicked'

    @allure.feature('LinksPage')
    class TestLinksPage:

        @allure.title('Check Link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'Link is broken or URL is incorrect'

        @allure.title('Check BrokenLink')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'Link works or the status code is not 400'

    @allure.feature('UploadAndDownload')
    class TestUploadAndDownload:

        @allure.title('Check UploadFile')
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result_text_after_upload = upload_download_page.upload_file()
            assert file_name == result_text_after_upload, 'File has not been upload'

        @allure.title('Check DownloadFile')
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, 'File has not been download'

    @allure.feature('DynamicProperties')
    class TestDynamicProperties:

        @allure.title('Check DynamicProperties')
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_button_before, color_button_after = dynamic_properties_page.check_changed_of_color()
            assert color_button_before != color_button_after, 'Colors have not been changed'

        @allure.title('Check AppearOfButton')
        def test_appear_of_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, 'Button did not appear after 5 second'

        @allure.title('Check EnableOfButton')
        def test_enable_of_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'Button did not enable after 5 second'
