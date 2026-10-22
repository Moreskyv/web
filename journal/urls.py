from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('students/', views.students, name='students'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('group/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('student/<int:student_id>/', views.student_detail_view, name='student_detail'),
    path('groups/add', views.GroupCreateView.as_view(), name='group_add'),
    path('students/add', views.students_add_view, name='student_add'),
    path('group/<int:pk>/edit/', views.GroupUpdateView.as_view(), name='group_edit'),
    path('group/add/', views.groups_add_view, name='group_add'),
    path('student/<int:student_id>/edit/', views.students_edit_view, name='student_edit'),
    path('group/<int:group_id>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('student/<int:pk>/delete/', views.student_delete_view, name='student_delete'),
    path('grade/add/', views.grade_add_view, name='grade_add'),
]
