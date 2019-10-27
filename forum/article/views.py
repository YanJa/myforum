from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from block.models import Block
from utils.paginator import pagination

# Create your views here.


# 查看文章列表
def article_list(request, block_id):
    template = "article/article_list.html"
    block_id = int(block_id)
    bl = Block.objects.get(id=block_id)  # 指定版块对应的文章信息
    article_objs = Article.objects.filter(block=bl, status=0).order_by('-id')
    response = {
        "bl": bl,
        "articles": article_objs
        }
    # 返回的页面数据放在分页里面了
    page_no = int(request.GET.get('page_no', 1))
    res = pagination(article_objs, page_no)
    response.update(res)
    return render(request, template, response)


@login_required(login_url='/accounts/login/')
def article_create(request, block_id):
    template = "article/article_create.html"
    block_id = int(block_id)
    # 通过传入的block_id获取版块信息
    bl = Block.objects.get(id=block_id)
    # 请求GET方法用于获取页面将block传递给页面
    if request.method == 'GET':
        return render(request, template, {"bl": bl})
    else:
        # POST方法提交数据
        # 采用表单验证用户提交的数据
        form = ArticleForm(request.POST)
        if form.is_valid():  # 判定参数合法性
            res = Article.objects.create(block=bl, title=form.cleaned_data['title'],
                                         content=form.cleaned_data['content'],
                                         status=0)
            res.save()
            article = form.save(commit=False)  # commit决定是否写入数据库
            article.block = bl
            article.status = 0
            article.save()
            return redirect("/article/list/%d" % block_id)
        else:
            response = {
               "bl": bl,
               "form": form
            }
            return render(request, template, response)


# 文章详情页面
@login_required(login_url='/accounts/login/')
def article_detail(request, article_id):

    template = "article/article_detail.html"

    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    response = {
       "article": article
    }
    return render(request, template, response)


# 创建文章
class AticleCreateView(View):
    """
    基于类的views
    """
    def _init_data(self, block_id):
        self.template = "article/article_create.html"
        self.block_id = int(block_id)
        self.bl = Block.objects.get(id=block_id)

    def get(self, request, block_id):
        self._init_data(block_id)
        return render(request, self.template, {"bl": self.bl})

    def post(self, request, block_id):
        self._init_data(block_id)
        print(request.user.id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # 是否提交数据
            article.block = self.bl
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % self.block_id)
        else:
            response = {
                "bl": self.bl,
                "form": form
            }
            return render(request, self.template, response)


# 基于类的文章详情页
class ArticleDetailView(DetailView):
    # 模块, 定义获取哪个数据表的对象
    model = Article
    template_name = "article/article_detail.html"
    # 返回给模板的字典key名称
    context_object = "article"

