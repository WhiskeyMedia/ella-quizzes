try:
    from django.conf.urls import patterns, url
except:
    from django.conf.urls.defaults import patterns, url

from ella_quizzes.views import calculate, get_result

urlpatterns = patterns('',
    url(r'^$', calculate, name='quiz-calculate'),
    url(r'^(?P<choice>[0-9]+)/$', get_result, name='quiz-result')
)
