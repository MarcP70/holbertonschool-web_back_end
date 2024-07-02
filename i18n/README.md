      Project: i18n | Holberton Laval, France Intranet

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/91e1c50322b2428428f9.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240702%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240702T073450Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7692bda2a4bfab53cc69dba309c65084eafd33ef1c5e532d599c44e96c9bdd43)

Resources
---------

**Read or watch:**

*   [Flask-Babel](/rltoken/O7S-gr-vGk6dOtLsp596dw "Flask-Babel")
*   [Flask i18n tutorial](/rltoken/5ZXAPeW50RkAGQAEjkToug "Flask i18n tutorial")
*   [pytz](/rltoken/3nHx3G1tJcP7iHnF1E7FUw "pytz")

Learning Objectives
-------------------

*   Learn how to parametrize Flask templates to display different languages
*   Learn how to infer the correct locale based on URL parameters, user settings or request headers
*   Learn how to localize timestamps

Requirements
------------

*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle style (version 2.5)
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   All your `*.py` files should be executable
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

### Python Scripts

  * Ensure venv package is installed
  sudo apt-get install python3.11-venv

  * Create virtual environment
  python3 -m venv venv

  * Activate virtual environment
  source venv/bin/activate

  * Install dependencies
  pip install Flask
  pip install flask_babel


Tasks
-----

### 0\. Basic Flask app

mandatory

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `0-app.py, templates/0-index.html`

**0/6** pts

### 1\. Basic Babel setup

mandatory

Install the Babel Flask extension:

    $ pip3 install flask_babel


Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `1-app.py, templates/1-index.html`

**0/9** pts

### 2\. Get locale from request

mandatory

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `2-app.py, templates/2-index.html`

**0/5** pts

### 3\. Parametrize templates

mandatory

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_


Then initialize your translations with

    $ pybabel extract -F babel.cfg -o messages.pot .


and your two dictionaries with

    $ pybabel init -i messages.pot -d translations -l en
    $ pybabel init -i messages.pot -d translations -l fr


Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

msgid

English

French

`home_title`

`"Welcome to Holberton"`

`"Bienvenue chez Holberton"`

`home_header`

`"Hello world!"`

`"Bonjour monde!"`

Then compile your dictionaries with

    $ pybabel compile -d translations


Reload the home page of your app and make sure that the correct messages show up.

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`

**0/8** pts

### 4\. Force locale with URL parameter

mandatory

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:** ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240702%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240702T073450Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4fdb5b28385e79f704a26155618b15be47a93ebfe1809728180a60c6a6e93006)

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `4-app.py, templates/4-index.html`

**0/6** pts

### 5\. Mock logging in

mandatory

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.

    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid

English

French

`logged_in_as`

`"You are logged in as %(username)s."`

`"Vous êtes connecté en tant que %(username)s."`

`not_logged_in`

`"You are not logged in."`

`"Vous n'êtes pas connecté."`

**Visiting `http://127.0.0.1:5000/` in your browser should display this:**

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240702%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240702T073450Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=11cfb0f446479303df54b727049d02d6209c5079d97099514c8ebed986981044)

**Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:** ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240702%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240702T073450Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5510ba9227958eb559be350b55b5761c5f2fa2a57728442d9433cb314ac596ec)

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `5-app.py, templates/5-index.html`

**0/8** pts

### 6\. Use user locale

mandatory

Change your `get_locale` function to use a user’s preferred local if it is supported.

The order of priority should be

1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240702%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240702T073450Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9b39d3af88a1da2fba85747fc0f1c41c7377b934e120cdb681428147c00100d6)

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `6-app.py, templates/6-index.html`

**0/6** pts

### 7\. Infer appropriate time zone

mandatory

Define a `get_timezone` function and use the `babel.timezoneselector` decorator.

The logic should be the same as `get_locale`:

1.  Find `timezone` parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.

**Repo:**

*   GitHub repository: `holbertonschool-web_back_end`
*   Directory: `i18n`
*   File: `7-app.py, templates/7-index.html`

**0/6** pts
