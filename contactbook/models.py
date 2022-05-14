from django.db import models

class Contact(models.Model):  
    cid = models.CharField(max_length=20)  
    cname = models.CharField(max_length=100)  
    cemail = models.EmailField()  
    ccontact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "contact"  