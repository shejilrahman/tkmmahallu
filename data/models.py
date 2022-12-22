from secrets import choice
from django.db import models
from django.contrib.auth.models import User

MAHALLU_WARD_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]
PANCHAYATH_WARD_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')]
class Family(models.Model):
    PostofficeType = models.TextChoices('Postofficetype', 'Talikulam Nattika')
    Landmarkchoice = models.TextChoices('Landmarkchoice', 'Talikulam Pallimukk Puthiyangady KunnathPally Nambikadavu Aynichod BhagavanNagar Naseeb Kakkerivalavu Kaithakal Aryampadam Ravinagar AsadNagar College Fathahpalli')
    mahallu_ward = models.CharField(max_length=5, choices=MAHALLU_WARD_CHOICES)
    mahallu_house_no= models.CharField(max_length=10)
    panchayath=models.CharField(default='Talikulam',choices=PostofficeType.choices,max_length=60)
    pachayath_ward = models.CharField(max_length=5, choices=PANCHAYATH_WARD_CHOICES)
    panchayath_house_no= models.CharField(max_length=10)
    name_of_family_head=models.CharField(max_length=60)
    son_of=models.CharField(max_length=60)
    living_from=models.IntegerField()
    address = models.CharField(max_length=60)
    landmark=models.CharField(blank=True,choices=Landmarkchoice.choices,max_length=60)
    post_office=models.CharField(default='Talikulam',choices=PostofficeType.choices,max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    
        return str(self.mahallu_ward) + '/' + str(self.mahallu_house_no) + '   ' + self.name_of_family_head


    class Meta:
        verbose_name_plural = "Families"
    
STATUS_CHOICES = [('H', 'Family Head'),
('M', 'Member'),('W','Wife'),('M','Mother'),('S','Son'),('D','Daughter'),('F','Father'),('O','Son in Law'),('A','Daughter in Law')]

class Member(models.Model):
   Choice = models.TextChoices('Choice', 'Yes No')
   Grouptype = models.TextChoices('Grouptype', 'NA A+ O+ B+ AB+ A- O- B- AB-')
   family = models.ForeignKey(Family, on_delete=models.CASCADE)
   name = models.CharField(max_length=60)
   age = models.IntegerField(blank=True,null=True)
   education = models.CharField(max_length=60,blank=True,null=True)
   job = models.CharField(max_length=60,blank=True,null=True)
   blood_group=models.CharField(default='NA',choices=Grouptype.choices,max_length=60)
   phone_number=models.CharField(blank=True,max_length=15)
   status = models.CharField(max_length=5,default='M', choices=STATUS_CHOICES)
   remarks=models.CharField(max_length=300,blank=True,null=True)
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   Required_help_for_marriage=models.CharField(default='No',choices=Choice.choices,max_length=4)
   Required_help_for_building_home=models.CharField(default='No',choices=Choice.choices,max_length=4)
   Required_any_other_financial_help=models.CharField(default='No',choices=Choice.choices,max_length=4)
   remarks=models.CharField(max_length=300,blank=True,null=True)
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   
   def __str__(self):
        return self.name