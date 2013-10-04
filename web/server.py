from app import app
from views import index
from views import sav

app.add_url_rule('/', 'index', index, methods=['GET'])
app.add_url_rule('/', 'sav', sav, methods=['POST'])


if __name__=="__main__":
    app.run('0.0.0.0')
