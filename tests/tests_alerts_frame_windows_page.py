import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'New tab has not been opened'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', 'New window has not been opened'

    class TestAlerts:
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_button()
            assert alert_text == 'You clicked a button', 'Alert has not been displayed'

        def test_time_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_time_alert_button()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert has not been displayed'

        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_button()
            assert alert_text == 'You selected Ok', 'Alert has not been displayed'

        def test_promt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, prompt_text = alerts_page.check_prompt_button()
            assert text in prompt_text, 'Alert has not been displayed'


