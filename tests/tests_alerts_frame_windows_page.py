import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramesPage, \
    ModelDialogsPage


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

    class TestFrame:
        def test_frame(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame_1 = frame_page.check_frame('frame1')
            result_frame_2 = frame_page.check_frame('frame2')
            assert result_frame_1 == ['This is a sample page', '500px', '350px'], 'Frame has not been exist'
            assert result_frame_2 == ['This is a sample page', '100px', '100px'], 'Frame has not been exist'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frames()
            assert parent_text == 'Parent frame', 'Nested Frame has not been exist'
            assert child_text == 'Child Iframe', 'Nested Frame has not been exist'

    class TestModelDialogs:
        def test_model_dialogs(self, driver):
            model_dialogs_page = ModelDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            model_dialogs_page.open()
            small_button, large_button = model_dialogs_page.check_model_dialogs()
            assert small_button[1] < large_button[1], 'Body of small button is bigger then in large button'
            assert small_button[0] == 'Small Modal', 'Title of small button is not Small Modal'
            assert large_button[0] == 'Large Modal', 'Title of large button is not Large Modal'


