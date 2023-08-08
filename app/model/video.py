
#枚举
from enum import Enum
from django.db import models

class ViedoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    teleplay = 'teleplay'
    variety = 'variety'
    other = 'other'
ViedoType.movie.lable = '电影'
ViedoType.cartoon.lable = '动漫'
ViedoType.teleplay.lable = '电视剧'
ViedoType.variety.lable = '综艺'
ViedoType.other.lable = '其他'

class FromType(Enum):
    youku = 'youku'
    custom = 'custom'
FromType.youku.lable = '优酷'
FromType.custom.lable = '自制'

class National(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    america = 'america'
    other = 'other'
National.china.lable = '中国'
National.japan.lable = '日本'
National.korea.lable = '韩国'
National.america.lable = '美国'
National.other.lable = '其他'

class Video(models.Model):
    name = models.CharField(max_length=100,null=False)
    image = models.CharField(max_length=500,default='')
    video_type = models.CharField(max_length=50,default=ViedoType.other.value)
    from_to = models.CharField(max_length=20,default=FromType.custom.value)
    nationality = models.CharField(max_length=20,default=National.other.value)
    description = models.TextField()
    status = models.BooleanField(default=True,db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name','video_type','from_to','nationality')
    def __str__(self):
        return self.name

class VideoStar(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='Video_star',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100,null=False)
    identity = models.CharField(max_length=50,default='')

    class Meta:
        unique_together = ('video','name','identity')
    def __str__(self):
        return self.name

class VideoSub(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='Video_sub',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    url = models.CharField(max_length=500,null=False)
    number = models.IntegerField(default=1)

    class Meta:
        unique_together = ('video','number')
    def __str__(self):
        return 'video:{},number:{}'.format(self.video.name,self.number)
