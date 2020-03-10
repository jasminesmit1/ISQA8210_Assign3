from django.db import models
from django.contrib.auth.models import AbstractUser


class Area(models.Model):
    floor_list = [("First Floor", "First Floor"), ("Second Floor", "Second Floor"),
                 ("Third Floor", "Third Floor"), ("Fourth Floor", "Fourth Floor"),
                 ("Fifth Floor", "Fifth Floor"), ("Sixth Floor", "Sixth Floor")]
    area = models.CharField(max_length=250,  blank=False, null=False)
    floor = models.CharField(max_length=250, choices=floor_list, blank=False, null=False)

    def __str__(self):
        return self.area


class User(AbstractUser):
    employ_num = models.CharField(max_length=4)

    def __str__(self):
        return self.username


class AssignedJob(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False,
                                 related_name='emplye_assigned')
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, blank=False, null=False,
                             related_name='area_assigned')
    special_instructions = models.TextField(max_length=500, blank=True, null=True,)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.area) + str(self.date)


class Task(models.Model):
    task_list = [("Sweep/Vacuum Floor", "Sweep/Vacuum Floor"), ("Mop Floor", "Mop Floor"),
                 ("Dust", "Dust"), ("Clean Windows", "Clean Windows"),("Clean Mirrors", "Clean Mirrors"),
                 ("Take out trash", "Take out trash"), ("Sanitize Bathroom", "Sanitize Bathroom"),
                 ("Change bedding", "Change bedding"), ("Wipe counters", "Wipe Counters"),
                 ("Exchange towels", "Exchange towels"), ("Arrange Furniture", "Arrange Furniture"),
                 ("Stock toiletries", "Stock toiletries"), ("Other", "Other"),
                 ]
    task = models.CharField(max_length=250, choices=task_list, blank=False, null=False, )
    done = models.BooleanField(default=False)
    job = models.ForeignKey(AssignedJob, on_delete=models.DO_NOTHING, blank=False, null=False,
                            related_name='job_assigned_to')

    def __str__(self):
        return self.task
