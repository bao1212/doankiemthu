from unittest import TestLoader, TestSuite, TextTestRunner
from tests import TestHome
from tests import TestLogin
from tests import TestRegister

import testtools as testtools

if __name__ == "__main__":

  test_loader = TestLoader()
  test_suite = TestSuite((
    test_loader.loadTestsFromTestCase(TestHome),
    test_loader.loadTestsFromTestCase(TestLogin),
    test_loader.loadTestsFromTestCase(TestRegister),
  ))

  test_runner = TextTestRunner(verbosity=2)
  test_runner.run(test_suite)
