from django.db import models

class Place(models.Model):
	STATUS_CHOICES = (
		(1, 'Enable'),
		(0, 'Disable')
	)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
	latitude = models.CharField(max_length=120)
	longitude = models.CharField(max_length=120)

	def __str__(self):
		return "%s" % (self.id)