from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_us, name="about"),
    path('archives/', views.archives, name="archives"),
    
    path('events/', views.events, name="events"),
    path('backup-events/', views.backup_events, name="backup-events"),
    path('event/<str:pk>/', views.event, name="event"),
    path('add-event/', views.add_event, name="add-event"),
    path('edit-event/<str:pk>/', views.edit_event, name="edit-event"),
    path('delete-event/<str:pk>/', views.delete_event, name="delete-event"),
    path('restore-event/<str:pk>/', views.restore_event, name="restore-event"),
    path('restore-all-events', views.restore_all_events, name="restore-all-events"),

    path('special-orders/', views.special_orders, name="special-orders"),
    path('backup-special-orders/', views.backup_special_orders, name="backup-special-orders"),
    path('add-order/', views.add_order, name="add-order"),
    path('edit-order/<str:pk>/', views.edit_order, name="edit-order"),
    path('delete-order/<str:pk>/', views.delete_order, name="delete-order"),
    path('restore-order/<str:pk>/', views.restore_order, name="restore-order"),
    path('restore-all-orders/', views.restore_all_orders, name="restore-all-orders"),

    path('add-event-agency/<str:pk>/', views.add_event_agency, name="add-event-agency"),
    path('edit-event-agency/<str:pk>/', views.edit_event_agency, name="edit-event-agency"),
    path('delete-event-agency/<str:pk>/', views.delete_event_agency, name="delete-event-agency"),

    path('memorandums/', views.memorandums, name="memorandums"),
    path('backup-memorandums/', views.backup_memorandums, name="backup-memorandums"),
    path('add-memo/', views.add_memo, name="add-memo"),
    path('edit-memo/<str:pk>/', views.edit_memo, name="edit-memo"),
    path('delete-memo/<str:pk>/', views.delete_memo, name="delete-memo"),
    path('restore-memo/<str:pk>/', views.restore_memo, name="restore-memo"),
    path('restore-all-memos', views.restore_all_memorandums, name="restore-all-memorandums"),

    path('comm-letters/', views.comm_letters, name="comm-letters"),
    path('backup-comm-letters/', views.backup_comm_letters, name="backup-comm-letters"),
    path('add-letter/', views.add_letter, name="add-letter"),
    path('edit-letter/<str:pk>/', views.edit_letter, name="edit-letter"),
    path('delete-letter/<str:pk>/', views.delete_letter, name="delete-letter"),
    path('restore-letter/<str:pk>/', views.restore_letter, name="restore-letter"),
    path('restore-all-letters/', views.restore_all_letters, name="restore-all-letters"),

    path('moas/', views.moas, name="moas"),
    path('backup-moas/', views.backup_moas, name="backup-moas"),
    path('moa/<str:pk>/', views.moa, name="moa"),
    path('add-moa/', views.add_moa, name="add-moa"),
    path('edit-moa/<str:pk>/', views.edit_moa, name="edit-moa"),
    path('delete-moa/<str:pk>/', views.delete_moa, name="delete-moa"),
    path('restore-moa/<str:pk>/', views.restore_moa, name="restore-moa"),
    path('restore-all-moas/', views.restore_all_moas, name="restore-all-moas"),

    path('add-party/<str:pk>/', views.add_party, name="add-party"),
    path('edit-party/<str:pk>/', views.edit_party, name="edit-party"),
    path('delete-party/<str:pk>/', views.delete_party, name="delete-party"),

    path('add-signatory/<str:pk>/', views.add_signatory, name="add-signatory"),
    path('edit-signatory/<str:pk>/', views.edit_signatory, name="edit-signatory"),
    path('delete-signatory/<str:pk>/', views.delete_signatory, name="delete-signatory"),

    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),

    path('profile/', views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('edit-info/', views.edit_info, name="edit-info"),


    path('generate-reports/', views.generate_reports, name="generate-reports"),
    path('pdf-view/', views.viewpdf, name="pdf-view")
]