# myrecipe
A demo web app to share reipes. Built using django.

### Implementaions:
- Multiple database using database router
- Using different databases sqlite3 and MongoDB for authentication and storing data respectively.

To setup, run commands:

```
git clone https://github.com/ghostsam7/myrecipe
cd myrecipe
pip install -r requirement.txt
```
(some installs are from git repositories, may run slow)</br>
```
python manage.py syncdb
python manage.py runserver
```
