from django.contrib.auth.models import BaseUserManager

class CustomUserManagar(BaseUserManager):
    def create_user(self, phone_number, last_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Telefon raqamingizni kiritishingiz kerak!')
        user = self.model(
            phone_number = phone_number,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, phone_number, password, **extra_fields):
        user = self.create_user(
            phone_number,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number,
            password,
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user