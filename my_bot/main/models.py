import os
from django.db import models

def get_upload_path(instance, filename):
    folder_name = instance.text_content.replace(" ", "_")  # Replace spaces with underscores
    return os.path.join('static', 'uploads', folder_name, filename)


class Levels(models.Model):
    text = models.CharField(max_length = 250)


    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"


class Test(models.Model):
    
    text_content = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to=get_upload_path)
    voice_file = models.FileField(upload_to=get_upload_path)
    level = models.ForeignKey(Levels, default = True,on_delete = models.CASCADE)

    def __str__(self):
        return self.text_content
    
    def save(self, *args, **kwargs):
        # Create a folder for each instance based on text_content
        folder_path = os.path.join('static', 'uploads', self.text_content.replace(" ", "_"))
        os.makedirs(folder_path, exist_ok=True)
        super().save(*args, **kwargs)
