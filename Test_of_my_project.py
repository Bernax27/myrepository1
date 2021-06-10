from new_reader import Csv_handler
import unittest

class Test_csv(unittest.TestCase):
    """Тесты библиотеки"""

    def test_finder_min(self):
        a = Csv_handler('dict.csv', 'new_file.csv')
        a.reader_csv_file()
        self.assertEqual(a.finder_min(), 1)

    def test_finder_max(self):
        a = Csv_handler('dict.csv', 'new_file.csv')
        a.reader_csv_file()
        self.assertEqual(a.finder_max(), 94191)


if __name__ == '__main__':
    unittest.main()
