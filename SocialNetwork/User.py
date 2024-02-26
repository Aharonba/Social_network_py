from Member import Member
from Sender import Sender
from PostCreating import PostCreating


class User(Sender, Member):

    def __init__(self, name: str):
        super().__init__()
        self.__name = name
        self.__notifications = []
        self.__counter_post = 0
        self.connected = True

    def publish_post(self, type: str, content: str, price= None, collection_point=None):
        if self.connected:
            post = PostCreating.create_post(self, type, content, price, collection_point)
            self.notify_member()
            self.__counter_post = self.__counter_post + 1
            return post
        else:
            pass

    def get_name(self):
        return self.__name

    def update_sender(self, user, type= str):
        if type == "like":
            self.__notifications.append(user.get_name() + " liked your post")
        if type == "comment":
            self.__notifications.append(user.get_name() + " commented on your post")

    def notify_member(self):
        for member in self._followers:
            member.__notifications.append(self.__name + " has a new post")

    def __str__(self):
        return f"User name: {self.__name}, Number of posts: {self.__counter_post}, Number of followers: {len(self._followers)}"

    def print_notifications(self):
        print(f"{self.__name}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def get_counter_post(self):
        return self.__counter_post

    def get_number_of_followers(self):
        return len(self._followers)