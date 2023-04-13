import unittest


class TestInstall(unittest.TestCase):
    def test_typedllm_is_installed(self):
        import typedllm
        from typedllm.version import VERSION

        self.assertIsNotNone(typedllm)
        self.assertIsNotNone(VERSION)
