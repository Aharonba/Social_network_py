from Post import Post
from SocialNetwork import SocialNetwork


class SalePost(Post):

    def __init__(self, user, details: str, price: int, collection_point: str):
        super().__init__(user)
        self.details = details
        self.price = price
        self.collection_point = collection_point
        self.available = True

    def discount(self, discount: int, password: str):
        user = self.get_user()
        name = user.get_name()
        network = SocialNetwork(user)
        ans = network.access_permission(name, password)
        if ans == True:
            self.price = self.price*((100-discount)/100)
            print(f"Discount on {self.get_user().get_name()} product! the new price is: {self.price}")
        else:
            pass

    def sold(self, password: str):
        if self.available:
            user = self.get_user()
            name = user.get_name()
            network = SocialNetwork(user)
            ans = network.access_permission(name, password)
            if ans:
                self.available = False
                print(user.get_name() + "'s product is sold")
        else:
            pass

    def __str__(self):
        if self.available:
            return (self.get_user().get_name() + " posted a product for sale:\n" +
                  "For sale! "+ self.details + ", price: " + str(
                self.price) + ", pickup from: " + self.collection_point + "\n")
        else:
            return (self.get_user().get_name() + " posted a product for sale:\n" +
                    "Sold! " + self.details + ", price: " + str(
                        self.price) + ", pickup from: " + self.collection_point + "\n")



