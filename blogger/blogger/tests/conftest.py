# This file is read by pytest before it runs any tests

# We can create test setups here
from pytest_factoryboy import register

# Register factories to use them in our tests
from .factories import PostFactory

# The registered factories can be accessed in snake case as an argument in the test functions
register(PostFactory)
