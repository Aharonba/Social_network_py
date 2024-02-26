class SocialNetwork:
    __instance = None
    __is_initialized = False

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        if self.__is_initialized:
            return
        self.__name = name
        self.__users = {}
        self.__connect = set()
        self.__user_instances = []
        self.__is_initialized = True
        print("The social network " + self.__name + " was created!")

    def sign_up(self, user: str, password: str):
        from User import User
        if 4 < len(password) < 8:
            self.__users[user] = password
            self.__connect.add(user)
            user_instance = User(user)
            self.__user_instances.append(user_instance)
            return user_instance
        else:
            return

    def get_instance(self):
        return self.__instance

    def access_permission(self, name: str, password: str):
        if self.__users[name] == password:
            return True
        else:
            return False

    def log_out(self, name: str):
        if name in self.__connect:
            self.__connect.remove(name)
            for user in self.__user_instances:
                if user.get_name() == name:
                    user.connected = False
            print(f"{name} disconnected")
        else:
            pass

    def log_in(self, name: str, password: str):
        if self.access_permission(name, password):
            self.__connect.add(name)
            for user in self.__user_instances:
                if user.get_name() == name:
                    user.connected = True
            print(f"{name} connected")

        else:
            pass

    def __str__(self):
        final_string= f"{self.__name} social network:\n"
        for user in self.__user_instances:
            final_string += f"User name: {user.get_name()}, Number of posts: {user.get_counter_post()}, Number of followers: {user.get_number_of_followers()}\n"
        return final_string
