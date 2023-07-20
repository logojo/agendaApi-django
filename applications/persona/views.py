
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# rest framework
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .serializer import (
    PersonSerializer, 
    PersonCustomSerializer, 
    PersonSerializer2,
    PersonPaginationSerializer,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
    CountReunionSerializer
)
# #


from .models import Person, Reunion

class PersonaList(ListView):
   #model = Person
   template_name = "persona/index.html"
   context_object_name = "personas"

    #puedo usar el model para jalar los datos o usar la funcion
   def get_queryset(self):
       return Person.objects.all()
   

#respuesta json   
class PersonaApiList(ListAPIView):
   serializer_class = PersonSerializer
   pagination_class = PersonPaginationSerializer

   #serializer vinculado a un modelo pero agregandole campos que no pertenecen al modelo
   #serializer_class =  PersonSerializer2

   def get_queryset(self):
       return Person.objects.all()
   


class PersonView(TemplateView):
    template_name = "persona/lista.html"


#busqueda api json   
class PersonSearchApi(ListAPIView):
   serializer_class = PersonSerializer

   def get_queryset(self):
       kword = self.kwargs['kword']

       return Person.objects.filter(
           full_name__icontains = kword
       )
   
#Creación de registro Api
class PersonaCreate(CreateAPIView):
    serializer_class = PersonSerializer


#detalle de registro
class PersonaDetail(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() #aqui se puede realizar un filter para hacer mas eficiente la consulta


#eliminando registro
class PersonaDestroy(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 


#actualizando registro
class PersonaUpdate(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 

#actualizando registro extrayendo los datos que tenia anteriormente
class PersonaUpdateRetrieve(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all() 


#utilizando serializador que no depende de un modelo
class PersonApiListCustom(ListAPIView):
   serializer_class = PersonCustomSerializer
   def get_queryset(self):
       return Person.objects.all()
   

#utilizando serializador con relaciones
class ReunionList(ListAPIView):
   serializer_class = ReunionSerializer
   def get_queryset(self):
       return Reunion.objects.all()
   

#Utilizando SerializerMethodField para agregar una funcion dentro del resultado de la consulta
class ReunionList2(ListAPIView):
   serializer_class = ReunionSerializer2
   def get_queryset(self):
       return Reunion.objects.all()
   
#Utilizando LinkSerializer para mandar link de los campos relacionados
class ReunionListLink(ListAPIView):
   serializer_class = ReunionSerializerLink
   def get_queryset(self):
       return Reunion.objects.all()
   

class ReunionByJob(ListAPIView):
   serializer_class = CountReunionSerializer
   def get_queryset(self):
       return Reunion.objects.reuniones_by_job()