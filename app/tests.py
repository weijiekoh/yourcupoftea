import unittest
import ranking
import parties
import questions

class TestRanking(unittest.TestCase):
    """
    Tests for the ranking calculation
    """

    def setUp(self):
        self.sample_responses_1 = [
            ('checkbox_1', [u'0', u'2', u'3', u'4']),
            ('checkbox_3', [u'1', u'3']),
            ('slider_1', [u'5']),
            ('radio_2', [u'2']),
            ('slider_4', [u'3']),
            ('radio_0', [u'0']),
            ('slider_2', [u'5']),
            ('slider_3', [u'5']),
            ('slider_0', [u'5']),
            ('radio_4', [u'2'])
        ]

        self.sample_responses_2 = [
            ('slider_4', [u'3']),
            ('slider_2', [u'3']),
            ('slider_3', [u'3']),
            ('slider_0', [u'3']),
            ('slider_1', [u'3'])
        ]


    def test_sort_responses(self):
        """
        Test the sort_responses method, which converts a flask request.form.lists() data structure to something more sensible
        """
        self.assertEqual(ranking.sort_responses(self.sample_responses_1), 
                {
                    0: {'importance': 5, 'radio': 0}, 
                    1: {'importance': 5, 'checkbox': [0, 2, 3, 4]}, 
                    2: {'importance': 5, 'radio': 2}, 
                    3: {'importance': 5, 'checkbox': [1, 3]}, 
                    4: {'importance': 3, 'radio': 2}
                }
            )


    def test_fill_in_blank_responses(self):
        self.assertEqual(ranking.fill_in_blank_responses(ranking.sort_responses(self.sample_responses_2), questions.questions),
                {
                    0: {'importance': 3, 'radio': 2}, 
                    1: {'importance': 3, 'checkbox': []}, 
                    2: {'importance': 3, 'radio': 2}, 
                    3: {'importance': 3, 'checkbox': []}, 
                    4: {'importance': 3, 'radio': 2}
                }
            )

    def test_sample_1(self):
        results = ranking.calculate(self.sample_responses_1, parties.parties, questions.questions)
        print results
        return True


if __name__ == '__main__':
    unittest.main()
