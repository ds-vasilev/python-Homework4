import unittest
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES
from blossom import get_page_content
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UrlTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.all_test_cases = PUBLIC_TEST_CASES + SECRET_TEST_CASES

    def test_url(self):
        """Тесирование функции разнесения данных из json по таблицам. Удаление созданной БД."""
        for test_case in self.all_test_cases:
            test_inp = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertEqual(expected, get_page_content(test_inp)['get_page_content']['is_success'])
