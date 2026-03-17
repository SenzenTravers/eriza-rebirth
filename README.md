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