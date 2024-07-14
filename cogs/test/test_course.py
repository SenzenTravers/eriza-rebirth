from ..utils import coureur_handler
import unittest


class TestCoureurMethods(unittest.TestCase):
    def setUp(self):
        self.course = coureur_handler.Course(
            participants=[
            {"name": "Lucile", "starting_wordcount": 0, "ending_wordcount": 0},
            {"name": "Jean", "starting_wordcount": 10, "ending_wordcount": -5},
            {"name": "Bob", "starting_wordcount": 10, "ending_wordcount": 35},
        ],
        is_on=True
        )

    def test_give_starting_wordcount_when_already_joined(self):
        result = self.course.give_starting_wordcount('Lucile', "blob")
        self.assertEqual(
            result,
            [
                {'name': 'Lucile', 'starting_wordcount': "399", 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35}
            ]
        )

    def test_give_starting_wordcount_when_already_joined(self):
        self.course.give_starting_wordcount('Lucile', "399")
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': "399", 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35}
            ]
        )

    def test_give_starting_wordcount_when_not_already_joined(self):
        self.course.give_starting_wordcount('Bidule', "399")
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
                {'name': 'Bidule', 'starting_wordcount': "399", 'ending_wordcount': 0}
            ]
        )

    def test_give_ending_wordcount_when_not_already_joined(self):
        self.course.give_ending_wordcount('Bidule', "399")
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': 0},
                {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
                {'name': 'Bidule', 'starting_wordcount': "399", 'ending_wordcount': "399"}
            ]
        )

    def test_give_ending_wordcount(self):
        self.course.give_ending_wordcount('Lucile', "399")
        self.assertEqual(
            self.course.participants,
            [
                {'name': 'Lucile', 'starting_wordcount': 0, 'ending_wordcount': "399"},
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

    def test_participant_is_joining_already_joined(self):
        result = self.course.participant_is_joining({"name": 'Lucile', "wordcount": "399"})
        self.assertEqual(
            result,
            [1, 'Lucile joint avec 399 mots.']
        )

        self.assertEqual(
                self.course.participants,
                [
                    {'name': 'Lucile', 'starting_wordcount': "399", 'ending_wordcount': 0},
                    {'name': 'Jean', 'starting_wordcount': 10, 'ending_wordcount': -5},
                    {'name': 'Bob', 'starting_wordcount': 10, 'ending_wordcount': 35},
                ]
        )

    def test_participant_is_joining_no_sprint(self):
        self.course.is_on = False
        result = self.course.participant_is_joining({"name": 'Lucile', "wordcount": "399"})
        self.assertEqual(
            result,
            [0, 'Aucune course en cours. Tanpis.']
        )

    def test_participant_is_joining_wrong_format(self):
        result = self.course.participant_is_joining({"name": 'Lucile', "wordcount": "xxx"})
        self.assertEqual(
            result,
            [0, 'Format: ```!cj VOTRE_NOMBRE_DE_MOT```']
        )
