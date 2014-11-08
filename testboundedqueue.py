import boundedqueue as Q
import unittest

class TestBoundedQueue(unittest.TestCase):

    def setUp(self):
        self.my_queue = Q.BoundedQueue(50)

    def test_init_with_no_iterable(self):
        self.my_queue = Q.BoundedQueue(50)
        self.assertIsInstance(self.my_queue, Q.BoundedQueue, 'Checking if it is a boundedqueue')

    def test_init_with_iterable(self):
        self.my_queue = Q.BoundedQueue(5, [1,2,3])
        self.assertIsInstance(self.my_queue, Q.BoundedQueue, 'Checking if it is a boundedqueue')
             
    def test_is_empty_no_elements(self):
        self.assertTrue(self.my_queue.is_empty(), 'checking if is_empty works, should be true here')

    def test_is_empty_with_elements(self):
        self.my_queue.enqueue(10)
        self.assertFalse(self.my_queue.is_empty(), 'checking if is_empty works when theres an element')

    def test_is_empty_with_iterable_within_capacity(self):
        self.my_queue = Q.BoundedQueue(5, [1,2,3])
        self.assertFalse(self.my_queue.is_empty(), 'checking if is_empty works when theres an element')
        
    def test_is_empty_with_iterable_outside_capacity(self):
        self.my_queue = Q.BoundedQueue(0, [1,2,3])
        self.assertTrue(self.my_queue.is_empty(), 'checking if is_empty works when theres an element')

    def test_enqueue_within_capacity(self):
        self.my_queue.enqueue(1)
        self.assertEqual(self.my_queue.dequeue(), 1, 'checking if it added it, then dequeue it and check if it is the same value')

    def test_enqueue_outside_capacity(self):
        self.my_queue = Q.BoundedQueue(0)
        self.my_queue.enqueue(51)
        self.assertTrue(self.my_queue.is_empty(), 'nothing should have happened since it isn"t within the capacity')

    def test_enqueue_within_capacity_after_init_with_iterable(self):
        self.my_queue = Q.BoundedQueue(5, [1,2,3])
        self.my_queue.enqueue(1)
        self.assertEqual(self.my_queue.dequeue(), 1, 'checking if it added it, then dequeue it and check if it is the same value')

    def test_enqueue_outside_capacity_after_init_with_iterable(self):
        self.my_queue = Q.BoundedQueue(1, [3])
        self.my_queue.enqueue(51)
        self.assertEqual(self.my_queue.dequeue(), 3, 'nothing should have happened since it isn"t within the capacity')

    def test_dequeue_within_capacity(self):
        self.my_queue = Q.BoundedQueue(50)
        self.my_queue.enqueue(25)
        self.assertEqual(self.my_queue.dequeue(), 25, 'checking if it dequeued the right value/element')

    def test_dequeue_with_no_elements(self):
        self.my_queue = Q.BoundedQueue(50)
        self.assertRaises(IndexError, self.my_queue.dequeue)

    def test_dequeue_outside_capacity(self):
        self.my_queue = Q.BoundedQueue(1)
        self.my_queue.enqueue(20)
        self.my_queue.enqueue(55)
        self.assertEqual(self.my_queue.dequeue(), 20, 'should be 20 since enqueueing 55 doesn"t do anything')

    def test_dequeue_after_init_with_iterable_within_capacity(self):
        self.my_queue = Q.BoundedQueue(5, [1])
        self.assertEqual(self.my_queue.dequeue(), 1)

    def test_dequeue_after_init_with_iterable_outside_capacity(self):
        self.my_queue = Q.BoundedQueue(0, [1])
        self.assertRaises(IndexError, self.my_queue.dequeue)

    def test_size_with_iterable_outside_capacity(self):
        self.my_queue = Q.BoundedQueue(0, [1,2,3])
        self.assertEqual(self.my_queue.size(), 0, 'test for no elements, which is 0 size')

    def test_size_with_iterable_within_capacity(self):
        self.my_queue = Q.BoundedQueue(5, [1,2,3])
        self.assertEqual(self.my_queue.size(), 3, 'test with elements, which is 3 size')

    def test_size_with_no_elements(self):
        self.my_queue = Q.BoundedQueue(50)
        self.assertEqual(self.my_queue.size(), 0, 'test for no elements, which is 0 size')

    def test_size_with_some_elements(self):
        self.my_queue = Q.BoundedQueue(2)
        self.my_queue.enqueue(2)
        self.my_queue.enqueue(3)
        self.assertEqual(self.my_queue.size(), 2, 'should be size two since we only added two elements')

    def test_size_with_elements_over_capacity(self):
        self.my_queue = Q.BoundedQueue(2)
        self.my_queue.enqueue(2)
        self.my_queue.enqueue(3)
        self.my_queue.enqueue(55)
        self.assertEqual(self.my_queue.size(), 2, 'size should still be two since going over the capacity does not change the size')

    def test_size_after_dequeueing(self):
        self.my_queue = Q.BoundedQueue(3)
        self.my_queue.enqueue(1)
        self.my_queue.enqueue(2)
        self.my_queue.enqueue(3)
        self.my_queue.dequeue()
        self.assertEqual(self.my_queue.size(), 2, 'size should be decreased by one since we dequeued')

    
if __name__ == '__main__':
    unittest.main()
