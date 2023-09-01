from django.db import models

class CourseMaterial(models.Model):
    LEVEL_CHOICES = (
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    )

    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='course_materials/')

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

