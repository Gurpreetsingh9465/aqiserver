from django.db import models


class Aqi(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    additionalInfo = models.CharField(max_length=255,default="no info")

    def __str__(self):
        return self.additionalInfo

class Connection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    node1 = models.ForeignKey(Aqi,on_delete=models.DO_NOTHING,related_name='node_1')
    node2 = models.ForeignKey(Aqi,on_delete=models.DO_NOTHING,related_name='node_2')

