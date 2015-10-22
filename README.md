**==================**
**=== PokeBattle ===**
**==================**

====================
=== Installation ===
====================

Please note that these instructions are designed for unix users. I really cannot be arsed to document the Windows experience... I may however in the future if requested add in some documentation I made for Windows users

To install PokeBattle you must ensure you have python v2.7+ and less than v3.0

    git clone

    cd Pokebattle/
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

===================
=== Development ===
===================

Initially you'll need to do the following from the root dir of the project:

    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser

To run the project:

    python manage.py runserver

If you edit any models.py file you must run the following:

    python manage.py makemigrations
    python manage.py migrate

You can now view the homepage at:

    http://localhost:8000/

You can add players and pokemon using the address:

    http://localhost:8000/admin/

If you add some players and Pokemon using the admin panel then you will see something like this on the homepage:

    Hello, world!

    Current players are:
    red
    blue

    Current Pokemon are:
    Charmander
    Bulbasaur


=============
=== Notes ===
=============

- The ability Illusion and the moves Role Play and Skill Swap need to be fixed because they didn't work last time on Pokebattle
- There were also issues with Sheer Force for a while
- Stuff like ignoring Iron Barbs for example