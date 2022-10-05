tiny_personal_website
=====================

THIS IS BACK FROM THE DEAD :D

This is a Python based CMS for a small personal website. The back end uses
the bottle web framework and the front end is bootstrap. YAML is used for site
 specific configurations. Tested with Python 3.10.7 only.

 I originally wrote this 7 or 8 years ago, and recently absolutely borked my
 newer website, resulting in me quickly resurrecting this thing in about a
 day. It's... fine. It's not terrrible.

 Here's the guide I used for digital ocean:
 https://docs.digitalocean.com/tutorials/app-deploy-flask-app/

 You want the following command plugged into where-ever this runs:

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


## Old setup

1. Clone this github repo into your desired webroot.

2. Install missing libraries if any: `pip3.10 install -r requirements.txt`

3. You can configure everything (e.g. the webroot absolute path, your photo,
 quote, etc) by renaming `config/config.yaml.sample` to `config.yaml` and 
replacing all the sample data with your own real data.

4. The website assumes you're running on a Linux server with apache. I use the
 [mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi) apache module to
deliver this content. 
  + In `config/example_apache_vhost.conf` I have an example apache
virutal host config. I recommend creating a special user and group for this
 website to run as.
  + There is also a mandatory `config/wsgi.conf` you'll need to put in your
 apache config. You may also need to modify permissions for the socket file if
 you are running CentOS/RHEL, which will live in `/var/run/http`.

5. All changes to HTML, CSS, JS, Python, or your core YAML will require an
 apache restart - with this specific configuration for the web server portion.
