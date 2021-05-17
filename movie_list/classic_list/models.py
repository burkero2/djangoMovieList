from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Overwrites the default return value for new items, to using their own values provided above
    def __str__(self):
        return self.name