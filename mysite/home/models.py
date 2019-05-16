from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    Id = models.BigAutoField(null=False,blank=False, primary_key=True)
    CategoryName = models.CharField(null=False,blank=False, max_length=100)
    Level = models.IntegerField()
    CreatedBy = models.BigIntegerField(null=False, blank=False)
    CreatedTime = models.DateTimeField(null=False, blank=False, default=timezone.now)
    ModifiedBy = models.BigIntegerField()
    ModifiedTime = models.DateTimeField(default=timezone.now)
    IsDeleted = models.BooleanField()
    DeletedBy = models.BigIntegerField(null=True,blank=True)
    DeletedTime = models.DateTimeField(default=timezone.now)
    Status = models.BooleanField(null=False,blank=False)

    def __str__(self):
        return self.CategoryName

class Post(models.Model):
    Id = models.BigAutoField(null=False,blank=False, primary_key=True)
    CategoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title = models.CharField(null=False,blank=False, max_length=100)
    Content = models.TextField(null=False,blank=False)
    Summary = models.TextField(null=False,blank=False, max_length=300)
    Resource = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to="gallery")
    View = models.BigIntegerField(default=0)
    Tags = models.CharField(max_length=500, null=False, blank=False,default='netnews')
    PostStatus = models.SmallIntegerField(default=1)
    CreatedBy = models.BigIntegerField(null=False, blank=False)
    CreatedTime = models.DateTimeField(null=False, blank=False, default=timezone.now)
    ModifiedBy = models.BigIntegerField()
    ModifiedTime = models.DateTimeField(default=timezone.now)
    IsDeleted = models.BooleanField()
    DeletedBy = models.BigIntegerField()
    DeletedTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Id)

    class Meta:
        ordering = ('Id',)





