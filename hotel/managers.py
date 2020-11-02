from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of staffnames.
    """
    def create_user(self,
                    staffname,
                    tablename,
                    password,
                    is_staff=False,
                    is_active=True,
                    is_admin=False):
        """
        Create and save a User with the given email and passwords.
        """
        if not staffname:
            raise ValueError(_('The staffname must be set'))
        staffname = self.normalize_email(staffname)
        user = self.model(staffname=staffname,
                          tablename=tablename,
                          password=password,
                          )
        
        staffname = staffname
        tablename = tablename
        user.set_password(password)
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_superuser(self, password, staffname, tablename,
                         ):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
                                staffname=staffname,
                                tablename=tablename,
                                password=password,
                                )
        user.staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
