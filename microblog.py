from app import app, db
from app.models import User, Post


'''
@app.shell_context_processor decorator registers the function as  a shell context function.
- when the flask shell command runs, it will invoke this function and register the items returned by it in the shell session
- for each item you have to provide a name which it will be referenced in the shell, which is given by dict keys
- after you add the shell context processor you can work with database entities without having to import them
- If errors, set `export FLASK_APP=microblog.py` in virtualenv
'''
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}