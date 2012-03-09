from django.conf.urls.defaults import *
import os.path
import account



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pdbooks/', include('pdbooks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^login$', account.login),
    (r'^logout$',account.logout),
    (r'^register$', account.register),
    (r'^thanks$',account.thanks),
    
)
