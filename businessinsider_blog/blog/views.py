from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm, SearchForm
from .models import Comment
from django.db.models import Count
from django.http import Http404

# Create your views here.
def top_stories(request, populary=None, cat=None, exact_post=None, det=None):
    if det == None:
        post = Post.objects.order_by('-views')
        latest_post = post.order_by('publish')
        market_post = latest_post.filter(category_id=Category.objects.get(category_name='markets').id)
        leader_post = latest_post.filter(category_id=Category.objects.get(category_name='leaders').id)
        lifestyle_post = latest_post.filter(category_id=Category.objects.get(category_name='lifestyle').id)
        career_post = latest_post.filter(category_id=Category.objects.get(category_name='careers').id)
        temp_val = {'first_post':post[0], 'other_posts':post[1:6], 'latest_post':latest_post[:6],
                    'market_post':market_post[:3], 'leader_post':leader_post[:3], 'lifestyle_post':lifestyle_post[:3],
                    'career_post':career_post[:3]}
        return render(request, 'index.html', temp_val)
    elif det == 1:
        if cat.isnumeric():
            cat_name = Category.objects.get(id=int(cat)).category_name
            return HttpResponsePermanentRedirect(reverse('stories', args=(cat_name, exact_post)))
        else:
            post = Post.objects.get(category_id=Category.objects.get(category_name=cat).id, slug=exact_post, status='publish')
            post.views +=1
            # users_views = post.views
            # users_views+=1
            # post.views = users_views
            post.save()
            related_tags = Tag.objects.filter(post_id=post.id).values_list('tag_name', flat=True)
            saved_post = Tag.objects.filter(tag_name__in=related_tags).values_list('post_id', flat=True)
            similar_posts = Post.objects.filter(id__in=saved_post)
            print(similar_posts)
        if len(similar_posts) > 6:
            return render(request, 'story.html', {'post':post, 'group':'local', 'similar_posts':similar_posts[:6]})
        else:
            return render(request, 'story.html', {'post':post, 'group':'local', 'similar_posts':similar_posts})
    elif det == 2:
        post = Post.objects.filter(category_id=Category.objects.get(category_name=cat).id, ).order_by('-publish')
        excl_first = post[1:]
        paginator = Paginator(excl_first, 6)
        page = request.GET.get('page')
        try:
            other_posts = paginator.page(page)
        except PageNotAnInteger:
            other_posts = paginator.page(1)
        except EmptyPage:
            other_posts = paginator.page(paginator.num_pages)
        return render(request, 'category.html', {'first_post':post[0], 'post':other_posts, 'url_cat':cat})
        # except:
        #     raise Http404
    elif det == 3 or det == 4:
        success = False
        group = ''
        if det == 3:
            group = 'trending'
            post = Post.objects.get(slug=exact_post, popular=group)
        elif det == 4:
            group = 'news'
            post = Post.objects.get(slug=exact_post)
        trend = Post.objects.filter(popular='trending').exclude(id=post.id)
        users_views = post.views
        users_views += 1
        post.views = users_views
        post.save()
        all_comment = Comment.objects.filter(post=post.id).order_by('created')
        if request.method == 'POST':
            comment = CommentForm(request.POST)
            if comment.is_valid():
                input_into = comment.cleaned_data
                add_comment = Comment(comment_name=input_into['name'], comment_email=input_into['email'], comment_message=input_into['body'], post=post)
                add_comment.full_clean()
                add_comment.save()
                comment = CommentForm()
                success = True
                return render(request, 'story.html',
                              {'post': post, 'group': group, 'trend_post': trend, 'comment_to_temp': comment, 'success':success, 'all_comment':all_comment})
        else:
            comment = CommentForm()
        return render(request, 'story.html', {'post':post, 'group':group, 'trend_post':trend, 'comment_to_temp':comment, 'all_comment':all_comment, 'success':success})

post_result = []
def search_form(request):
    global post_result
    if request.POST:
        s_form = SearchForm(request.POST)
        if s_form.is_valid():
            collected = s_form.cleaned_data
            post_result = Post.objects.filter(post_body__icontains=collected['search_inpt'])
            return HttpResponseRedirect(reverse('search'))
    else:
        s_form = SearchForm()
    return render(request, 'search.html', {'form': s_form, 's_post': post_result})