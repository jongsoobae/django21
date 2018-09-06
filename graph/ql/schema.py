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

schema = graphene.Schema(query=Query)
