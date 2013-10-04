from config import properties

import rethinkdb as r

def check_db():
    r.connect(properties.get('RETHINK_HOST'), properties.get('RETHINK_PORT')).repl()
    
    if 'relayr' in r.db_list().run():
        return True

    return False


def create_db():
    r.connect(properties.get('RETHINK_HOST'), properties.get('RETHINK_PORT')).repl()

    r.db_create('relayr').run()
    r.db('relayr').table_create('requests').run()


    
