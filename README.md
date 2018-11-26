# melichallenge-imap-python
Email fetcher using Python for a MELI challenge
## SetUp
Change the enviroment variables from docker-compose.yml to setup your account
```yml
EMAIL_USER: "username@gmail.com"
EMAIL_PASSWORD: "mailpassword"
```
## Init
```bash
docker-compose up
```
## To inspect DB
Open in browser [Adminer](http://localhost:8080)
```yml
MYSQL_HOST: "mysql"
MYSQL_DB: "MeliChallenge"
MYSQL_USER: "root"
MYSQL_PASSWORD: "rootpassword"
```
