import unittest
import logging
import traceback

logging.basicConfig(
    level=logging.INFO,
    filename='runner_test.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


#first = Runner('Вося', 10)
#second = Runner('Илья', 5)
#third = Runner('Арсен', 10)

#t = Tournament(101, first, second)
#print(t.start())


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            rn = Runner('Vasya', -10)
            for i in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner\n{e}')
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            rn = Runner(5)
            for i in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для Runner\n{e}')
            logging.warning(traceback.format_exc())
        rn = Runner(name='John1')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        runner1 = Runner(name='John2')
        runner2 = Runner(name='John3')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
