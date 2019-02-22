from django.shortcuts import render, redirect, get_object_or_404
from .models import Like


def post(request):
    return render(request, 'post/post.html')


# @require_POST # 해당 뷰는 POST method 만 받는다.
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Like, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create()

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message}

    return HttpResponse(json.dumps(context))