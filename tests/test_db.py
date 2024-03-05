from sqlalchemy import select

from fast_zero.models import User


def test_create_new_user(session):
    new_user = User(username='John',  password='secret', email='test@example.com')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'John'))

    assert user.username == 'John'
