from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalePost


class PostCreating:

    def create_post(user, type: str, content: str, price=None, collection_point=None):
        if type == "Text":
            text_post = TextPost(user, content)
            print(user.get_name() + " published a post:\n" + '"' + text_post.text + '"\n')
            return text_post
        if type == "Image":
            image_post = ImagePost(user, content)
            print(user.get_name() + " posted a picture\n")
            return image_post
        if type == "Sale":
            sale_post = SalePost(user, content, price, collection_point)
            print(user.get_name() + " posted a product for sale:\n" +
                  "For sale! " + sale_post.details + ", price: " + str(
                sale_post.price) + ", pickup from: " + sale_post.collection_point)
            print()
            return sale_post
