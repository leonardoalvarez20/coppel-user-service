import pendulum
from sqlalchemy import DateTime, TypeDecorator


class CustomDateTime(TypeDecorator):
    """DateTime decorator
    Returns:
        [pendulum.datetime]: datetime from string
    """

    impl = DateTime

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            return pendulum.from_format(value, "YYYY-MM-DDTHH:mm:ss.SSSSSSZ")
        return value
