from django.db import models
from Profile.models import User
# Create your models here.
class Task(models.Model):
    status_choices=[('c','Completed'),('p','Pending'),('I','In Progress')]
    name=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=1,choices=status_choices)
    fnished_date=models.DateField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name