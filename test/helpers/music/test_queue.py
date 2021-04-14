import unittest
from frozendict import frozendict

from src.helpers.music.queue import Queue, QueueIsEmptyError, RemoveOutOfIndexError

class QueueTest(unittest.TestCase):

    queue1 = [
        frozendict({ 'name' : 'song1' }),
        frozendict({ 'name' : 'song2' }),
        frozendict({ 'name' : 'song3' })
    ]

    queue2 = {
        frozendict({ 'name' : 'song1' }),
        frozendict({ 'name' : 'song2' }),
        frozendict({ 'name' : 'song3' })
    }

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.q1 = Queue(QueueTest.queue1)
        self.q2 = Queue(QueueTest.queue2)
        self.q3 = Queue()

    def tearDown(self):
        pass
    
    def test_create_queue(self):
        q = Queue()
        self.assertEqual(q._queue, [])

    def test_is_empty(self):
        self.assertFalse(self.q1.is_empty)
        self.assertTrue(self.q3.is_empty)

    def test_first_track(self):
        self.assertEqual(self.q1.first_track['name'], QueueTest.queue1[0]['name'])
        with self.assertRaises(QueueIsEmptyError):
            self.q3.first_track

    def test_current_track(self):
        self.assertEqual(self.q1.current_track['name'], QueueTest.queue1[0]['name'])
        self.q1.get_next_track()
        self.assertEqual(self.q1.current_track['name'], QueueTest.queue1[1]['name'])
        self.assertNotEqual(self.q1.current_track['name'], QueueTest.queue1[0]['name'])
        with self.assertRaises(QueueIsEmptyError):
            self.q3.current_track

    def test_upcoming(self):
        self.assertEqual(self.q1.upcoming[0]['name'], QueueTest.queue1[1]['name'])
        self.assertEqual(self.q1.upcoming[1]['name'], QueueTest.queue1[2]['name'])
        self.q1.get_next_track()
        self.assertEqual(self.q1.upcoming[0]['name'], QueueTest.queue1[2]['name'])
        self.assertNotEqual(self.q1.upcoming[0]['name'], QueueTest.queue1[1]['name'])
        with self.assertRaises(QueueIsEmptyError):
            self.q3.upcoming

    def test_empty(self):
        self.q1.empty()
        self.assertEqual(self.q1.length, 0)
        self.assertEqual(self.q1.position, 0)

    def test_length(self):
        self.assertEqual(self.q1.length, 3)
        self.assertEqual(self.q3.length, 0)

    def test_repeat_mode_all(self):
        self.q1.set_repeat_mode('ALL')
        self.q1.position = len(self.q1._queue)
        next_track = self.q1.get_next_track()
        self.assertEqual(next_track['name'], QueueTest.queue1[0]['name'])

    def test_get_next_track(self):
        with self.assertRaises(QueueIsEmptyError):
            self.q3.get_next_track()
        
        next_track = self.q1.get_next_track()
        self.assertEqual(self.q1.position, 1)

        self.q1.position = len(self.q1._queue)
        next_track = self.q1.get_next_track()
        self.assertIsNone(next_track)

    def test_remove(self):
        with self.assertRaises(RemoveOutOfIndexError):
            self.q1.remove(255)
        with self.assertRaises(RemoveOutOfIndexError):
            self.q1.remove(-1)
        self.q1.remove(1)
        self.assertEqual(self.q1._queue[1]['name'], QueueTest.queue1[2]['name'])