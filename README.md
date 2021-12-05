# Grogu bot <img align="right" src="https://github.com/alejandrodlsp/razer-bot/blob/main/assets/avatar-circle.png?raw=true" alt="drawing" width="200"/>
### Open source discord bot made using *discord.py*

<hr/>
<br>
<br>

## Support

Currently, the bot supports the following commands and functionality:

:wrench: **Administrator commands** 
- Kick 
- Ban
- Unban

:mag: **Util commands**
- Clear
- Ping
- Change server prefix

:musical_keyboard: **Music commands** 
- Play
- Pause
- Resume
- Remove
- Shuffle
- Stop
- Queue
- Song
- Skip
- Previous
- Repeat (All, one, none)

:computer: **Functionality** 
- Cycling presence messages
- Custom server based prefixes
- Command alias support
- Logging

## Roadmap

These are the main features that I aim to intruduce in the following future:

- ~~Music support~~
- Spotify playlists
- ~~Meme generation~~
- Digital currency

<hr/>

## Seting-up locally

To set up a copy of the client locally, you will need to generate a discord bot project, detailed documentation on how to do this can be found [here](https://discordpy.readthedocs.io/en/latest/discord.html)

You can clone the repository using: 

```shell
git clone https://github.com/alejandrodlsp/grogu-bot.git
```

To activate the python virtual environment, you will need to have the venv package installed. You can install this using pip3:

```shell
pip3 install venv
```

You will need to create a **.env** file containing all environment variables. You can find an example **.env** file in the **.env.example** file. Alternativelly, you can run the 
**setup.sh** script to generate the environment file.

You will need to populate the .env file with your discord private token, as well as any other environment variables.

To run the bot, first you will need to run the **audio server**, to do this you will need to have Java 11+ installed on your machine (Java 11 recommended), and run:

```shell
java -jar audio_server/Lavalink.jar
```

Finally, to run the bot client:

```shell
python3 bot.py
```
<hr/>
