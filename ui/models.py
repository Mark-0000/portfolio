from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100, default='#', blank=True)
    image = models.ImageField(default='default.jpg', upload_to='project_images')
    technology = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} - {self.technology}'

    def save(self, **kwargs):
        super(Project, self).save(**kwargs)
        gallery = Gallery(project=self)
        gallery.save()


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    txt1 = models.CharField(max_length=100, blank=True, default='NULL')
    img1 = models.ImageField(default='default.jpg', upload_to='gallery_images')
    txt2 = models.CharField(max_length=100, blank=True, default='NULL')
    img2 = models.ImageField(default='default.jpg', upload_to='gallery_images')
    txt3 = models.CharField(max_length=100, blank=True, default='NULL')
    img3 = models.ImageField(default='default.jpg', upload_to='gallery_images')
    txt4 = models.CharField(max_length=100, blank=True, default='NULL')
    img4 = models.ImageField(default='default.jpg', upload_to='gallery_images')
    txt5 = models.CharField(max_length=100, blank=True, default='NULL')
    img5 = models.ImageField(default='default.jpg', upload_to='gallery_images')
    txt6 = models.CharField(max_length=100, blank=True, default='NULL')
    img6 = models.ImageField(default='default.jpg', upload_to='gallery_images')

    def __str__(self):
        return f'{self.project} - {self.txt1}'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.percentage}%'


class Service(models.Model):
    icon = models.CharField(max_length=100, default='fa fa-', blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.icon}'
