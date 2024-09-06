from django.db import models


class Menu(models.Model):
    title = models.CharField(verbose_name="Название меню", max_length=255, unique=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
