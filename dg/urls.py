from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import coco.urls
import data_upload.urls

from django.contrib import admin
admin.autodiscover()

from coco.data_log import send_updated_log
from coco_admin import coco_admin
from output.views import video_analytics
from static_site_views import spring_analytics
from mcoco_admin import mcoco_admin
import website_archive_urls
import deoanalytics.urls

#coco_admin.index_template = 'social_website/index.html'
#coco_admin.login_template = 'social_website/login.html'
#coco_admin.logout_template = 'social_website/home.html'
#mcoco_admin.index_template = 'social_website/index.html'
#mcoco_admin.login_template = 'social_website/login.html'
#mcoco_admin.logout_template = 'social_website/home.html'

coco_admin.index_template = 'admin/index.html'


urlpatterns = patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^login/$', 'social_website.views.login_view', {'template_name': 'social_website/login.html'}, name='signin'),
    #url(r'^signup/$', 'social_website.views.signup_view', {'template_name': 'social_website/signup.html'}, name='signup'),
    #url(r'^denied/$', 'django.views.defaults.permission_denied', {'template_name': 'social_website/403.html'}),
    #url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'social_website/password_change.html', 'post_change_redirect':'/',}, name='change_password'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    (r'^archive/', include(website_archive_urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(coco_admin.urls)),
    #url(r'^admin/', include(admin.urls)),
    (r'^mcocoadmin/', include(mcoco_admin.urls)),
    (r'^adminblog/', include(admin.site.urls)),
    (r'^data_upload/', include(data_upload.urls)),
    (r'^coco/', include(coco.urls)),
    (r'^analytics/', include('output.urls')),
    (r'^video/?$',video_analytics.video),

    (r'^get_log/?$', send_updated_log),
    # End imports from dashboard
    ##Special page.needs to be deleted
    (r'^spring/analytics/?$', spring_analytics),
    
    # Imports from farmerbook
    (r'^analytics/cocouser/',include('deoanalytics.urls')),
    (r'^coco/docs/', TemplateView.as_view(template_name='cocodoc.html')),
    

    #AJAX for Feedback
    #url(r'^feedbacksubmit_json$', 'dg.feedback_view.ajax'),
)

# Static files serving locally
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
