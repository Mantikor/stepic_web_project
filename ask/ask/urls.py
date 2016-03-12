from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^', include('qa.urls')),
    
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'qa.views.list_question'),
    # url(r'^login/', 'qa.views.login'),
    # url(r'^signup', 'qa.views.signup'),
    # url(r'^question/(?P<slug>\w+)/$', 'qa.views.show_question'),
    # url(r'^ask/', 'qa.views.post_question'),
    # url(r'^popular/', 'qa.views.list_popular'),
    # url(r'^new/', 'qa.views.test'),
    # url(r'^answer/', 'qa.views.post_answer')
)
