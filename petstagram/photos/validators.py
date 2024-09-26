from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_file_size(image_object):
    if image_object.size > 5242800:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')


@deconstructible    # to return in tuple with data
class FileSizeValidator:
    def __init__(self, file_size_mb, message=None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"The maximum file size that can be uploaded is {self.file_size_mb}MB"
        else:
            self.__message = value

    def __call__(self, image_object):
        if image_object.size > self.file_size_mb * 1024 * 1024:  #5242800 B
            raise ValidationError(self.message)
