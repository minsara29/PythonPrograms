import configparser

cfg_data = {
    'mysql': {'host': 'localhost', 'user': 'user7',
              'passwd': 's$cret', 'db': 'ydb'}
}

config = configparser.ConfigParser()
config.read_dict(cfg_data)
config.read('db.ini')

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

print(f'Host: {host}')
print(f'User: {user}')
print(f'Password: {passwd}')
print(f'Database: {db}')

