# Eriza — A Jack-Of-All-Trade Discord Bots

## Launching locally
Merely run `python main.py` or `python3 main.py`, depending on your exploitation system.

## Install


## Fly.io
### Deploying with Fly.io
First off, create your fly.io account. Then, you must install the fly software [following these instructions](https://app-generator.dev/docs/deployment/fly-io/index.html).

Go to your terminal, from your fly app. Then, run the following:
```
fly auth login
fly deploy
```

### Connection to the fly.io database from your local environment

Do keep in mind that these instructions are aimed at the bot current fly.io hosting. Fly.io changed its process since the bot's inception, so it might be different for you. 

Then, start a proxy with the instruction:
`fly proxy 5433:5432 -a erizadb
Proxying localhost:5433 to remote [erizadb.internal]:5432`

```
fly ssh console -a {YOUR APP NAME, NOT THE DB's}

// Inside the fly.io VM:

printenv DATABASE_URL
```

You will get something like
`postgres://postgres:ACTUAL_PASSWORD@erizadb.internal:5432/REAL_DB_NAME`.

Take this URL. Change to this model: `postgres://postgres:ACTUAL_PASSWORD@localhost:5433/REAL_DB_NAME?sslmode=disable`.

Do note that the port is changed as well, to follow the proxy's port.

You will need to keep the proxy open every time you want to access the datatabase from your local.


### Documentation
[Using the DB (just in case)](https://fly.io/docs/postgres/getting-started/what-you-should-know/)

[Secret handling](https://fly.io/docs/reference/secrets/). Secrets are listed into the local env file.

[Downscaling app](https://community.fly.io/t/what-does-downscaling-app-mean/12309)

[Deploy a python discord](https://community.fly.io/t/deploy-python-discord-bot/5667)

## TODO
- Tests
- Fix rare word list
- Fix rare word scraping
- Fix help