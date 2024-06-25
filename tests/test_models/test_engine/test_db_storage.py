#!/usr/bin/python3
""" Module for testing file storage."""

# Import necessary modules
from datetime import datetime
import os
import unittest
import MySQLdb
from models import storage
from models.user import User
from models.engine.db_storage import DBStorage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
class TestDBStorage(unittest.TestCase):
    """ Class to test the database storage method """

    # Helper method for setting up database connection
    def setUp(self):
        self.db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        self.cursor = self.db.cursor()

    # Helper method for tearing down database connection
    def tearDown(self):
        """Close database connection."""
        self.cursor.close()
        self.db.close()

    # Test new object creation to database
    def test_new(self):
        """New object is correctly added to database."""
        new = User(
            email='johndoe@hbtn.com',
            password='admin123',
            first_name='John',
            last_name='Doe'
        )
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())

        self.cursor.execute('SELECT * FROM users WHERE id=%s', (new.id,))
        result = self.cursor.fetchone()
        self.cursor.close()

        self.assertTrue(result is not None)
        self.assertIsNotNone(result)
        self.assertEqual('johndoe@hbtn.com', result[3])
        self.assertEqual('admin123', result[4])
        self.assertEqual('John', result[5])
        self.assertEqual('Doe', result[6])

    # Test object deletion from database
    def test_delete(self):
        """Object is correctly deleted from database."""
        new = User(
            email='johndoe@hbtn.com',
            password='admin123',
            first_name='John',
            last_name='Doe'
        )
        new.save()

        obj_key = 'User.{}'.format(new.id)
        self.assertTrue(new in storage.all().values())

        self.cursor.execute('SELECT * FROM users WHERE id=%s', (new.id,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertIn(obj_key, storage.all(User).keys())

        new.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())

    # Test reloading of the database session
    def test_reload(self):
        """Test the reloading of the database session."""
        self.cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '007-agent',
                str(datetime.now()),
                str(datetime.now()),
                'jamesbond@casinoroyale.com',
                'bond',
                'James',
                'Bond',
            ]
        )

        self.cursor.close()

        self.assertNotIn('User.007-agent', storage.all())
        self.db.commit()
        storage.reload()
        self.assertIn('User.007-agent', storage.all())

    # Test object saving to database
    def test_save(self):
        new = User(
            email='johndoe@hbtn.com',
            password='admin123',
            first_name='John',
            last_name='Doe'
        )

        self.cursor.execute('SELECT COUNT(*) FROM users')
        old_count = self.cursor.fetchall()[0][0]
        self.cursor.close()

        new.save()

        self.cursor.execute('SELECT COUNT(*) FROM users')
        new_count = self.cursor.fetchall()[0][0]
        self.cursor.close()

        self.assertEqual(new_count, old_count + 1)

    # Test storage variable creation
    def test_storage_var_created(self):
        """Test type of Storage object created."""
        self.assertEqual(type(storage), DBStorage)

    # Test new and save methods
    def test_new_and_save(self):
        """Create and save new data entry."""
        new = User(
            first_name='nick',
            last_name='fury',
            email='nickfury@marvel.com',
            password='marvels'
        )

        self.cursor.execute('SELECT COUNT(*) FROM users')
        old_count = self.cursor.fetchall()[0][0]
        self.cursor.close()

        new.save()

        self.cursor.execute('SELECT COUNT(*) FROM users')
        new_count = self.cursor.fetchall()[0][0]
        self.cursor.close()

        self.assertEqual(new_count, old_count + 1)
