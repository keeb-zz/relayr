from config import properties

import rethinkdb as r

r.connect(properties.get('RETHINK_HOST'), properties.get('RETHINK_PORT')).repl()

r.db_create('relayr').run()
r.db('relayr').table_create('requests').run()


    
