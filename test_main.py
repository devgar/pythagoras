import unittest
from main import hypotenuse, cathetus

class HypotenuseTestCase(unittest.TestCase):
  """Tests for `main.py` hypotenuse function."""

  def test_5_is_3_4_hypotenuse(self):
    """Is 5 successfully determined as result of hypotenuse(3, 4)?"""
    
    self.assertEqual(hypotenuse(3, 4), 5.0)

  def test_hypotenuse_4_ranged_5_65_5_66(self):
    """Is hypotenuse(4) result in range [5.65, 5.66]"""
    h4 = hypotenuse(4)
    self.assertGreater(h4, 5.65)
    self.assertLess(h4, 5.66)

class CathetusTestCase(unittest.TestCase):
  """Test for `main.py` cathetus function."""

  def test_3_is_5_4_cathetus(self):
    """Is 3 successfully determined as result of cathetus(5, 4)?"""

    self.assertAlmostEqual(cathetus(5, 4), 3.0)

if __name__ == '__main__':
  unittest.main()