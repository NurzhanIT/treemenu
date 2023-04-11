from django.db import models


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=15, blank=True, null=False)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class MenuListItem(models.Model):
    name = models.CharField(max_length=25, blank=True, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=0)
    path = models.CharField(max_length=255, blank=True, null=False, unique=True)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.name
