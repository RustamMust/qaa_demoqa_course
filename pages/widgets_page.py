import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('check_accordian')
    def check_accordian(self, accordian_num):
        accordian = {
            'first': {'title': self.locators.FIRST_SECTION_HEADING, 'content': self.locators.FIRST_SECTION_TEXT},
            'second': {'title': self.locators.SECOND_SECTION_HEADING, 'content': self.locators.SECOND_SECTION_TEXT},
            'third': {'title': self.locators.THIRD_SECTION_HEADING, 'content': self.locators.THIRD_SECTION_TEXT}
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('fill_input_multi')
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('remove_value_from_multi')
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.SINGLE_MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('check_color_in_multi')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('remove_all_values_from_multi')
    def remove_all_values_from_multi(self):
        self.element_is_clickable(self.locators.REMOVE_ALL_MULTI_VALUES_BUTTON).click()
        try:
            multi_values = self.elements_are_present(self.locators.MULTI_VALUE)
            multi_value_count_after = len(multi_values)
        except TimeoutException:
            multi_value_count_after = 0
        return multi_value_count_after

    @allure.step('fill_input_single')
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('check_color_in_single')
    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('select_date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('set_date_by_text')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('set_item_from_list')
    def set_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    @allure.step('select_date_and_time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('change_slider_value')
    def change_slider_value(self):
        slider_value_before = self.element_is_visible(self.locators.INPUT_VALUE).get_attribute('value')
        slider = self.element_is_visible(self.locators.SLIDER)
        self.action_drag_and_drop_by_offset(slider, random.randint(10, 50), 0)
        slider_value_after = self.element_is_visible(self.locators.INPUT_VALUE).get_attribute('value')
        return slider_value_before, slider_value_after


class ProgressBar(BasePage):
    locators = ProgressBarLocators()

    @allure.step('change_progress_bar_value')
    def change_progress_bar_value(self):
        progress_bar_before = self.element_is_present(self.locators.PROGRESS_BAR_LINE).text
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        time.sleep(random.randint(2, 5))
        self.element_is_clickable(self.locators.START_STOP_BUTTON).click()
        progress_bar_after = self.element_is_present(self.locators.PROGRESS_BAR_LINE).text
        return progress_bar_before, progress_bar_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('check_tabs_page')
    def check_tabs_page(self, name_tab):
        tabs = {
            'what': {'title': self.locators.WHAT_TAB, 'content': self.locators.WHAT_TAB_TEXT},
            'origin': {'title': self.locators.ORIGIN_TAB, 'content': self.locators.ORIGIN_TAB_TEXT},
            'use': {'title': self.locators.USE_TAB, 'content': self.locators.USE_TAB_TEXT},
            'more': {'title': self.locators.MORE_TAB, 'content': self.locators.MORE_TAB_TEXT}
        }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        text = self.element_is_visible(tabs[name_tab]['content']).text
        return [button.text, len(text)]


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('get_text_from_tool_tip')
    def get_text_from_tool_tip(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOLTIP_TEXT)
        text = tool_tip_text.text
        return text

    @allure.step('check_tool_tip')
    def check_tool_tip(self):
        tool_tip_text_button = self.get_text_from_tool_tip(self.locators.HOVER_ME_TO_SEE_BUTTON,
                                                           self.locators.TOOLTIP_BUTTON)
        tool_tip_text_input = self.get_text_from_tool_tip(self.locators.HOVER_ME_TO_SEE_INPUT,
                                                          self.locators.TOOLTIP_INPUT)
        tool_tip_text_contrary = self.get_text_from_tool_tip(self.locators.CONTRARY_LINK,
                                                             self.locators.TOOLTIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tip(self.locators.SECTION_LINK, self.locators.TOOLTIP_SECTION)
        return tool_tip_text_button, tool_tip_text_input, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('check_menu')
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    @allure.step('check_select_menu')
    def check_select_menu(self):
        self.element_is_visible(self.locators.MULTI_SELECT_INPUT).send_keys('Green')
        self.element_is_visible(self.locators.MULTI_SELECT_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.MULTI_VALUE_SINGLE_DELETE).click()
        self.element_is_visible(self.locators.SELECT_OPTION).click()
        self.element_is_visible(self.locators.SELECT_OPTION_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_ONE).click()
        self.element_is_visible(self.locators.SELECT_ONE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.STANDARD_MULTI_SELECT).click()
        self.element_is_visible(self.locators.STANDARD_MULTI_SELECT).send_keys(Keys.RETURN)
        old_style_select_list = self.element_is_visible(self.locators.OLD_STYLE_SELECT)
        old_style_text = old_style_select_list.text
        return old_style_text.split()

