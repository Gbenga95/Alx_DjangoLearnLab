📌 Views Configuration

This project uses Django REST Framework (DRF) generic views to manage posts.

PostListCreateView

URL: /posts/

Methods:

GET → Retrieve all posts

POST → Create a new post

Customization: Uses PostSerializer for validation and serialization.

PostRetrieveUpdateDestroyView

URL: /posts/<id>/

Methods:

GET → Retrieve a single post

PUT/PATCH → Update a post

DELETE → Delete a post

Customization: Uses PostSerializer for validation and serialization.

⚡ Note:
If you extend these views, you can add custom behavior using hooks such as:

perform_create(self, serializer) → to modify data before saving (e.g., attach request.user to a post).

get_queryset(self) → to filter data dynamically (e.g., only return posts owned by the current user).

Example of Custom Hook in Code
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """
        Custom hook to save the user who created the post.
        """
        serializer.save(author=self.request.user)