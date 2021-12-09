from django.db import models

# Create your models here.


# class Department:
#     dept_id integerfield
#     dept_name charfield
#     dept_head charfield


# class Student:
#     std_id integerfield
#     first_name charfield
#     last_name charfield
#     departments fk(Department)


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=128)
    dept_head = models.CharField(max_length=128)

    def __str__(self):
        return self.dept_name

    class Meta:
        db_table = 'department'


class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE)

    def _str__(self):
        return self.full_name()

    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        db_table = 'student'
