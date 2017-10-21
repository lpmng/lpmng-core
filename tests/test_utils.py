from django.test import TestCase
import coreapp.utils

class HashPasswordTestCase(TestCase):
    def test_hash_password(self):
        self.assertEqual('{SHA}PkEX3wXp71oONtMvdlHdq6AnSPM=', coreapp.utils.hash_password('plouf'))
        self.assertEqual('{SHA}6PyxUBps2qg0332JEJ9tFDrRtIo=', coreapp.utils.hash_password('plif'))
