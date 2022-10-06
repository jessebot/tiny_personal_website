tiny_personal_website
=====================

THIS IS BACK FROM THE DEAD :D

This is a Python based CMS for a small personal website. The back end uses
the bottle web framework and the front end is bootstrap. YAML is used for site
 specific configurations. Tested with Python 3.10.7 only.

 I originally wrote this 7 or 8 years ago, and recently absolutely borked my
 newer website, resulting in me quickly resurrecting this thing in about a
 day. It's... oke :shrug:

 You want the following command plugged into where-ever this runs
 (e.g. digital ocean app platform):
 ```bash
 gunicorn --worker-tmp-dir /dev/shm app:app
 ```

### Coming Soon
better docker file

Under the Hood
--------------
* Bootstrap v5
* Flask
* The Open Source Community <3


## Setup

1. Clone this github repo into your desired webroot.

2. Install missing libraries if any: `pip3.10 install -r requirements.txt`

3. You can configure everything (e.g. website title, your photo, quote, etc)
   by renaming `config/config.yaml.sample` to `config.yaml` and replacing all 
   the sample data with your own real data.

5. All changes to HTML, CSS, and Python, or your core YAML will require a
   restart of gunicorn or a rebuild of the docker container.

6. for docker, you can just do:
   ```bash
   docker build . -t <name of tag you want>`
   # if you want to test it locally, you can do this
   docker run --rm -p 8080:8000 <name of the tag you used>
   ```
   Then you can go to http://127.0.0.1:8080 in a browser to view your changes.

   For testing locally, _without_ a docker rebuild:
   ```bash
   gunicorn app:app
   ```
   Then you can go to http://127.0.0.1:8000 in a browser to view your changes.

## Notes
I found [this guide](https://stackoverflow.com/questions/68558955/bootstrap-centering-container-in-the-middle-of-the-page)
on vertically centering items and it helped a lot. Basically both the body and
base container you have need to be h-100 and vh-100 and for extra security, 
add `min-height: 100vh;` to the CSS for the body
