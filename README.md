# How to Deploy

1. Clone the Github repository by running the following command in the terminal:

```
$ git clone https://github.com/owiwamasa/fetch-rewards-take-home.git
```

2. Navigate to the project directory by running the following command in the terminal:

```
$ cd fetch-rewards-take-home
```

3. If pipenv or python isn't installed on your machine (Else, continue to step 4):

- <a href='https://www.python.org/downloads/'>Download python here</a>
- <a href='https://pypi.org/project/pipenv/#description'>Download pipenv here</a>

4. Install all dependencies from the Pipfile:

```
$ pipenv install
```

5. Spawn a shell in a virtual environment:

```
$ pipenv shell
```

6. Start the backend server:

```
$ flask run
```

7. Test the application (while the server is running) by entering the following command:

```
$ python test.py
```

The terminal should display the following result:

```
{'payer': 'DANNON', 'points': 1000, 'timestamp': 'Mon, 02 Nov 2020 14:00:00 GMT'}
{'payer': 'UNILEVER', 'points': 200, 'timestamp': 'Sat, 31 Oct 2020 11:00:00 GMT'}
{'payer': 'DANNON', 'points': -200, 'timestamp': 'Sat, 31 Oct 2020 15:00:00 GMT'}
{'payer': 'MILLER COORS', 'points': 10000, 'timestamp': 'Sun, 01 Nov 2020 14:00:00 GMT'}
{'payer': 'DANNON', 'points': 300, 'timestamp': 'Sat, 31 Oct 2020 10:00:00 GMT'}
[{'payer': 'DANNON', 'points': -100}, {'payer': 'UNILEVER', 'points': -200}, {'payer': 'MILLER COORS', 'points': -4700}]
{'DANNON': 1000, 'MILLER COORS': 5300, 'UNILEVER': 0}
```
