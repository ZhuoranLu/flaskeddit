# flaskeddit

[![CircleCI](https://circleci.com/gh/aqche/flaskeddit.svg?style=svg)](https://circleci.com/gh/aqche/flaskeddit)

A simplified Reddit clone built in Flask.

## Features

* Secure registration and authentication.
* Create communities.
* Create community posts.
* Reply to community posts.
* Edit or delete your communities, posts, and replies.
* Join communities.
* Get a feed of posts from your joined communities.
* Upvote or downvote posts and replies.
* Sort communities, posts, and replies by latest or most popular.
* Basic user profiles.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. See deployment for notes on how to deploy the project.

### Prerequisites

To run this application you need [Python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/), and [SQLite](https://www.sqlite.org/).

### Local Setup

Clone the project.

```
git clone https://github.com/aqche/flaskeddit.git
```

Use create a `venv` and use `pip` to install the project dependencies.

```
cd flaskeddit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set the `FLASK_APP` environment variable, create the SQLite database, and start the app. Now you can give the application a try at [http://localhost:5000](http://localhost:5000)!

```
export FLASK_APP=flaskeddit.py
flask cli create_db
flask run
```

You can also serve the application locally using [gunicorn](https://gunicorn.org/).

```
gunicorn "flaskeddit:create_app()"
```

## Testing

Flaskeddit is tested using pytest.

Use `pytest` to run the application's tests.

```
pytest
```

## Deployment

Flaskeddit is automatically deployed to [Heroku](https://www.heroku.com/) using [CircleCI](https://circleci.com/).

You can also use `git` to manually deploy the application.

```
export HEROKU_API_KEY="heroku_api_key"
export HEROKU_APP_NAME="heroku_app_name"
git push https://heroku:$HEROKU_API_KEY@git.heroku.com/$HEROKU_APP_NAME.git master
```

## Built With

* [Flask](http://flask.pocoo.org/) - Python Framework
* [Bootstrap](https://getbootstrap.com/) - CSS Framework

## Contributing

Feel free to submit a pull request!

## Authors

* **aqche** - *Author* - [aqche](https://github.com/aqche)

See also the list of [contributors](https://github.com/aqche/flaskeddit/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for more details.

## Acknowledgments

* [reddit](https://www.reddit.com/) - The inspiration for this site.
* [logohub.io](https://logohub.io/) - For the neat logo.
* [favicon.io](https://favicon.io/) - For the matching favicon.
