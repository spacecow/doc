import sqlite3
from collections import namedtuple
Link = namedtuple('Link',['id','url'])

db = sqlite3.connect(':memory:')
db.execute('create table links (id integer, url text)')
db.execute('insert into links values (?,?)',Link(1,'google.com'))
cursor = db.execute('select url from links')
for link_tuple in cursor:
  print link_tuple #--> (u'google.com',)
cursor = db.execute('select * from links')
print Link(*cursor.fetchone()).url #--> google.com
