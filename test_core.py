import unittest
from worldweather import core


class TestCore(unittest.TestCase):
    def test_sanitize_query(self):

        # Test if forbidden chars are removed
        query = '@_*/~a'
        sanitized = core.sanitize_query(query)
        self.assertEquals(sanitized, 'a')

        # And if allowed chars are kept
        query = '123abcDEF,;- '
        sanitized = core.sanitize_query(query)
        self.assertEquals(sanitized, '123abcDEF,;-')

        # And also make sure the length is cut down to 128
        query = 'a' * 300
        sanitized = core.sanitize_query(query)
        self.assertEquals(len(sanitized), 128)
