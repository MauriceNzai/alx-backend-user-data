# 0x03. User authentication service

In the industry, you should not implement your own authentication system and
 use a module or framework that doing it for you (like in Python-Flask:
 Flask-User). Here, for the learning purpose, we will walk through each step
 of this mechanism to understand it by doing.

## Resources

- [Flask documentation](https://intranet.alxswe.com/rltoken/lKExyvivrrW4eh0eI8UV6A "Flask documentation")
- [Requests module](https://intranet.alxswe.com/rltoken/py7LuuD1u2MUwcaf8wnDzQ "Requests module")
- [HTTP status codes](https://intranet.alxswe.com/rltoken/cj-mc5ZHp_KyXn1yikHC0A"HTTP status codes")

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone,
 without the help of Google:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Tasks

### 0. User model
In this task you will create a SQLAlchemy model named User for a database
 table named users (by using the [mapping declaration](https://intranet.alxswe.com/rltoken/-a69l-rGqoFdXnnu6qfKdA "mapping declaration") of SQLAlchemy).
The model will have the following attributes:
- id, the integer primary key
- email, a non-nullable string
- hashed_password, a non-nullable string
- session_id, a nullable string
- reset_token, a nullable string
