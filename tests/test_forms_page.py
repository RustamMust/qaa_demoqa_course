import time
import allure

from pages.forms_page import FormPage


@allure.suite('Form')
class TestForm:
    @allure.feature('FormPage')
    class TestFormPage:
        @allure.title('Check form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()
            result_info = form_page.form_result()
            assert ([person_info.first_name + ' ' + person_info.last_name, person_info.email]
                    == [result_info[0], result_info[1]]), 'Form has not been filled'
