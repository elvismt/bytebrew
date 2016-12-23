# bytebrew/blog/models.py is part of bytebrew's site
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

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title
