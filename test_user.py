import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User
from schemas import UserCreate, UserUpdate
import crud

# Setup in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pytest fixture to provide a fresh database for each test
@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


# Test creating a new user
def test_create_user(db):
    user_data = UserCreate(username="testuser", email="test@example.com", password="secret")
    user = crud.create_user(db, user_data)
    assert user.username == "testuser"
    assert user.email == "test@example.com"


# Test retrieving a user by ID
def test_get_user(db):
    user_data = UserCreate(username="testuser2", email="user2@example.com", password="pass")
    user = crud.create_user(db, user_data)
    fetched = crud.get_user(db, user.id)
    assert fetched.username == "testuser2"


# Test updating a user's information
def test_update_user(db):
    user_data = UserCreate(username="testuser3", email="user3@example.com", password="pass")
    user = crud.create_user(db, user_data)
    update_data = UserUpdate(username="updateduser", email="updated@example.com", password="newpass")
    updated = crud.update_user(db, user.id, update_data)
    assert updated.username == "updateduser"
    assert updated.email == "updated@example.com"


# Test deleting a user
def test_delete_user(db):
    user_data = UserCreate(username="testuser4", email="user4@example.com", password="pass")
    user = crud.create_user(db, user_data)
    deleted = crud.delete_user(db, user.id)
    assert deleted.username == "testuser4"
    assert crud.get_user(db, user.id) is None


# Test retrieving a list of users
def test_get_users(db):
    users = [
        UserCreate(username=f"user{i}", email=f"user{i}@example.com", password="pass")
        for i in range(5)
    ]
    for user_data in users:
        crud.create_user(db, user_data)
    result = crud.get_users(db, skip=0, limit=10)
    assert len(result) == 5
    assert result[0].username == "user0"
