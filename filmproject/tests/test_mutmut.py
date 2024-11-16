"""
If someone can manage to write a test to pass mutation testing,
put it here.

Make sure you delete the pycache in tests directory and
delete mutations directory if it exists. Then run `mutmut run`

Good f'n luck.

"""
from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_always_passes(self):
        boolean = True
        if boolean:
            self.assertTrue(boolean)
        else:
            self.assertFalse(boolean)