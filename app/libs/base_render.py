from mako.lookup import TemplateLookup  # 导入配置文件
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context  # 导入上下文
from django.http import HttpResponse

def render_to_response(request, template, data=None):
    context_instance = RequestContext(request)  # 创建上下文实例
    path = settings.TEMPLATES[0]['DIRS'][0]
    lookup = TemplateLookup(
        directories=[path],
        output_encoding='utf-8',  # 输出格式
        input_encoding='utf-8'  # 输入格式
    )
    mako_template = lookup.get_template(template)

    if not data:
        data = {}

    if context_instance:  # 如果实例存在就更新数据
        context_instance.update(data)
    else:
        context_instance = Context(data)  # 如果没有则创建实例

    result = {}

    for d in context_instance:
        result.update(d)

    # 创建csrf_token
    result['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(
        request.META['CSRF_COOKIE'])
    return HttpResponse(mako_template.render(**result))
