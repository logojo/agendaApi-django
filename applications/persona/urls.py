from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('', views.PersonaList.as_view(), name='home'),
    path('lista', views.PersonView.as_view(), name='lista'),

    #urls para apirest
    path('api/personas', views.PersonaApiList.as_view()),
    path('api/personas/create', views.PersonaCreate.as_view()),
    path('api/personas/detail/<pk>', views.PersonaDetail.as_view(), name='person-detail'),#show
    path('api/personas/delete/<pk>', views.PersonaDestroy.as_view()),
    path('api/personas/update/<pk>', views.PersonaUpdate.as_view()),
    path('api/personas/update-retrieve/<pk>', views.PersonaUpdateRetrieve.as_view()),
    path('api/persona/search/<kword>', views.PersonSearchApi.as_view()),

    #urls para serializer que no depende de un modelo
    path('api/personas-custom', views.PersonApiListCustom.as_view()),


    path('api/reuniones', views.ReunionList.as_view()),
    path('api/reuniones2', views.ReunionList2.as_view()),
    path('api/reuniones-link', views.ReunionListLink.as_view()),
    path('api/reunion-by-job', views.ReunionByJob.as_view()),
]