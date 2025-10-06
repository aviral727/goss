class User:
    def __init__(self, username):
        self.username = username
        self.posts = {}  # Change to dictionary
        self.next_post_id = 1  # Track next post ID
    
    def create_post(self, content):
        post_id = self.next_post_id
        self.posts[post_id] = content
        self.next_post_id += 1
        print(f"{self.username} posted (ID {post_id}): {content}")
    
    def view_posts(self):
        if not self.posts:
            print(f"{self.username} has no posts yet.")
        else:
            print(f"\nPosts by {self.username}:")
            for post_id, post in self.posts.items():
                print(f"{post_id}. {post}")
    
    def like_post(self, author, post_id):
        if post_id in author.posts:
            print(f"{self.username} liked the post: {author.posts[post_id]}")
        else:
            print(f"Post ID {post_id} not found.")
    
    def message_user(self, other_user, message):
        print(f"{self.username} sent {message} to {other_user.username}")
