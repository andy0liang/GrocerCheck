from django.db import models
from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# Create your models here.

class ad_placement(models.Model):
    ad_blurb = models.TextField(max_length=10000)
    ad_img_src = models.CharField(max_length=300)
    # ad_local_img = models.ImageField(storage = FileSystemStorage(location=settings.MEDIA_ROOT))
    ad_link = models.CharField(max_length=1000)
    ad_timestamp = models.DateTimeField()
    ad_city = models.CharField(max_length=300)

class blog_entry(models.Model):
    title = models.CharField(max_length=500)
    author_name = models.CharField(max_length=100)
    author_blurb = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    content = models.TextField(max_length=40000)
    image_blurb = models.CharField(max_length=500)
    article_sources = models.CharField(max_length=10000)
    article_timestamp = models.DateTimeField()

class Store(models.Model):
    ''' MODEL REPRESENTING A GROCERY STORE '''
    name = models.CharField(max_length=100)
    place_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    lat = models.CharField(max_length=10)
    lng = models.CharField(max_length=10)
    monhours = models.CharField(max_length=100, null=True, blank=True)
    tuehours = models.CharField(max_length=100, null=True, blank=True)
    wedhours = models.CharField(max_length=100, null=True, blank=True)
    thuhours = models.CharField(max_length=100, null=True, blank=True)
    frihours = models.CharField(max_length=100, null=True, blank=True)
    sathours = models.CharField(max_length=100, null=True, blank=True)
    sunhours = models.CharField(max_length=100, null=True, blank=True)
    live_busyness = models.IntegerField(null=True)
    keywords = models.CharField(max_length=2000, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    mon00 = models.IntegerField(null=True)
    mon01 = models.IntegerField(null=True)
    mon02 = models.IntegerField(null=True)
    mon03 = models.IntegerField(null=True)
    mon04 = models.IntegerField(null=True)
    mon05 = models.IntegerField(null=True)
    mon06 = models.IntegerField(null=True)
    mon07 = models.IntegerField(null=True)
    mon08 = models.IntegerField(null=True)
    mon09 = models.IntegerField(null=True)
    mon10 = models.IntegerField(null=True)
    mon11 = models.IntegerField(null=True)
    mon12 = models.IntegerField(null=True)
    mon13 = models.IntegerField(null=True)
    mon14 = models.IntegerField(null=True)
    mon15 = models.IntegerField(null=True)
    mon16 = models.IntegerField(null=True)
    mon17 = models.IntegerField(null=True)
    mon18 = models.IntegerField(null=True)
    mon19 = models.IntegerField(null=True)
    mon20 = models.IntegerField(null=True)
    mon21 = models.IntegerField(null=True)
    mon22 = models.IntegerField(null=True)
    mon23 = models.IntegerField(null=True)
    tue00 = models.IntegerField(null=True)
    tue01 = models.IntegerField(null=True)
    tue02 = models.IntegerField(null=True)
    tue03 = models.IntegerField(null=True)
    tue04 = models.IntegerField(null=True)
    tue05 = models.IntegerField(null=True)
    tue06 = models.IntegerField(null=True)
    tue07 = models.IntegerField(null=True)
    tue08 = models.IntegerField(null=True)
    tue09 = models.IntegerField(null=True)
    tue10 = models.IntegerField(null=True)
    tue11 = models.IntegerField(null=True)
    tue12 = models.IntegerField(null=True)
    tue13 = models.IntegerField(null=True)
    tue14 = models.IntegerField(null=True)
    tue15 = models.IntegerField(null=True)
    tue16 = models.IntegerField(null=True)
    tue17 = models.IntegerField(null=True)
    tue18 = models.IntegerField(null=True)
    tue19 = models.IntegerField(null=True)
    tue20 = models.IntegerField(null=True)
    tue21 = models.IntegerField(null=True)
    tue22 = models.IntegerField(null=True)
    tue23 = models.IntegerField(null=True)
    wed00 = models.IntegerField(null=True)
    wed01 = models.IntegerField(null=True)
    wed02 = models.IntegerField(null=True)
    wed03 = models.IntegerField(null=True)
    wed04 = models.IntegerField(null=True)
    wed05 = models.IntegerField(null=True)
    wed06 = models.IntegerField(null=True)
    wed07 = models.IntegerField(null=True)
    wed08 = models.IntegerField(null=True)
    wed09 = models.IntegerField(null=True)
    wed10 = models.IntegerField(null=True)
    wed11 = models.IntegerField(null=True)
    wed12 = models.IntegerField(null=True)
    wed13 = models.IntegerField(null=True)
    wed14 = models.IntegerField(null=True)
    wed15 = models.IntegerField(null=True)
    wed16 = models.IntegerField(null=True)
    wed17 = models.IntegerField(null=True)
    wed18 = models.IntegerField(null=True)
    wed19 = models.IntegerField(null=True)
    wed20 = models.IntegerField(null=True)
    wed21 = models.IntegerField(null=True)
    wed22 = models.IntegerField(null=True)
    wed23 = models.IntegerField(null=True)
    thu00 = models.IntegerField(null=True)
    thu01 = models.IntegerField(null=True)
    thu02 = models.IntegerField(null=True)
    thu03 = models.IntegerField(null=True)
    thu04 = models.IntegerField(null=True)
    thu05 = models.IntegerField(null=True)
    thu06 = models.IntegerField(null=True)
    thu07 = models.IntegerField(null=True)
    thu08 = models.IntegerField(null=True)
    thu09 = models.IntegerField(null=True)
    thu10 = models.IntegerField(null=True)
    thu11 = models.IntegerField(null=True)
    thu12 = models.IntegerField(null=True)
    thu13 = models.IntegerField(null=True)
    thu14 = models.IntegerField(null=True)
    thu15 = models.IntegerField(null=True)
    thu16 = models.IntegerField(null=True)
    thu17 = models.IntegerField(null=True)
    thu18 = models.IntegerField(null=True)
    thu19 = models.IntegerField(null=True)
    thu20 = models.IntegerField(null=True)
    thu21 = models.IntegerField(null=True)
    thu22 = models.IntegerField(null=True)
    thu23 = models.IntegerField(null=True)
    fri00 = models.IntegerField(null=True)
    fri01 = models.IntegerField(null=True)
    fri02 = models.IntegerField(null=True)
    fri03 = models.IntegerField(null=True)
    fri04 = models.IntegerField(null=True)
    fri05 = models.IntegerField(null=True)
    fri06 = models.IntegerField(null=True)
    fri07 = models.IntegerField(null=True)
    fri08 = models.IntegerField(null=True)
    fri09 = models.IntegerField(null=True)
    fri10 = models.IntegerField(null=True)
    fri11 = models.IntegerField(null=True)
    fri12 = models.IntegerField(null=True)
    fri13 = models.IntegerField(null=True)
    fri14 = models.IntegerField(null=True)
    fri15 = models.IntegerField(null=True)
    fri16 = models.IntegerField(null=True)
    fri17 = models.IntegerField(null=True)
    fri18 = models.IntegerField(null=True)
    fri19 = models.IntegerField(null=True)
    fri20 = models.IntegerField(null=True)
    fri21 = models.IntegerField(null=True)
    fri22 = models.IntegerField(null=True)
    fri23 = models.IntegerField(null=True)
    sat00 = models.IntegerField(null=True)
    sat01 = models.IntegerField(null=True)
    sat02 = models.IntegerField(null=True)
    sat03 = models.IntegerField(null=True)
    sat04 = models.IntegerField(null=True)
    sat05 = models.IntegerField(null=True)
    sat06 = models.IntegerField(null=True)
    sat07 = models.IntegerField(null=True)
    sat08 = models.IntegerField(null=True)
    sat09 = models.IntegerField(null=True)
    sat10 = models.IntegerField(null=True)
    sat11 = models.IntegerField(null=True)
    sat12 = models.IntegerField(null=True)
    sat13 = models.IntegerField(null=True)
    sat14 = models.IntegerField(null=True)
    sat15 = models.IntegerField(null=True)
    sat16 = models.IntegerField(null=True)
    sat17 = models.IntegerField(null=True)
    sat18 = models.IntegerField(null=True)
    sat19 = models.IntegerField(null=True)
    sat20 = models.IntegerField(null=True)
    sat21 = models.IntegerField(null=True)
    sat22 = models.IntegerField(null=True)
    sat23 = models.IntegerField(null=True)
    sun00 = models.IntegerField(null=True)
    sun01 = models.IntegerField(null=True)
    sun02 = models.IntegerField(null=True)
    sun03 = models.IntegerField(null=True)
    sun04 = models.IntegerField(null=True)
    sun05 = models.IntegerField(null=True)
    sun06 = models.IntegerField(null=True)
    sun07 = models.IntegerField(null=True)
    sun08 = models.IntegerField(null=True)
    sun09 = models.IntegerField(null=True)
    sun10 = models.IntegerField(null=True)
    sun11 = models.IntegerField(null=True)
    sun12 = models.IntegerField(null=True)
    sun13 = models.IntegerField(null=True)
    sun14 = models.IntegerField(null=True)
    sun15 = models.IntegerField(null=True)
    sun16 = models.IntegerField(null=True)
    sun17 = models.IntegerField(null=True)
    sun18 = models.IntegerField(null=True)
    sun19 = models.IntegerField(null=True)
    sun20 = models.IntegerField(null=True)
    sun21 = models.IntegerField(null=True)
    sun22 = models.IntegerField(null=True)
    sun23 = models.IntegerField(null=True)

    def __str__(self):
        return self.name


