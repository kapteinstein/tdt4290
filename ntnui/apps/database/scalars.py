from graphene.types import Scalar
from functools import partial

genders = ["m", "f", "-"]
languages = ["no", "en"]


class Gender(Scalar):
    ''' Custom Gender GraphQL query enum '''

    @staticmethod
    def serialize(gd):
        ''' Ensure the enum is capitalized '''
        return gd.lower()

    @staticmethod
    def parse_literal(node):
        if node.value.lower() in genders:
            return node.value.lower()

    @staticmethod
    def parse_value(value):
        if value.lower() in genders:
            return value.lower()


class Language(Scalar):
    ''' Custom Language GraphQL query enum '''

    @staticmethod
    def serialize(lng):
        ''' Ensure enum is capitalized '''
        return lng.lower()

    @staticmethod
    def parse_literal(node):
        if node.value.lower() in languages:
            return node.value.lower()

    @staticmethod
    def parse_value(value):
        if value.lower() in languages:
            return value.lower()
