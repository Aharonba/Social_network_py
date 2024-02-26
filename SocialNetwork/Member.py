from abc import ABC, abstractmethod


class Member(ABC):

    def __init__(self):
        pass

    def follow(self, user):
        user.register(self, user.get_name())

    def unfollow(self, user):
        user.unregister(self, user.get_name())





