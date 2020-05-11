import os


class Set():
    """Sets enviromental variables."""
    os.environ["email_address_env_var"] = "example@example.com"
    os.environ["password_env_var"] = "examplePassword"


class Get():
    """Gets enviromental variables by fetching their keys"""
    email_address = os.getenv('email_address_env_var')
    email_password = os.getenv('password_env_var')
