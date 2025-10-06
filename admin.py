from user import User

class Admin(User):
    def delete_post(self, user, index):
        if 0 <= index < len(user.posts):
            deleted = user.posts.pop(index)
            print(f"Admin {self.username} deleted post: '{deleted}' from {user.username}")
        else:
            print("Invalid post index.")