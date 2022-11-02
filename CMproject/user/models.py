from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class CustomUser(AbstractUser):
    
    cpf = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    nome_completo = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.cpf

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, cpf, telefone, nome_completo):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, cpf=cpf, telefone=telefone, nome_completo=nome_completo)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, cpf=None, telefone=None, nome_completo=None):
        return self._create_user(email, password, cpf, telefone, nome_completo)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.user.cpf


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()