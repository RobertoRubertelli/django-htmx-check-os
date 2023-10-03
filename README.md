# [Django Htmx Check](https://github.com/RobertoRubertelli/django-htmx-check-os)

####
DJANGO-HTMX. [HTMX](https://htmx.org/) doesn't work in old browser.
I need a way to advise the user if the browser doesn't work.
In the home view, I'm checking if the user has a 64bit or not.
In the template thrue one line of [_Hyperscript](https://hyperscript.org/), 
if something is wrong in the view, the warning disappear, keeping me safe.
I want to use HTMX in DJANGO, htmx is the present and the next future for django web site.
_Hyperscript is fitting very well htmx in the DOM, it is written by the same htmx author, that's why I choosed it. If _Hyperscript is working, HTMX is working too. This is my conclusion.

[link to Git-Hub source files](https://github.com/RobertoRubertelli/django-htmx-check-os)

My Site [Managepy.it](https://www.managepy.it/)

## Getting started

## Setup

Follow these instructions to try this demo out locally.
I'm using pipenv, you can use pip instead for the virtual environment and install.

```bash

# Install requirements.txt in a new virtual environment
pipenv install -r requirements.txt
# activate the shell
pipenv shell

# Clone Git folders 
git clone ....

# Setup database.
./manage.py migrate

# Run the development server.
./manage.py runserver

# Now you can view the project at http://localhost:8000
```
