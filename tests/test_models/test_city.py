#!/usr/bin/python3
import unittest
from models.city import City
import datetime

class TestCity(unittest.TestCase):

    def test_init_with_kwargs(self):
        state_id = 'test_state_id'
        name = 'test_name'
        kwargs = {'id': 'test_id', 'created_at': '2024-05-10T12:00:00', 'updated_at': '2024-05-10T13:00:00', 'state_id': state_id, 'name': name}
        obj = City(**kwargs)
        self.assertEqual(obj.id, 'test_id')
        self.assertEqual(obj.created_at, datetime.fromisoformat('2024-05-10T12:00:00'))
        self.assertEqual(obj.updated_at, datetime.fromisoformat('2024-05-10T13:00:00'))
        self.assertEqual(obj.state_id, state_id)
        self.assertEqual(obj.name, name)

    def test_str(self):
        obj = City(id='test_id', state_id='test_state_id', name='test_name')
        self.assertEqual(str(obj), "[City] (test_id) {'id': 'test_id', 'created_at': None, 'updated_at': None, 'state_id': 'test_state_id', 'name': 'test_name'}")

    def test_to_dict(self):
        created_at = datetime(2024, 5, 10, 12, 0, 0)
        updated_at = datetime(2024, 5, 10, 13, 0, 0)
        obj = City(id='test_id', created_at=created_at, updated_at=updated_at, state_id='test_state_id', name='test_name')
        expected_dict = {'id': 'test_id', 'created_at': '2024-05-10T12:00:00', 'updated_at': '2024-05-10T13:00:00', '__class__': 'City', 'state_id': 'test_state_id', 'name': 'test_name'}
        self.assertEqual(obj.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
