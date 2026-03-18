class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def set_username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    def compare_password(self, password_to_compare):
        return self.__password == password_to_compare
