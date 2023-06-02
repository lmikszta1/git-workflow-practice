class Medication(models.Model):
    name = models.CharField()
    dose = models.CharField()
    frequency = models.IntegerField()
    warnings = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)



more models here