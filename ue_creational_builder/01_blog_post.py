# Building a Simple Blog Post
# Create a builder pattern to construct a blog post with a title, a list of tags, and content.
# # Use fluent interface methods for setting each part of the blog post.




if __name__ == '__main__':
    blog_builder = BlogPostBuilder()
    blog_post = blog_builder.set_title("My Journey with Design Patterns")\
                            .add_tag("Software Engineering")\
                            .add_tag("Education")\
                            .set_content("Today, I explored various design patterns...")\
                            .build()
    print(blog_post)
