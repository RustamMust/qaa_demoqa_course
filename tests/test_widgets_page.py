import time
import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBar, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


@allure.suite('Widgets')
class TestWidgets:
    @allure.feature('AccordianPage')
    class TestAccordianPage:

        @allure.title('Check accordian page')
        def test_accordian_page(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    @allure.feature('AutoCompletePage')
    class TestAutoCompletePage:
        @allure.title('Check fill_multi_auto_complete')
        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, 'Added colors are missing in the input'

        @allure.title('Check remove_value_from_multi')
        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Value has not been deleted'

        @allure.title('Check remove_all_from_multi')
        def test_remove_all_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            multi_value_count_after = auto_complete_page.remove_all_values_from_multi()
            assert multi_value_count_after == 0, 'Value has not been deleted'

        @allure.title('Check single_auto_complete')
        def test_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'Added colors are missing in the input'

    @allure.feature('DatePickerPage')
    class TestDatePickerPage:
        @allure.title('Check change_date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'Date has not been changed'

        @allure.title('Check change_date_and_time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'Date and time has not been changed'

    @allure.feature('SliderPage')
    class TestSliderPage:
        @allure.title('Check slider_page')
        def test_slider_page(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            slider_value_before, slider_value_after = slider_page.change_slider_value()
            assert slider_value_before != slider_value_after, 'Slider value has not been changed'

    @allure.feature('ProgressBarPage')
    class TestProgressBarPage:
        @allure.title('Check progress_bar_page')
        def test_progress_bar_page(self, driver):
            progress_bar_page = ProgressBar(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_bar_before, progress_bar_after = progress_bar_page.change_progress_bar_value()
            assert progress_bar_before != progress_bar_after, 'Progress Bar value has not been changed'

    @allure.feature('TabsPage')
    class TestTabsPage:
        @allure.title('Check tabs_page')
        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_button_text = tabs_page.check_tabs_page('what')
            origin_button, origin_button_text = tabs_page.check_tabs_page('origin')
            use_button, use_button_text = tabs_page.check_tabs_page('use')
            more_button, more_button_text = tabs_page.check_tabs_page('more')
            assert what_button == 'What' and what_button_text != 0, 'What Tab has not been pressed'
            assert origin_button == 'Origin' and origin_button_text != 0, 'Origin Tab has not been pressed'
            assert use_button == 'Use' and use_button_text != 0, 'Use Tab has not been pressed'
            assert more_button == 'More' and more_button_text != 0, 'More Tab has not been pressed'

    @allure.feature('ToolTipsPage')
    class TestToolTipsPage:
        @allure.title('Check tooltips_page')
        def test_tooltips_page(self, driver):
            tooltips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltips_page.open()
            text_button, text_input, text_contrary, text_section = tooltips_page.check_tool_tip()
            assert text_button == 'You hovered over the Button', 'Hover missing or incorrect text'
            assert text_input == 'You hovered over the text field', 'Hover missing or incorrect text'
            assert text_contrary == 'You hovered over the Contrary', 'Hover missing or incorrect text'
            assert text_section == 'You hovered over the 1.10.32', 'Hover missing or incorrect text'

    @allure.feature('MenuPage')
    class TestMenuPage:
        @allure.title('Check menu_page')
        def test_menu_page(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            expected_data = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            assert data == expected_data, 'Menu items do not exist'

    @allure.feature('SelectMenuPage')
    class TestSelectMenuPage:
        @allure.title('Check select_menu_page')
        def test_select_menu_page(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open()
            old_style_text = select_menu_page.check_select_menu()
            expected_text = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']
            assert old_style_text == expected_text, 'Text does not displayed correctly'






