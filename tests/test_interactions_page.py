import allure
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('SortablePage')
    class TestSortablePage:
        @allure.title('Check sortable page')
        def test_sortable_page(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_order_before, list_order_after = sortable_page.change_list_order()
            grid_order_before, grid_order_after = sortable_page.change_grid_order()
            assert list_order_before != list_order_after, 'Order of the list has not been changed'
            assert grid_order_before != grid_order_after, 'Order of the grid has not been changed'

    @allure.feature('SelectablePage')
    class TestSelectablePage:
        @allure.title('Check selectable page')
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_list_element = selectable_page.select_list_item()
            active_grid_element = selectable_page.select_grid_item()
            assert len(active_list_element) > 0, 'Element has not been selected'
            assert len(active_grid_element) > 0, 'Element has not been selected'

    @allure.feature('ResizablePage')
    class TestResizablePage:
        @allure.title('Check resizable page')
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size_big, min_size_big = resizable_page.change_size_big_box()
            max_size_small, min_size_small = resizable_page.change_size_small_box()
            assert ('500px', '300px') == max_size_big, 'Maximum size is mot equal to "500px", "300px"'
            assert ('150px', '150px') == min_size_big, 'Minimum size is mot equal to "150px", "150px"'
            assert max_size_small != min_size_small, 'Small box size has not been changed'

    @allure.feature('DroppablePage')
    class TestDroppablePage:
        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The elements have not been dropped'

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            drop_text_not_acceptable, drop_text_acceptable = droppable_page.drop_accept()
            assert drop_text_not_acceptable == 'Drop here', 'Dropped element has been accepted'
            assert drop_text_acceptable == 'Dropped!', 'Dropped element has not been accepted'

        @allure.title('Check prevent propogation droppable')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box = droppable_page.drop_prevent_propogation()
            assert text_not_greedy_box == 'Dropped!', 'Elements text has not been changed'
            assert text_not_greedy_inner_box == 'Dropped!', 'Elements text has not been changed'
            assert text_greedy_box == 'Outer droppable', 'Elements text has been changed'
            assert text_greedy_inner_box == 'Dropped!', 'Elements text has not been changed'

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_position_after_move, will_position_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_position_after_move, not_will_position_after_revert = droppable_page.drop_revert_draggable(
                'not_will')
            assert will_position_after_move != will_position_after_revert, 'Elements has not reverted'
            assert not_will_position_after_move == not_will_position_after_revert, 'Elements has not reverted'

    @allure.feature('DragabblePage')
    class TestDragabblePage:
        @allure.title('Check simple dragabble')
        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before_position, after_position = dragabble_page.simple_drag_box()
            assert before_position != after_position, 'Position of the box has not been changed'

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            top_x, left_x = dragabble_page.axis_restricted_x()
            top_y, left_y = dragabble_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, 'Box position has not been changed'
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, 'Box position has not been changed'
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, 'Box position has not been changed'
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, 'Box position has not been changed'
