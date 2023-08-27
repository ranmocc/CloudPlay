
#枚举
from enum import Enum
from django.db import models

class VideoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    teleplay = 'teleplay'
    variety = 'variety'
    other = 'other'
VideoType.movie.label = '电影'
VideoType.cartoon.label = '动漫'
VideoType.teleplay.label = '电视剧'
VideoType.variety.label = '综艺'
VideoType.other.label = '其他'

class FromType(Enum):
    youku = 'youku'
    tengxun = 'tengxun'
    aiqiyi = 'aiqiyi'
    bili = 'bili'
    custom = 'custom'
FromType.youku.label = '优酷'
FromType.tengxun.label = '腾讯'
FromType.aiqiyi.label = '爱奇艺'
FromType.bili.label = 'B站'
FromType.custom.label = '自制'

class National(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    america = 'america'
    other = 'other'
National.china.label = '中国'
National.japan.label = '日本'
National.korea.label = '韩国'
National.america.label = '美国'
National.other.label = '其他'

class StarIdentity(Enum):
    to_star = 'to_star'
    supporting_role = 'supporting_role'
    director = 'director'
StarIdentity.to_star.label = '主角'
StarIdentity.supporting_role.label = '配角'
StarIdentity.director.label = '导演'


class Video(models.Model):
    name = models.CharField(max_length=100,null=False)
    image = models.CharField(max_length=500,default='')
    video_type = models.CharField(max_length=50,default=VideoType.other.value)
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
        related_name='video_star',
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
        related_name='video_sub',
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
