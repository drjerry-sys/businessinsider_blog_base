from .models import Post, Category
from .forms import SearchForm

def _values(request):
    POPULAR = ['news', 'trending', 'local', 'retail']
    categ = Category.objects.all()
    trend_post = Post.objects.filter(popular='trending')
    s_form = SearchForm()
    from_context = {'categ':categ, 'popular':POPULAR, 'trend_post':trend_post[:5], 's_form': s_form}
    return from_context