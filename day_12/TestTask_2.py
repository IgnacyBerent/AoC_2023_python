import unittest
from task_2 import calculate_poss_r

examples = [
    ('?#?#?#?#?#?#?#?', [1, 3, 1, 6], 1),
    ('.??..??...?##.', [1, 1, 3], 4),
    ('?###????????', [3, 2, 1], 10)
]


class MyTestCase(unittest.TestCase):
    def test_examples(self):
        for record, nums, expected in examples:
            with self.subTest(record=record, nums=nums, expected=expected):
                self.assertEqual(calculate_poss_r(record, nums), expected)


if __name__ == '__main__':
    unittest.main()
