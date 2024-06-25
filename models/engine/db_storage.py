#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place, place_amenity
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    """A database storage engine object.

    Attributes_:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    DB_CLASSES = [User, State, City, Amenity, Place, Review]

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.
        Return_:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        queries = dict()

        if cls:
            query = self.__session.query(cls).all()

            for q in query:
                key = '{}.{}'.format(q.__class__.__name__, q.id)
                queries[key] = q

        else:
            for class_type in self.DB_CLASSES:
                query = self.__session.query(class_type).all()
                for q in query:
                    key = '{}.{}'.format(q.__class__.__name__, q.id)
                    queries[key] = q

        return queries

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        curr_session = scoped_session(session_factory)

        self.__session = curr_session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
