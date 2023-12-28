from django.urls import path
from Library import views

urlpatterns = [
    path('',views.home,name='home'),
    path('StudentRegForm/',views.StudentReg,name='StudentRegForm'),
    path('addBook/',views.addBook,name='addBook'),
    path('borrow/',views.borrow,name='borrow'),
    path('booklist/',views.booklist,name='booklist'),
    path('editbook/<int:id>/',views.editBook,name='editBook'),
    path('deletebook/<int:idx>/',views.deleteBook,name='deleteBook'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.auth_login,name='login'),
    path('logout/',views.auth_logout,name='logout'),
]
