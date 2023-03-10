import pathlib

from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
from django.template.defaultfilters import slugify


def file_path(instance, file_name: str) -> str:

    # "Название класса (lower)" / "title" / "file_name"
    return "/".join([instance.__class__.__name__.lower(), instance.slug, file_name])


class DocBaseAbstract(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)



    # URL no slug = '/books/4123/update'
    # URL + slug  = '/books/python-learn-2022/update'
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    image = models.ImageField(upload_to=file_path)
    file = models.FileField(upload_to=file_path)

    class Meta:
        abstract = True
        indexes = [models.Index(fields=("created",), name="%(class)s_created_index")]





class Book(DocBaseAbstract):
    def get_absolute_url(self):
        return f"/books/{self.slug}"


class Journal(DocBaseAbstract):
    def get_absolute_url(self):
        return f"/journal/{self.slug}"


class Comics(DocBaseAbstract):
    def get_absolute_url(self):
        return f"/comics/{self.slug}"


@receiver([pre_save], sender=Comics)
@receiver([pre_save], sender=Journal)
@receiver([pre_save], sender=Book)
def create_slug(sender, instance: DocBaseAbstract, **kwargs):
    print("Создаем SLUG!")
    # Создаем SLUG
    instance.slug = slugify(
        instance.title.translate(
            str.maketrans(
                r"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                r"abvgdeejzijklmnoprstufhc4ss_y_euaABVGDEEJZIJKLMNOPRSTUFHC4SS_Y_EUA",
            )
        )
    )
    print("-"*20)


@receiver([post_save], sender=Comics)
@receiver([post_save], sender=Journal)
@receiver([post_save], sender=Book)
def clean_files(sender, instance: DocBaseAbstract, created, **kwargs):
    if not created:

        image_file = instance.image.path
        object_file = instance.file.path

        files = pathlib.Path(object_file).parent.glob("*")

        for file in files:
            if str(file.absolute()) not in [image_file, object_file]:
                file.unlink()


@receiver([pre_delete], sender=Comics)
@receiver([pre_delete], sender=Journal)
@receiver([pre_delete], sender=Book)
def delete_files(sender, instance: Book, **kwargs):
    dir_ = pathlib.Path(instance.image.path).parent
    for file in dir_.glob("*"):
        file.unlink()
    dir_.rmdir()
