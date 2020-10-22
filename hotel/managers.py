from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,
                    username,
                    tablenumber,
                    password,
                    is_staff=False,
                    is_active=True,
                    is_admin=False):
        """
        Create and save a User with the given email and passwords.
        """
        if not username:
            raise ValueError(_('The Username must be set'))
        username = self.normalize_email(username)
        user = self.model(username=username,
                          tablenumber=tablenumber,
                          password=password,
                          )
        
        username = username
        tablenumber = tablenumber
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, password, username, tablename,
                         ):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
                                username=username,
                                tablesname=tablesname,
                                password=password,
                                )
        user.staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
