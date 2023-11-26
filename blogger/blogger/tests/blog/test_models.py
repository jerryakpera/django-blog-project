import pytest

# Allow all the classes here to access the db
pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        # Passing arguments will override the fields declared in the factories
        post = post_factory(title="test-post")

        assert post.__str__() == "test-post"
