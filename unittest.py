import unittest

class TestScoreTable(unittest.TestCase):

	def test_score(self):
		INSERT INTO score(score) VALUES (11) #makes sure that scores are being contained in table
		self.assertTrue(score.contains(11))
		
class TestEndGame(unittest.TestCase):
	def test_end(self):
		steps = 65
		assertTrue(gameOpen) #tests that the game begins ending sequence after 60 steps
	
	
if __name__ == '__main__':
    unittest.main()