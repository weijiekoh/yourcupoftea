# Remain vs Leave

This is the source code for Remain vs Leave, a sociopolitical questionnaire for voters in the 2015 British referendum on EU membership, commonly known as Brexit. Try it out at http://remainvsleave.co.uk/.

## Technical overview

This is a Flask app and works on Heroku out of the box. It doesn't require a database. To use it locally, run these commands:

```
git clone https://github.com/weijiekoh/yourcupoftea.git && cd yourcupoftea
python app.py
```
... and launch http://0.0.0.0:5000 in a web browser.

This app can be deployed to Heroku with a simple `git push`. Make sure to store a random Flask secret key in the `FLASK_SECRET_KEY` environment variable.
