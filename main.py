from user import User
from admin import Admin

def main():
    # Create users
    user1 = User("Aviral")
    user2 = User("Raj")
    admin = Admin("Admin")

    # User1 and User2 make posts
    user1.create_post("Hello everyone! This is my first post.")
    user2.create_post("Feeling great today!")
    user1.create_post("Learning Python OOP is fun!")
    
    # View posts
    user1.view_posts()
    user2.view_posts()
    
    # User1 likes User2's post
    user2.like_post(user1,2)

    # Admin deletes a post
    admin.delete_post(user1, 1)

    #message between users
    user1.message_user(user2, "Hey Raj, how are you?")
    
    # View again after deletion
    user1.view_posts()

if __name__ == "__main__":
    main()
