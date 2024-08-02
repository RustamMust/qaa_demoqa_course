import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_OF_NEW_OPENED_PAGE).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_OF_NEW_OPENED_PAGE).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert_button(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_time_alert_button(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_button(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        alert_text = self.element_is_visible(self.locators.CONFIRM_RESULT).text
        return alert_text

    def check_prompt_button(self):
        text = f'autotest{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        prompt_text = self.element_is_visible(self.locators.PROMT_RESULT).text
        return text, prompt_text
