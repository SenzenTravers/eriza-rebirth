from ..utils import coureur_handler
import unittest


class TestCoureurMethods(unittest.TestCase):
    def setUp(self):
        self.course = coureur_handler.Course()
        self.course.participants = [
            {"name": "Lucile", "starting_wordcount": 0, "ending_wordcount": 0},
            {"name": "Jean", "starting_wordcount": 10, "ending_wordcount": -5},
            {"name": "Bob", "starting_wordcount": 10, "ending_wordcount": 35},
        ]

    def test_give_starting_wordcount_when_already_joined(self):
        self.course.give_starting_wordcount('Lucile', 399)
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 399, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35}
            ]
        )

    def test_give_starting_wordcount_when_not_already_joined(self):
        self.course.give_starting_wordcount('Bidule', 399)
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
                {'name': 'Bidule', 'starting_wordcount': 399, 'ending_wordcount': 0}
            ]
        )

    def test_give_ending_wordcount_when_not_already_joined(self):
        self.course.give_ending_wordcount('Bidule', 399)
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
                {'name': 'Bidule', 'starting_wordcount': 399, 'ending_wordcount': 399}
            ]
        )

    def test_give_ending_wordcount(self):
        self.course.give_ending_wordcount('Lucile', 399)
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 399},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
            ]
        )

    def test_give_ending_wordcount_when_inferior(self):
        self.course.give_ending_wordcount('Bob', 5)
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 5},
            ]
        )