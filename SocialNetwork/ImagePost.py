from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImagePost(Post):

    def __init__(self, user, image_route: str):
        super().__init__(user)
        self.image_route = image_route

    def __str__(self):
        return f"{self.get_user().get_name()} posted a picture\n"

    def display(self):
        print("Shows picture")
        img = mpimg.imread(self.image_route)
        plt.imshow(img)
        plt.show()
