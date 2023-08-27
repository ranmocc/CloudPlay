
from django.views.generic import View
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth
from django.shortcuts import redirect,reverse
from app.model.video import Video,VideoStar,VideoSub,FromType,VideoType,National
from datetime import datetime

class OtherVideo(View):
    TEMPLATE = 'dashboard/video/other_video.html'
    @dashboard_auth
    def get(self,request):
        error = request.GET.get('error','')
        data = {'error':error}
        videos = Video.objects.exclude(from_to=FromType.custom.value)
        #处理video的time格式
        for i in videos:
            i.created_time = i.created_time.strftime('%Y-%m-%d %H:%M:%S')
            i.updated_time = i.updated_time.strftime('%Y-%m-%d %H:%M:%S')
            print(i.created_time)
            print(i.updated_time)
        data['videos'] = videos

        # 调试查看输出08-16
        # print('-------------sssss---------------------')
        print(datetime.now())
        # print('---------aaaa-----------')

        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request):
        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        description = request.POST.get('description')

        if not all([name,image,video_type,from_to,nationality,description]):
            return redirect('{}?error={}'.format(reverse('other_video'),'缺少字段，请您仔细检查一下'))

        Video.objects.create(
            name=name,
            image=image,
            video_type=video_type,
            from_to=from_to,
            nationality=nationality,
            description=description
        )

        return redirect(reverse('other_video'))

class VideoSubUrl(View):
    TEMPLATE = 'dashboard/video/video_sub.html'
    @dashboard_auth
    def get(self,request,video_id):
        print(video_id,"----sssss-------")
        video = Video.objects.get(pk=video_id)
        data = {}
        data['video'] = video
        print(video)

        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request,video_id):
        url = request.POST.get('url')

        video = Video.objects.get(pk=video_id)

        length = video.video_sub.count()

        print("--------aaaaaaaaaaa-----")
        print(length)
        try:
            VideoSub.objects.create(
                url=url,
                number=length+1,
                video_id=video_id
            )
        except:
            return redirect(reverse('video_sub',kwargs={'video_id':video_id}))

        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))

class VideoSubStar(View):
    def post(self,request):
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        video_id = request.POST.get('video_id')

        print(name,identity,video_id)

        path_format = '{}'.format(reverse('video_sub',kwargs={'video_id':video_id}))
        if not all([name,identity,video_id]):
            return redirect('{}?error={}'.format(path_format,'缺少必要字段'))

        video = Video.objects.get(pk=video_id)
        # 捕获异常
        try:
            VideoStar.objects.create(
                video=video,
                name=name,
                identity=identity
            )
        except:
            # print('创建失败')
            return redirect('{}?error={}'.format(path_format,'创建失败'))

        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))

class StarDelete(View):
    def get(self,request,star_id,video_id):
        VideoStar.objects.filter(id=star_id).delete()
        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))