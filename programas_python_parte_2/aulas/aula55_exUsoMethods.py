class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        #setter -> armazena valores
        self.user = user

    def set_user(self, password):
        #setter -> armazena valores
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        return f'LOG: {msg}'

c1 = Connection()
c2 = Connection.create_with_auth('Rafael', '123')

print(vars(c1))
print(vars(c2))
print(Connection.log('Mensagem de log.'))