from runner import Runner, Tournament
import unittest
import inspect

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print(f'{test}:')
            print({i: str(j) for i, j in cls.all_results[test].items()})

    def test_usain_nick(self):
        tour = Tournament(90, self.usain, self.nick)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_andrey_nick(self):
        tour = Tournament(90, self.andrey, self.nick)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_usain_andrey_nick(self):
        tour = Tournament(90, self.usain, self.andrey, self.nick)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_another_distance(self):
        tour = Tournament(9, self.nick, self.andrey, self.usain)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()

