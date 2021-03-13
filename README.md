This is initial code for create sample codes in in django rest framework
---

- [1. setup environment](#1-setup-environment)
- [2. create project and User app](#2-create-project-and-user-app)
  - [2.1. create project and app](#21-create-project-and-app)
  - [2.2. create sample data](#22-create-sample-data)
- [3. Run server](#3-run-server)
  - [3.1. Access swagger](#31-access-swagger)
  - [3.2. Access admin site](#32-access-admin-site)
  - [3.3. Access users/groups apis](#33-access-usersgroups-apis)
- [4. Music app](#4-music-app)
  - [4.1. Create new app and migrate database](#41-create-new-app-and-migrate-database)
  - [4.2. Views](#42-views)
    - [4.2.1. musican-api-views](#421-musican-api-views)
    - [4.2.2. musican-generic-views](#422-musican-generic-views)
    - [4.2.3. musican-viewset](#423-musican-viewset)
    - [4.2.4. musican-debug](#424-musican-debug)
  - [4.3. Serializers](#43-serializers)
    - [4.3.1. Common serializer](#431-common-serializer)
    - [4.3.2. Model serializer](#432-model-serializer)
- [5. Using serializer effectively](#5-using-serializer-effectively)
  - [5.1. In read data](#51-in-read-data)
    - [5.1.1. Using source keyword](#511-using-source-keyword)
    - [5.1.2. Using SerializerMethod](#512-using-serializermethod)
    - [5.1.3. Using to_representation](#513-using-to_representation)
  - [5.2. In write data](#52-in-write-data)
    - [5.2.1. Add custom field validator](#521-add-custom-field-validator)
    - [5.2.2. Cross field validation](#522-cross-field-validation)
    - [5.2.3. When and how to override to_internal_value()](#523-when-and-how-to-override-to_internal_value)
    - [5.2.4. When and how to override create()](#524-when-and-how-to-override-create)
  - [5.3. Other things](#53-other-things)
    - [5.3.1. Passing a value directly to the save method](#531-passing-a-value-directly-to-the-save-method)
    - [5.3.2. Get current user of the request](#532-get-current-user-of-the-request)
    - [5.3.3. HiddenField](#533-hiddenfield)
    - [5.3.4. access serializer raw input](#534-access-serializer-raw-input)
    - [5.3.5. Override data to force ordering](#535-override-data-to-force-ordering)
    - [5.3.6. Handling multiple creates/updates/deletes in nested serializers](#536-handling-multiple-createsupdatesdeletes-in-nested-serializers)
- [6. Other tricks](#6-other-tricks)
  - [6.1. django-rest-framework-tricks](#61-django-rest-framework-tricks)
  - [6.2. Customizing the generic views](#62-customizing-the-generic-views)
- [7. QuerySet](#7-queryset)
- [8. Search-Filter-Ordering](#8-search-filter-ordering)
  - [8.1. Filter base on url and query params](#81-filter-base-on-url-and-query-params)
  - [8.2. Using 3rd Filter Class](#82-using-3rd-filter-class)
  - [8.3. Search](#83-search)
  - [8.4. Ordering](#84-ordering)
  - [8.5. Compose search filter ordering in one viewsets](#85-compose-search-filter-ordering-in-one-viewsets)
- [9. Pagination](#9-pagination)
- [10. Sequence diagram](#10-sequence-diagram)
  - [10.1. List api](#101-list-api)
- [11. Add nginx configs](#11-add-nginx-configs)
  - [11.1. Config for http only](#111-config-for-http-only)
  - [11.2. Config for https](#112-config-for-https)

# 1. setup environment

```shell
pyenv install -v 3.8.0
pyenv local 3.8.0
python --version
which python
venv-create     # if it detect wrong version of python, it need to open another shell
.venv
which python
pip install -r requirements.txt

# mac 
brew install jq
# ubuntu
sudo apt-get install jq -y
```

# 2. create project and User app

create this app as link: https://www.django-rest-framework.org/tutorial/quickstart/

## 2.1. create project and app

**NOTE**: Ignore this step if User app is created

```shell
django-admin startproject main .
django-admin startapp user
```

## 2.2. create sample data

```shell
make create-sample-data
```

# 3. Run server

make run

## 3.1. Access swagger

http://127.0.0.1:8027/swagger/

## 3.2. Access admin site

http://127.0.0.1:8027/admin

Account as above: admin/admin

## 3.3. Access users/groups apis

http://127.0.0.1:8027/api/v1

login by above account: admin/admin

or by command: 

```shell
make user-get
```

[music/serializers.py](music/serializers.py)

# 4. Music app

## 4.1. Create new app and migrate database

```shell
# django-admin startapp music
make makemigrations
make migrate
```
access: http://127.0.0.1:8027/swagger/

## 4.2. Views
### 4.2.1. musican-api-views

This set of apis describle how to using `APIView` to make api as basic and normal, code will be handle by yourself

**Test:**

```shell
make musican-api-views-
```

**Conclusion:**

Using api views when you want to custom detail in your api

### 4.2.2. musican-generic-views

This set of apis describle how to using `generics` view to make api code will be made shorter

**Test:**

```shell
make musican-generic-views-
```

**Conclusion:**

Using generic view when you want to combine some methods in one view, but not all, ex: only allow methods: CREATE/GET/LIST

### 4.2.3. musican-viewset

This set of apis describle how to using `ModelViewSet` to make code shortest

**Test:**

```shell
make musican-viewset-
```

**Conclusion:**

Using viewset when you want to add all methods(actions) of a object in one view, all methods will be routed automatically

### 4.2.4. musican-debug

This apis help to debug all django rest framework flow, how a request is handled through all layers of this framework

Uncomment below line in settings.py

```python
MIDDLEWARE = [
    # 'main.middlewares.DebugpyMiddleware', 
```

```shell
make debug-
```

## 4.3. Serializers

### 4.3.1. Common serializer

This type of serializer you don't need to specify your model, but you must declare all neccessary fields manually

Ex: **MusicianSerializer** [music/serializers.py](music/serializers.py)

Ex: using this serializer here: [music/generic_views.py](music/generic_views.py)

### 4.3.2. Model serializer

You must specify your model in **Meta class**

You don't need to specify model field

Ex: [music/model_serializers.py](music/model_serializers.py)

# 5. Using serializer effectively

## 5.1. In read data

### 5.1.1. Using source keyword

Reference: https://medium.com/better-programming/how-to-use-drf-serializers-effectively-dc58edc73998

Using `source when you only want to get data, but not modify anything

code sample in this serializer: **MusicianModelSerializerReadEffective_SourceKeyword** in this file: [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)

- source=field_name to rename of this returned field, ex: `source='first_name'`
- source=Model.method() to get modified data, ex: `source='get_full_name'`
- source worker with relationships, ex: `OneToMany` or`ForeignKey`, `OneToOneField`, and `ManyToMany`
  - ex: `source='profile.street'` or `source='profile.city`
- source worker with methods of related objects, same `Model.method()`, ex: `source="profile.get_full_address"`
- source work with `OneToMany`, ex: `source='album_set'`. **NOTE** with `ManyToMany` don't need `source`, ex: `instruments` field

### 5.1.2. Using SerializerMethod

Using `SerializerMethod` when you want to custom more output data. For example:

- Convert `first_name` to titlecase during serialization.
- Convert `full_name` to uppercase.
- Set `albums` as `None` instead of an empty list if no groups are associated with the user.

All example in this serializer: **MusicianModelSerializerReadEffective_SerializerMethod** in file [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)

### 5.1.3. Using to_representation

Using to_representation when you want to custom mutiple data fields

All example in this serializer: **MusicianModelSerializerReadEffective_SerializerMethod** in file [music/using_serializer_effective/serializers.py](music/using_serializer_effective/serializers.py)


## 5.2. In write data

Reference: https://medium.com/@raaj.akshar/how-to-effectively-use-django-rest-framework-serializers-during-write-operations-dd73b62c26b5

### 5.2.1. Add custom field validator

Using it when want to validate a single field

Ex: field `password` in **MusicianModelSerializerReadEffective_SourceKeyword.validate_password()**

### 5.2.2. Cross field validation

Using it when we want to add some validation where we need to access multiple field simultaneously

Ex: validate that the `first_name` and `last_name` be different in **MusicianModelSerializerReadEffective_SourceKeyword.validate()**

### 5.2.3. When and how to override to_internal_value()

`to_internal_value()`  can be used to do some pre-processing before validation code is executed

Ex 1: Frontend or mobile app sends user information enclosed in another dictionary with key `user`

```json
{
	'user': {
		'first_name': 'john',
		'last_name': 'doe',
		'username': 'john',
		'password': 'abc123#'
	}
}
```

In such case, `user` info needs to be extracted out of the dictionary before the fields are validated. We can achieve this by overriding `to_internal_value()` in **MusicianModelSerializerReadEffective_SourceKeyword.to_internal_value()**

### 5.2.4. When and how to override create()

`create()` is called when `serializer.save()` is called

create() should be overridden when we want to do something different from this default behavior.

## 5.3. Other things

### 5.3.1. Passing a value directly to the save method

```python
serializer = EmailSerializer(data=request.data)
serializer.is_valid(raise_exception=True)
serializer.save(owner_id=request.user.id)   # <------ this passed value won't be validated
											# It may be used to force an override of the initial data
```

### 5.3.2. Get current user of the request

```python
serializers.CurrentUserDefault()
```

### 5.3.3. HiddenField

HiddenField is a field class that does not take a value based on user input, but instead takes its value from a default value or callable.

```python
modified = serializers.HiddenField(default=timezone.now)
owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
```

### 5.3.4. access serializer raw input

`serializer.initial_data`

### 5.3.5. Override data to force ordering

By default, Django querysets are not ordered at all. Enforcing ordering on the list view can easily be accomplished by adding ordering to the view’s `queryset`, but in cases where nested resources should also be ordered, it’s not so simple. For read-only fields, it can be done within `SerializerMethodField`, but what to do in a situation where a field has to be writable? In such a case, a serializer’s data property can be overridden, as shown in this example:

```python
@property
def data(self):
    data = super().data
    data['phone_numbers'].sort(key=lambda p: p['id'])
    return data
```

### 5.3.6. Handling multiple creates/updates/deletes in nested serializers

There are two paths you can follow in this case:

- use the quite popular, third party library DRF Writable Nested
- do it on your own
  
I would recommend choosing the second option at least once, so you will know what’s going underneath.

After analyzing incoming data, in most scenarios, we are able to make the following assumptions:

- all items that should be updated have id,
- all items that should be created don’t have id,
- all items that should be deleted are present in data storage (eg. database), but are missing in the incoming request.data
  
Based on this, we know what to do with particular items on the list. Below is a snippet that shows this process in detail:

```python
class CUDNestedMixin(object):
    @staticmethod
    def cud_nested(queryset: QuerySet,
                   data: List[Dict],
                   serializer: Type[Serializer],
                   context: Dict):
        """
        Logic for handling multiple updates, creates and deletes
        on nested resources.
        :param queryset: queryset for objects existing in DB
        :param data: initial data to validate passed from higher
                level serializer to nested serializer
        :param serializer: nested serializer to use
        :param context: context passed from higher level
                serializer
        :return: N/A
        """
        updated_ids = list()
        for_create = list()
        for item in data:
            item_id = item.get('id')
            if item_id:
                instance = queryset.get(id=item_id)
                update_serializer = serializer(
                    instance=instance,
                    data=item,
                    context=context
                )
                update_serializer.is_valid(raise_exception=True)
                update_serializer.save()
                updated_ids.append(instance.id)
            else:
                for_create.append(item)

        delete_queryset = queryset.exclude(id__in=updated_ids)
        delete_queryset.delete()

        create_serializer = serializer(
            data=for_create,
            many=True,
            context=context
        )
        create_serializer.is_valid(raise_exception=True)
        create_serializer.save()
```

And here is the simplified version of how a high-level serializer can make use of this mixin:

```python
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer,
                        CUDNestedMixin):
    phone_numbers = PhoneSerializer(
        many=True,
        source='phone_set',
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_numbers')

    def update(self, instance, validated_data):
        self.cud_nested(
            queryset=instance.phone_set.all(),
            data=self.initial_data['phone_numbers'],
            serializer=PhoneSerializer,
            context=self.context
        )
        ...
        return instance
```

Keep in mind that nested objects should consume `initial_data` instead of `validated_data`. That’s because running validation calls `field.to_internal_value()` on each of a serializer’s fields, which may modify data stored by a particular field (eg. by changing primary key to model instance).


# 6. Other tricks

## 6.1. [django-rest-framework-tricks](https://github.com/barseghyanartur/django-rest-framework-tricks)

## 6.2. [Customizing the generic views](https://www.django-rest-framework.org/api-guide/generic-views/#customizing-the-generic-views)


# 7. QuerySet

https://docs.djangoproject.com/en/3.1/topics/db/queries/

A django queryset is like its name says, basically a collection of (sql) queries, in your example above print(b.query) will show you the sql query generated from your django filter calls.

Since querysets are lazy, the database query isn't done immediately, but only when needed - when the queryset is evaluated. This happens for example if you call its __str__ method when you print it, if you would call list() on it, or, what happens mostly, you iterate over it (for post in b..). This lazyness should save you from doing unnecessary queries and also allows you to chain querysets and filters for example (you can filter a queryset as often as you want to).


# 8. Search-Filter-Ordering

Refer: https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user

## 8.1. Filter base on url and query params

```python
    # re_path('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)
```

```python
    # http://example.com/api/purchases?username=denvercoder9
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Purchase.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset
```

## 8.2. Using 3rd Filter Class

Sample in file: [viewsets.py](music/sample_search_filter_ordering/viewsets.py)

```python
filter_backends = [DjangoFilterBackend]
filterset_class = MusicanFilter
```

Test command:

```shell
make musican-sample-filter-list-FILTER
# NOTE: test also affect get single object, test with below command
make musican-sample-filter-get-FILTER
```

## 8.3. Search

Sample add search feature in file [viewsets.py](music/sample_search_filter_ordering/viewsets.py)

```python
# filter_backends = [filters.SearchFilter]
filter_backends = [CustomSearchFilter]
search_fields = ['=first_name', '=last_name', '=email', '=profile__city']
```

Test with command:

```shell
make musican-sample-search-list-SEARCH-city
make musican-sample-search-list-SEARCH-last_name
make musican-sample-search-list-SEARCH-last_name_only
```

The search behavior may be restricted by prepending various characters to the *search_fields* :

    '^' Starts-with search.
    '=' Exact matches.
    '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    '$' Regex search.

## 8.4. Ordering

Sample code in file: [viewsets.py](music/sample_search_filter_ordering/viewsets.py)

```python
filter_backends = [rest_filters.OrderingFilter]
ordering_fields = ['last_name', 'first_name', 'email']
ordering = ['email']    # default field for ordering
```

Test with command: 

```shell
make musican-sample-ordering-list-ORDERING-email
make musican-sample-ordering-list-ORDERING-email-last_name
```

## 8.5. Compose search filter ordering in one viewsets

Sample code in file: [viewsets.py](music/sample_search_filter_ordering/viewsets.py)

```python
class MusicianListRetriveViews_Filter_Search_Order(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
```

Test commands: 

```shell
make musican-sample-search-list-SEARCH-ORDERING-city
make musican-sample-filter-list-FILTER-ORDERING
```

# 9. Pagination

Declare default pagination class in file: [settings.py](main/settings.py)

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 10
}
```

Example of using custom pagination class in file: [generic_views.py](music/views/generic_views.py) and file [custom_paginations.py](music/paginations/custom_paginations.py)

```python
class MusicListCreateView(generics.ListCreateAPIView):
    # pagination_class = StandardResultsSetPagination
    pagination_class = CustomPagination
```

Reference: https://www.django-rest-framework.org/api-guide/pagination/#pagination-schemas

Test command:

```shell
make musican-generic-views-list
```

# 10. Sequence diagram

## 10.1. List api

![](readme_images/sequence-diagram-list-api.png)

# 11. Add nginx configs

## 11.1. Config for http only

See this commit:

```shell
commit 4acb9a853040282dc03b002d277ca196f9e344e9 (HEAD -> run-django-with-docker-postgres)
Author: xuananh <xuan.anh.phung@advesa.com>
Date:   Tue Jan 12 11:03:20 2021 +0700

    Add nginx and config nginx
```

Test command:

```shell
# call directly backend api service
make user-get
# call via nginx service
make user-get-via-nginx-http
```

## 11.2. Config for https

See this commit:

```shell
commit af634410e37149b4bd862462edc734323462c3b3 (HEAD -> run-django-with-docker-postgres)
Author: xuananh <xuan.anh.phung@advesa.com>
Date:   Tue Jan 12 13:50:24 2021 +0700

    Add config for using https on nginx
```

Create certificate (if it's not exists):

```shell
make create-ssl-certificate
```

Output:

```shell
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:New York
Locality Name (eg, city) []:New York City
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Bouncy Castles, Inc.
Organizational Unit Name (eg, section) []:Ministry of Water Slides
Common Name (e.g. server FQDN or YOUR name) []:server_IP_address
Email Address []:admin@your_domain.com
```
Test command:

```shell
make user-get-via-nginx-https
```