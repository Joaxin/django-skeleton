# django-skeleton-cat

![](https://img.shields.io/github/stars/joaxin/django-skeleton-cat) ![](https://img.shields.io/github/forks/joaxin/django-skeleton-cat) ![](https://img.shields.io/github/issues/joaxin/django-skeleton-cat) ![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fjoaxin%2Fdjango-skeleton-cat)

A template for launching new Django projects quickly. 

- django-skeleton-cat-allauth : Use django Social authentication via django-allauth : https://github.com/pennersr/django-allauth

- django-skeleton-cat-simple: Use django built-in authentication system via `django.contrib.auth`.

  `username`，`password`，`email`，`first_name`，`last_name`，`is_active`

- django-skeleton-cat-registration: Use django-registration system via: https://django-registration.readthedocs.io/en/latest/

## Screenshots

![main](shots/main.png)

![sign_up](shots/sign_up.png)

![admin](shots/admin.png)

## Features

Comes with a complete user authentication flow, custom user model, and social authentication options via Gmail, Facebook, Twitter, etc.

- For Django>=2.2 and Python>=3.7
- Styling with Bootstrap v4.5.0 : https://github.com/twbs/bootstrap via django-crispy-forms
- Email/password for log in/sign up instead of Django's default username/email/password pattern
- django-debug-toolbar : https://github.com/jazzband/django-debug-toolbar
- support for ~~django-suit~~  django-simpleui
- Support fontawesome 5.1: https://fontawesome.com/icons?d=gallery&q=cat&m=free

For django-skeleton-cat-allauth:

- Use django Social authentication via django-allauth 
- Support DRF(DjangoRestFramework)
- An CRUD demo with DRF
- Custom user model
- Still building…..

For django-skeleton-cat-simple:

- Use django built-in authentication system
- Extended user model

For django-skeleton-cat-registration:

- Use django-registration system 
- Still building…..

## First-time setup

setup a `virtualenv` if needed

```bash
mkdir env
virtualenv dj
source dj/bin/activate
```

```bash
cd yourproject
pip install -r requirements.txt
python manage.py makemigrations users
python manage.py makemigrations images
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
# A user with that username already exists.
test/test/test@test.com ==> test7...
luna/luna/luna@test.com
luna2/luna2/luna2@test.com
luna3/...
```

Run:

```
python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Authentication URL

> https://docs.djangoproject.com/en/3.1/topics/auth/default/

### Defualt (django.contrib.auth.views)

```python
urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
]
```

This will include the following URL patterns:

```python
LoginView
users/ login/ [name='login']
Defaults to registration/login.html

LogoutView
users/ logout/ [name='logout']
Defaults to registration/logged_out.html.

PaswordChangeView
users/ password_change/ [name='password_change']
Defaults to registration/password_change_form.html

PasswordChangeDoneView
users/ password_change/done/ [name='password_change_done']
Defaults to registration/password_change_done.html

PasswordResetView
users/ password_reset/ [name='password_reset']
Defaults to registration/password_reset_form.html

PasswordResetDoneView
users/ password_reset/done/ [name='password_reset_done']
Defaults to registration/password_reset_done.html

PasswordResetConfirmView
users/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
Defaults to registration/password_reset_confirm.html.

PasswordResetCompleteView
users/ reset/done/ [name='password_reset_complete']
Defaults to registration/password_reset_complete.html
```

If you want more control over your URLs, you can reference a specific view in your URLconf:

```python
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('login/',auth_views.LoginView.as_view(),name='login'),
    ...
]
```

The views have optional arguments you can use to alter the behavior of the view. 

For example, if you want to change the template name a view uses, you can provide the `template_name` argument. A way to do this is to provide keyword arguments in the URLconf, these will be passed on to the view. For example:

```python
path('logout/',
    auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html',
        next_page=None
    ),
    name = 'logout'
)
urlpatterns = [
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),
    ),
]
```

### Django-allauth

```python
accounts/ ^ ^signup/$ [name='account_signup']
accounts/ ^ ^login/$ [name='account_login']
accounts/ ^ ^logout/$ [name='account_logout']
accounts/ ^ ^password/change/$ [name='account_change_password']
accounts/ ^ ^password/set/$ [name='account_set_password']
accounts/ ^ ^inactive/$ [name='account_inactive']
accounts/ ^ ^email/$ [name='account_email']
accounts/ ^ ^confirm-email/$ [name='account_email_verification_sent']
accounts/ ^ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
accounts/ ^ ^password/reset/$ [name='account_reset_password']
accounts/ ^ ^password/reset/done/$ [name='account_reset_password_done']
accounts/ ^ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
accounts/ ^ ^password/reset/key/done/$ [name='account_reset_password_from_key_done']
```

## Next Steps

- Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
- Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
- Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/3.1/topics/email/#module-django.core.mail) to configure an SMTP backend
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

- [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
- [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
- `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html)

### Thanks to

- icon & logo: https://www.easyicon.net/language.en/1141863-announce_cat_icon.html
- images from [unsplash](https://unsplash.com/)
- [DjangoX](https://github.com/wsvincent/djangox) BY  [wsvincent](https://wsvincent.com)
