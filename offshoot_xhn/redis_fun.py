import redis
conn = redis.StrictRedis(
    host = 'localhost',
    port = 6379,
    password = '19971202xhn',
    ssl = True,
    ssl_ca_certs = '/etc/ssl/certs/ACCVRAIZ1.pem'
)
conn.ping()
print('connected')
conn.set('xhn','future is full of hope')