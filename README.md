# Bot motivator
Use [@PersuaderBot](https://t.me/PersuaderBot) telegram bot to stop doing something or to get a good habit.

## Usage
It's really simple. Bot provide you with some commands:
 - /start
 - /delete
 - /help
 - /cancel
 
#### Start command
This command is used to register habits. Interaction with bot is performed in
conversation form. Some parts of conversation allow you finishing it before getting to final state
of conversation. Also, you have an ability to cancel conversation in any state with ***/cancel*** command.

#### Delete command
Used to delete habits. Delete conversation has similar to ***/start*** conversation behaviour.

#### Help command
Shows you help information in russian language

#### Cancel command
Use to cancel conversation. Works only if ***/delete*** or ***/start*** conversation was called.

## Some technical information
Celery module is used as motivation logic engine.

## Contributing
Everything concerning contributing you can find [here](./CONTRIBUTING.md).
