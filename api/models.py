from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    role=(
        ("admin","admin"),
        ("user","user"),
    )
    Firstname=models.CharField(max_length=120,null=False)
    Lastname=models.CharField(max_length=120,null=False)
    Email_address=models.CharField(max_length=120,null=False)
    Password=models.CharField(max_length=12,null=False)
    Role=models.CharField(max_length=10,choices=role,null=False)

    def __str__(self):
        return self.Firstname+self.Lastname


class CustomerSupport(models.Model):
    user_id=models.IntegerField(null=False)
    message=models.CharField(max_length=120,null=False)
    ticket_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=120,default="Request")

    def __str__(self):
        return str(self.ticket_id)
