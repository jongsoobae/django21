from graphene_django import DjangoObjectType
import graphene
from ql.models import School, Classs, Student


class SchoolType(DjangoObjectType):
    class Meta:
        model = School
    

class ClasssType(DjangoObjectType):
    class Meta:
        model = Classs


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(graphene.ObjectType):
    schools = graphene.List(SchoolType)
    classes = graphene.List(ClasssType)
    students = graphene.List(StudentType)

    def resolve_schools(self, info):
        return School.objects.all()

    def resolve_classes(self, info):
        return Classs.objects.all()

    def resolve_students(self, info):
        return Student.objects.all()


class SchoolCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)


class CreateSchool(graphene.relay.ClientIDMutation):

    class Input:
        school = graphene.Argument(SchoolCreateInput)
    
    new_school = graphene.Field(SchoolType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        school_data = input.get("school")
        school = School()
        new_school = update_create_instance(school, school_data)

        return cls(new_school=new_school)

class Mutations(graphene.ObjectType):
    create_school = CreateSchool.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)


def update_create_instance(instance, args, exception=['id']):
    if instance:
        [setattr(instance, key, value) for key, value in args.items() if key not in exception]
    
    instance.save()
    return instance
