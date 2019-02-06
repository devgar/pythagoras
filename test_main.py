import unittest
from main import hypotenuse, cathetus

class HypotenuseTestCase(unittest.TestCase):
  """Tests for `main.py` hypotenuse function."""

  def test_5_is_3_4_hypotenuse(self):
    """Is 5 successfully determined as result of hypotenuse(3, 4)?"""
    
    self.assertEqual(hypotenuse(3, 4), 5.0)

class CathetusTestCase(unittest.TestCase):
  """Test for `main.py` cathetus function."""

  def test_3_is_5_4_cathetus(self):
    """Is 3 successfully determined as result of cathetus(5, 4)?"""

    self.assertAlmostEqual(cathetus(5, 4), 3.0)

if __name__ == '__main__':
  unittest.main()