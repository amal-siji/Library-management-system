from django.urls import path
from . import views
urlpatterns = [
    # MAIN
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('popularbooks/', views.popularbooks, name='popularbooks'),

    # LIBRARIAN
    path('li_register/', views.li_register, name='li_register'),
    path('li_login', views.li_login, name='li_login'),
    path('li_index/', views.li_index, name='li_index'),
    path('li_bookadd', views.book_add, name='li_bookadd'),
    path('li_bookview/', views.book_view, name='li_bookview'),
    path('lr_bookedit/<int:id>', views.lr_bookedit, name='li_bookedit'),
    path('lr_bookdelete/<int:id>', views.lr_bookdelete, name='li_bookdelete'),
    path('li_changepass', views.lr_password_change, name='li_changepass'),
    path('li_booktaken/', views.booktaken, name='li_booktaken'),
    path('lr_delete_cu/<int:id>', views.lr_delete_cu, name='lr_delete_cu'),

    # READER
    path('cu_register/', views.cu_register, name='cu_register'),
    path('cu_login', views.cu_login, name='cu_login'),
    path('cu_profile', views.cu_profile, name='cu_profile'),
    path('cu_index/', views.cu_index, name='cu_index'),
    path('cu_changepass', views.cu_changepass, name='cu_changepass'),
    path('cu_bookview/', views.cubook_view, name='cu_bookview'),
    path('cu_rentbook/', views.cu_rent_book, name='rentbook'),
   
    # ADMIN
    path('ad_login/', views.ad_login, name='ad_login'),
    path('ad_index/', views.ad_index, name='ad_index'),
    path('ad_changepass', views.ad_changepass, name='ad_changepass'),
    path('con_peoples', views.con_peoples, name='con_peoples'),
    path('ad_delCon/<int:id>', views.ad_delCon, name='ad_delCon'),
    path('readers/', views.ad_readers, name='readers'),
    path('ad_delreaders/<int:id>', views.ad_delreaders, name='ad_delreaders'),
    path('ad_bookview/', views.ad_bookview, name='ad_bookview'), 
    path('ad_bookdelete/<int:id>', views.ad_bookdelete, name='ad_bookdelete'),
    path('ad_bookedit/<int:id>', views.ad_bookedit, name='ad_bookedit'),
    path('ad_booktaken/', views.ad_booktaken, name='ad_booktaken'),
    path('ad_booktakendel/<int:id>', views.ad_booktakendel, name='ad_booktakendel'),
    
    #messages
    path('lisendmsgs/', views.lr_send_messages, name='lisendmsg'),
    path('show_messages/', views.show_messages, name='show_messages'),      
    path('adshow_messages/', views.adshow_messages, name='adshow_messages'),  
    path('lrshow_messages/', views.lrshow_messages, name='lrshow_messages'),      
    path('sendmessages/', views.sendmessages, name='sendmessages'), 
   
  
    
]
