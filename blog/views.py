# bytebrew/blogs/views.py is part of bytebrew's site
#
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

from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost


def index(request):
    return HttpResponse("Hello! You are at the index.")


def latest(request):
    post = BlogPost.get_latest_by('date published')
    html = '\n'.join([post.post_title, post.post_text, post.post_date])
    return HttpResponse(html)
