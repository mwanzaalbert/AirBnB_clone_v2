#!/usr/bin/python3
""" Module for testing file storage."""
import os
import unittest
import MySQLdb
from datetime import datetime
from models import storage
from models.user import User


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
class TestDBStorage(unittest.TestCase):
    """Class to test the database storage method."""

    def setUp(self):
        """Set up database connection"""
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close database connection"""
        self.cursor.close()
        self.db.close()

    def test_new_object_added_to_database(self):
        """New object is correctly added to database"""
        new_user = User(
            email='johndoe@hbtn.com',
            password='admin123',
            first_name='John',
            last_name='Doe'
        )
        self.assertFalse(new_user in storage.all().values())
        new_user.save()
        self.assertTrue(new_user in storage.all().values())
        self.cursor.execute('SELECT * FROM users WHERE id=%s', (new_user.id,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual('johndoe@hbtn.com', result[3])
        self.assertEqual('admin123', result[4])
        self.assertEqual('John', result[5])
        self.assertEqual('Doe', result[6])

    def test_object_deleted_from_database(self):
        """Object is correctly deleted from database"""
        new_user = User(
            email='johndoe@hbtn.com',
            password='admin123',
            first_name='John',
            last_name='Doe'
        )
        new_user.save()
        self.assertTrue(new_user in storage.all().values())
        obj_key = 'User.{}'.format(new_user.id)
        self.cursor.execute('SELECT * FROM users WHERE id=%s', (new_user.id,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertIn(obj_key, storage.all(User).keys())
        new_user.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())

    def test_reloading_database_session(self):
        """Tests the reloading of the database session"""
        self.cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password, '
            'first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '4447-by-me',
                str(datetime.now()),
                str(datetime.now()),
                'ben_pike@yahoo.com',
                'pass',
                'Benjamin',
                'Pike',
            ]
        )
        storage.reload()
        self.assertIn('User.4447-by-me', storage.all())
