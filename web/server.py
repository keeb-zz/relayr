from app import app
from views import index
from views import sav
from init.first import check_db
from init.first import create_db

app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/', 'sav', sav, methods=['POST'])


if __name__=="__main__":
    # check to see if the relayr database is set up..
    if not check_db():
        create_db()

    app.run('0.0.0.0')
