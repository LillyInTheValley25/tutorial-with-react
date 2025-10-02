"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import Http404, HttpResponse
import os

def serve_react_app(request, *args, **kwargs):
    """
    Serve the React app, but only for non-API routes
    """
    # Check if this is an API route that failed
    if request.path.startswith('/api/'):
        raise Http404("API endpoint not found")
    
    # Serve the React app
    try:
        index_file = os.path.join(settings.STATICFILES_DIRS[0], 'index.html')
        if os.path.exists(index_file):
            with open(index_file, 'r') as f:
                return HttpResponse(f.read(), content_type='text/html')
        else:
            return HttpResponse("React app not built. Run 'deno task build' first.", status=500)
    except Exception as e:
        return HttpResponse(f"Error serving React app: {str(e)}", status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # Serve assets from dist folder
    urlpatterns += [
        re_path(r'^assets/(?P<path>.*)$', serve, {
            'document_root': os.path.join(settings.STATICFILES_DIRS[0], 'assets'),
        }),
        # Serve other static files
        re_path(r'^(?P<path>.*\.(js|css|png|jpg|jpeg|gif|ico|svg))$', serve, {
            'document_root': settings.STATICFILES_DIRS[0],
        }),
    ]

# Catch-all for React app (must be last)
urlpatterns += [
    re_path(r'^.*$', serve_react_app, name='react-app'),
]
