#PokeBattle

##Installation

* Please note that these instructions are designed for [UNIX systems](https://www.youtube.com/watch?v=dFUlAQZB9Ng).
* I really cannot be arsed to document the Windows experience... I may however in the future if requested add in some documentation I made for Windows users.
* Be warned though that developing on Windows isn't included because it's much more of a bitch, UNIX is less effort.
* If you __insist__ on using Windows, then I recommend using [VirtualBox](https://www.virtualbox.org/) and installing [Ubuntu 14.04 LTS](http://www.ubuntu.com/download/desktop).
* Use the following commands to install the prerequisites on Ubuntu 14.04 LTS:

> sudo apt-get install git git-core python2.7 python-virtualenv

To install PokeBattle you must ensure you have python v2.7 installed, git installed and virtualenv installed then run the following (see above for Ubuntu):

```bash
git clone https://github.com/Cephlin/PokeBattle.git
cd Pokebattle/
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

##Development

Initially you'll need to do the following from the root dir of the project:

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

-----
To run the project:

> python manage.py runserver

-----
If you edit any models.py file you must run the following:

> python manage.py makemigrations
> python manage.py migrate

-----
You can now view the homepage at:

> http://localhost:8000/

-----
You can add players and pokemon using the address:

> http://localhost:8000/admin/

-----
If you add some players and Pokemon using the admin panel then you will see something like this on the homepage:

    Hello, world!

    Current players are:
    red
    blue

    Current Pokemon are:
    Charmander
    Bulbasaur


=======
##Notes

* The ability Illusion and the moves Role Play and Skill Swap need to be fixed because they didn't work last time on Pokebattle
* There were also issues with Sheer Force for a while
* Stuff like ignoring Iron Barbs for example