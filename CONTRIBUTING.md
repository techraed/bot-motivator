# Issues and Pull Requests
We don't have any strict rules concerning opening issues or pull requests. Just
suggest your ideas, edits or inform about issues, bugs within GitHub instruments.
Code cleaning and minor refactoring is always welcomed.

# Work flow
Contribute to project by pull requesting changes made in checkouted from develop branches.

# Run local
```.env
echo "BOT_TOKEN=<your_bot_token> >> .env

# make sure you have pipenv
pipenv run python3 main.py

# run celery worker
celery -A app.task_processor.celery_motivator worker -l INFO

# run celery beat
celery -A app.task_processor.celery_motivator beat -l INFO
```

Make sure you change motivational message sending timeout.

# New habits
Add your ***.yaml*** habit file to app/motivator/user/habits/habits_configs.
A good example is our first [habit](./app/motivator/users/habits/habits_configs/stop_eating_flour.yml) we made on our first release.
