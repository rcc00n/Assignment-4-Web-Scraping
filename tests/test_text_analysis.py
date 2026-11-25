import io
import unittest
from unittest.mock import patch
import main

class TextAnalysisTests(unittest.TestCase):
    def test_country_aliases_and_word_boundaries(self):
        self.assertEqual(main.clean_country_name('U.S.A.'), 'United States')
        self.assertEqual(main.clean_country_name('U.K.'), 'United Kingdom')
        counts = main.country_occurrence('Canada CANADA Canadian; Japan.', ['Canada', 'Japan', 'France'])
        self.assertEqual(counts, {'Canada': 2, 'Japan': 1})
        self.assertEqual(main.sort_country_counts(counts), [('Canada', 2), ('Japan', 1)])

    def test_page_text_uses_fixture_without_network(self):
        with patch('main.urllib.request.urlopen', return_value=io.BytesIO(b'<h1>Canada</h1><p>Japan</p>')):
            text = main.get_text_of_the_page('https://example.invalid/fixture')
        self.assertNotIn('<', text)
        self.assertEqual(main.country_occurrence(text, ['Canada', 'Japan']), {'Canada': 1, 'Japan': 1})

    def test_province_fixture_retains_original_alias_behavior(self):
        with patch('main.urlopen', return_value=io.BytesIO(b'Alberta AB Manitoba')):
            counts = main.provinceScraper('https://example.invalid/fixture')
        self.assertEqual(counts['Alberta'], 2)
        self.assertEqual(counts['Manitoba'], 1)
