tiny_personal_website
=====================

This is a small Python based personal website aimed first and foremost at being a resume. Example here:

<img src="./example.png" alt="screenshot of jessebot.work which serves as an example website. It features a picture of Jesse a person with blue hair that is almost 30. a blurb about them that you can read in config/config.yaml and link icons to github, gitlab, and linkedin." style="width: 40%;">

I originally wrote this 7 or 8 years ago, and recently absolutely borked my
newer website, resulting in me quickly resurrecting this thing in about a day
and a half. This one does the same thing, but better, and faster, with less js.

Feel free to take anything you need :) But keep it open source.
You gotta. [No, like you literally have to.](./LICENSE)


Under the Hood
--------------
* Bootstrap v5 - frontend js/css
* Flask        - backend routing
* Gunicorn     - serving website
* YAML         - config file

* The Open Source Community <3 - answers to all your questions for free


## Dev and Testing

1. Clone this github repo into your desired webroot.

2. Install missing libraries if any: `pip3.10 install -r requirements.txt`

3. You can configure everything (e.g. website title, your photo, quote, etc)
   by editing `config.yaml` and replacing all the Jesse data with your own.

5. All changes to HTML, CSS, and Python, or your core YAML will require a
   restart of gunicorn or a rebuild of the docker container.

6. for docker, you can just do:
   ```bash
   docker build . -t <name of tag you want>

   # to test locally, you can do -p 8000:8080 to forward
   # port 8080 on the container to port 8000 on your local machine
   docker run --rm -p 8000:8080 <name of the tag you used>
   ```

   For testing locally, _without_ a docker rebuild:
   ```bash
   gunicorn app:app
   ```

Then you can go to http://127.0.0.1:8000 in a browser to view your changes.


### Deploying on an app platform

You want the following command plugged into where-ever this runs
(e.g. digital ocean app platform):

```bash
gunicorn --worker-tmp-dir /dev/shm app:app
```

And the container port of note is port 8080.


## Frontend Dev Notes
I found [this guide](https://stackoverflow.com/questions/68558955/bootstrap-centering-container-in-the-middle-of-the-page)
on vertically centering items and it helped a lot. Basically both the body and
base container you have need to be h-100 and vh-100 and for extra security,
add `min-height: 100vh;` to the CSS for the body.
