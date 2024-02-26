from abc import ABC, abstractmethod


class Sender(ABC):

    def __init__(self):
        self._followers = set()

    def register(self, user, name_of_sender):
        self._followers.add(user)
        print(user.get_name() + " started following "+name_of_sender)

    def unregister(self, user,name_of_sender):
        self._followers.remove(user)
        print(user.get_name() + " unfollowed " + name_of_sender)



