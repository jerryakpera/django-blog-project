# factory-boy allows us to generate data
# pytest-cov generates testing reports to help identify missing tests

import factory
from blogger.blog.models import Post

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "test"

    is_staff = True
    is_superuser = True


# To create a factory create a class that inherits from
# factory.django.DjangoModelFactory
class PostFactory(factory.django.DjangoModelFactory):
    # Specify the model that this factory is for in the class Meta
    class Meta:
        model = Post

    slug = "x"
    title = "x"
    subtitle = "x"

    content = "x"
    status = "published"
    author = factory.SubFactory(UserFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(*extracted)
