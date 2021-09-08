# Cpt.Prof.Frankie Sanchez

A discord bot for a private server
Built with discord.py
Can be run as a docker container

## to run
set up the python environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
add a `.env` file, options are 
```
export DISCORD_BOT_TOKEN=<discord API Token>
export BOT_DEBUG=<True/False>
```

run with `python bot.py`

## make a docker image
`docker build --tag frankie-sanchez .`
`docker run -d --restart always frankie-sanchez`
