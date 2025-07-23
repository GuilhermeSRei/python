# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (X self, X cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def creat_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        return msg


# c1 = Connection()
c1 = Connection.creat_with_auth('Guilherme', '1234')

# c1.set_user('Guilherme')
# c1.set_password('123')

print(Connection.log('LOG: Essa é a mensagem de log'))
print(c1.user)
print(c1.password)
