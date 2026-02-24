from django.db import models
import string
import random

class URL(models.Model):
    original_url=models.URLField(max_length=500)
    short_code=models.CharField(max_length=10,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
    def save(self,*args,**kwargs):
        if not self.short_code:
            characters=string.ascii_letters+string.digits
            self.short_code=''.join(random.choice(characters)for _ in range(6))
            super().save(*args,**kwargs)