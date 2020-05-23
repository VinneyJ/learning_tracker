from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    #Something specific learnt on Topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
        
    def __str__(self):
        if self.text[:50]:
            return f"{self.text[:50]}..."
        elif self.text != self.text[:50]:
            return self.text
        
    