import random
import string


def random_lower_string() -> str:
    """Generate a random lower string"""
    return "".join(random.choices(string.ascii_lowercase, k=32))
