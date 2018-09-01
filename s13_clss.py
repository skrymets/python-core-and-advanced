import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class Course(object):

    def __init__(self, title):
        object.__init__(self)
        self.__title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, t):
        self.__title = t


c = Course("Python Core and Advanced")

try:
    print(c.__title)
except AttributeError as error:
    logger.error(error)

print(c.title)
