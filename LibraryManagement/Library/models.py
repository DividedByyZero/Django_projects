from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    facebook_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank = True)
    def __str__(self):
        return self.user.username

class Department(models.Model):
    department_Name = models.CharField(max_length=50)
    def __str__(self):
        return self.department_Name

class Students(models.Model):
    student_id = models.CharField(primary_key=True,max_length=50)
    student_Name = models.CharField(max_length=50)
    student_Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.student_id
class Books(models.Model):
    Book_id = models.CharField(primary_key=True,max_length=50)
    Book_title = models.CharField(max_length=50)
    Book_Author = models.CharField(max_length=50)
    release_date = models.DateField()
    def __str__(self):
        return self.Book_id
class Track(models.Model):
    department_Name = models.ForeignKey(Department,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
    Book_id = models.ForeignKey(Books,on_delete=models.CASCADE)
    issue_date = models.DateField()
    def __str__(self):
        return str(self.student_id)