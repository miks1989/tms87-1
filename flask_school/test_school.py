from datetime import datetime
from unittest.mock import patch, MagicMock

from flask import url_for
from flask_testing import TestCase
from werkzeug.security import generate_password_hash

from flask_school.flask_school import db, app, Group


class TestViews(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        group = Group(name='name')
        db.session.add(group)

        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('flask_todo.flask_todo.get_todo_for_user')
    @patch('flask_todo.flask_todo.current_user')
    def test_read_get_group(self, mock_current_user,
                               mock_get_todo_for_user):
        app.config['LOGIN_DISABLED'] = True
        mock1, mock2 = MagicMock(), MagicMock()
        mock_get_todo_for_user.return_value = [mock1, mock2]
        response = self.client.get('/')
        mock_get_todo_for_user.assert_called_once_with(mock_current_user.id, None)
        self.assert200(response)
        self.assertEqual(self.get_context_variable('data'), [mock1, mock2])
        self.assertEqual(self.get_context_variable('user'), mock_current_user)
        self.assertEqual(self.get_context_variable('priority'), None)

