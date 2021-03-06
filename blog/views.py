# Copyright (C) 2016 Elvis M Teixeira
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.template import loader, Context
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost


def index(request):
    posts = BlogPost.objects.all()
    template = loader.get_template("blog/blogindex.html")
    context = Context({
        'page_title': 'ByteBrew',
        'posts': posts,
        'blog_index_footer': 'Copyright (C) 2016 Elvis Teixeira',
    })
    return HttpResponse(template.render(context))


def latest(request):
    return HttpResponse("<h1>The latest post!</h1>")
