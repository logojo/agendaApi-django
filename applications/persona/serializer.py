from rest_framework import serializers, pagination

from .models import Person, Hobby, Reunion

class HobbySerializer(serializers.ModelSerializer):
     class Meta:
        model = Hobby
        fields = (
            'id',
            'hobby',
        ) 

class PersonSerializer(serializers.ModelSerializer):
    #Extraccion de datos cuando existen relacon ManyToMany
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        #se puede usar el   fields = ('__all__') para indicar todos los campos del modelo
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies'
        )

#serializador que no este vinculado a un modelo
class PersonCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()    
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False, )# default=False esto permite decirle al serializador que el atributo no es obligatorio



#serializer vinculado a un modelo pero agregandole campos que no pertenecen al modelo
class PersonSerializer2(serializers.ModelSerializer):
    
    #este campo puede ser usando cuando se requiere que dependiendo del valor de este campo se realice una cosa u otra en la base de datos
    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')
        


class PersonPaginationSerializer(pagination.PageNumberPagination):
   page_size = 3
   max_page_size = 100


# serializador con relaciones
class ReunionSerializer(serializers.ModelSerializer): 
    #con esto el serializador me extrara todos los datos que se allan definido en el serializador de persona y no solo el id relacionado
    persona = PersonSerializer()

    #agregando campo que viene de la funcion en el manager
    cantidad = serializers.IntegerField(required=False)
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'persona',
            'cantidad'
        ) 


class ReunionSerializer2(serializers.ModelSerializer):   

    #agregar atributo no existente en el modelo que sea resultado de la suma o combinacion de campos del modelo
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'persona',
            'fecha_hora'
        ) 

    #metodo que utilizara el serializers.SerializerMethodField()
    #el obj hace referencia a cada uno de los elementos del JSON, es devir esta funcion recorrera cada elemento y realizara la función
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)
    

#Utilizando HyperlinkedModelSerializer para mandar link de los campos relacionados
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'persona'
        ) 

        extra_kwargs = {
            'persona': {
                'view_name': 'persona_app:person-detail',
                'lookup_field': 'pk'
            }
        }

        
class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()    