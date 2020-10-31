from django.db import models
import datetime
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class place(models.Model):
    CITY_CHOICES = (
    ('杭州', (
            ('yhq', '余杭区'),
            ('xsq', '萧山区'),
            ('bjq', '滨江区'),
            ('xhq', '西湖区'),
            ('gsq', '拱墅区'),
            ('jgq', '江干区'),
            ('xcq', '下城区'),
            ('scq', '上城区'),    
        )
    ),
    ('嘉兴', (
            ('hn', '海宁市'),
            ('tx', '桐乡市'),
            ('hy', '海盐县'),
            ('ph', '平湖市'),
            ('js', '嘉善县'),
            ('nhq', '南湖区'),
            ('xzq', '秀洲区'),      
        )
    ),
    ('湖州', (
            ('dq', '德清县'),
            ('nxq', '南浔区'),
            ('wxq', '吴兴区'),
            ('cx', '长兴县'),      
        )
    ),
    ('苏州', (
            ('wjq', '吴江区'),
        )
    ),
    ('绍兴', (
            ('vhs', '越城区'),
            ('dvd', '柯桥区'),
            ('syq', '上虞区'),
        )
    ),
    ('上海', (
            ('jsq', '金山区'),
        )
    ),
)
    city = models.CharField(
        max_length=3,
        choices=CITY_CHOICES,
        default='hn',
    )

    date = models.DateField("Date", default=datetime.date.today)
    destination = models.CharField(verbose_name='Destination', max_length=200)
    address = models.CharField(verbose_name='Address', max_length=500, blank=True, null=True)

    rating = models.IntegerField(
        default = 7,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        verbose_name='rating')

    tags = TaggableManager(verbose_name='Tags', blank=True)

    notes =  models.TextField(verbose_name='Notes',  blank=True, null=True)


    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = verbose_name
        ordering = ("-date",)

    def __str__(self):
        return '{} - {} in {} from {}'.format(self.destination, self.address, self.city, self.date)
