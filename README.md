# Razer bot <img align="right" src="https://upload.wikimedia.org/wikipedia/en/thumb/4/47/RazerComms_icon.svg/1200px-RazerComms_icon.svg.png" alt="drawing" width="200"/>
### Open source discord bot made using *discord.py*

<hr/>
<br><br>
<br><br>
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

:computer: **Functionality** 
- Cycling presence messages
- Custom server based prefixes
- Command alias support
- Logging

## Roadmap

These are the main features that I aim to intruduce in the following future:

- Music support
- Spotify playlists
- Meme generation
- Digital currency

<hr/>

## Seting-up locally

To set up a copy of the client locally, you will need to generate a discord bot project, detailed documentation on how to do this can be found [here](https://discordpy.readthedocs.io/en/latest/discord.html)

You can clone the repository using: 

```shell
https://github.com/alejandrodlsp/razer-bot.git
```

To activate the python virtual environment, you will need to have the venv package installed. You can install this using pip3:

```shell
pip3 install venv
```

You can then activate the virtual environment using
```shell
source env/bin/activate
```
on mac and linux.

You will need to create a **.env** file containing all environment variables. You can find an example **.env** file in the **.env.example** file. Alternativelly, you can run the 
**setup.sh** script to generate the environment file.

You will need to populate the .env file with your discord private token, as well as any other environment variables.

<hr/>

## Contributing 

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features

### We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.

### We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests
Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints.
5. Issue that pull request!

### Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

### Report bugs using Github's [issues](https://github.com/alejandrodlsp/razer-bot/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/alejandrodlsp/razer-bot/issues/new); it's that easy!

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

### License
By contributing, you agree that your contributions will be licensed under its MIT License.
