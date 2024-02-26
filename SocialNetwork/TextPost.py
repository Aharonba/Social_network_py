from Post import Post


class TextPost(Post):

    def __init__(self, user, text: str):
        super().__init__(user)
        self.text = text

    def __str__(self):
        return self.get_user().get_name() + " published a post:\n" + '"' + self.text + '"\n'

