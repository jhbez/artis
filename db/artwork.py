
class Artwork(object):
    id = None
    name = None
    def __str__(self):
        return("Id:{} Name:{}".format(
            self.id,
            self.name
        ))
    def to_dict(self):
        return self.__dict__