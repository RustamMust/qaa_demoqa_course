import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, NestedFramesPageLocators, ModelDialogsPageLocators
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


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_number):
        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_OF_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_OF_FRAME).text
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModelDialogsPage(BasePage):
    locators = ModelDialogsPageLocators()

    def check_model_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODEL_BUTTON).click()
        body_of_small_button = self.element_is_visible(self.locators.BODY_OF_SMALL_MODEL_BUTTON).text
        title_of_small_button = self.element_is_visible(self.locators.TITLE_OF_SMALL_MODEL_BUTTON).text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODEL_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODEL_BUTTON).click()
        body_of_large_button = self.element_is_visible(self.locators.BODY_OF_LARGE_MODEL_BUTTON).text
        title_of_large_button = self.element_is_visible(self.locators.TITLE_OF_LARGE_MODEL_BUTTON).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODEL_BUTTON).click()
        return [title_of_small_button, len(body_of_small_button)], [title_of_large_button, len(body_of_large_button)]