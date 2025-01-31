from django.contrib import admin
from django.urls import path, include  # Include function is required
import debug_toolbar
import blog.views
from django.conf import settings  # Import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index, name="blog-index"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip, name="get-ip"),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
