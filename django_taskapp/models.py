from django.db import models

class DemoModel(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField(null=True)

#demo = DemoModel(title="aaa", number=1)
#demo = DemoModel(title="aaa", number=2)
#demo = DemoModel(title="aaa", number=3)
#demo.save()