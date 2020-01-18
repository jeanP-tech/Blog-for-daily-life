from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth.views import LoginView, logout_then_login, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('', include('blog.urls')),
]
