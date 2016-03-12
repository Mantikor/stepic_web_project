from django.conf.urls import patterns, include, url
from qa.views import list_qa, post_question, post_answer, login, new, list_popular, list_question, signup

urlpatterns = patterns('',
   url(r'^$', list_qa, name='list_qa'),
   url(r'^\?page=(?P<page>\d+)', list_qa, name='list_qa'),
   url(r'^ask/', post_question, name='post_question'),
   url(r'^answer/', post_answer, name='post_answer'),
   url(r'^login/', login, name='login'),
   url(r'^new/', new, name='new'),
   url(r'^popular/', list_popular, name='list_popular'),
   url(r'^popular/\?page=(?P<page>\d+)', list_popular, name='list_popular'),
   url(r'^question/(?P<id>\d+)/', list_question, name='list_question'),
   url(r'^signup/', signup, name='signup')
)
