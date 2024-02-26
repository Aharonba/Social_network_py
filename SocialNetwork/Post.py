from abc import ABC, abstractmethod


class Post(ABC):

    def __init__(self, user):
        from User import User
        self.__comments = {}
        self.__like = set()
        self.__user: User = user

    def like(self, user):
        if user.connected:
            self.__like.add(user)
            if self.get_user() == user:
                pass
            else:
                print(f"notification to {self.__user.get_name()}: {user.get_name()} liked your post")
                self.__user.update_sender(user, "like")
        else:
            pass

    def comment(self, user, comment: str):
        if user.connected:
            self.__comments[user] = comment
            if self.get_user() == user:
                pass
            else:
                print(f"notification to {self.__user.get_name()}: {user.get_name()} commented on your post: {comment}")
                self.__user.update_sender(user, "comment")
        else:
            pass

    def get_user(self):
        return self.__user

    def __str__(self):
        pass
