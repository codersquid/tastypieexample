from tastypie.resources import ALL, ALL_WITH_RELATIONS, ModelResource
from tastypie import authorization, authentication, validation

from inventory.forms import BookForm
from inventory.models import Author, Book


class AuthorResource(ModelResource):
    class Meta:
        resource_name = "authors"
        queryset = Author.objects.all()
        allowed_methods = ["get", "post"]
        filtering = {
            "name": ALL,
        }


class BookResource(ModelResource):

    class Meta:
        resource_name = "books"
        queryset = Book.objects.all()
        allowed_methods = ["get", "post"]
        filtering = {
            "name": ALL,
            "author": ALL_WITH_RELATIONS,
        }
        validation = validation.CleanedDataFormValidation(form_class=BookForm)
        authentication = authentication.Authentication()
        authorization = authorization.Authorization()
