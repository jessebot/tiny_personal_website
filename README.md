tiny_personal_website
=====================

This is a Python based CMS for a small personal website. The back end uses
the bottle web framework and the front end is bootstrap. YAML is used for site
 specific configurations.


Setup
-----

1. Clone this github repo into your desired webroot.

2. You can configure everything (e.g. the webroot absolute path, your photo,
 quote, etc) by renaming `config/config.yaml.sample` to `config.yaml` and 
replacing all the sample data with your own real data.

3. The website assumes you're running on a Linux server with apache. I use the
 [mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi) apache module to
deliver this content. 
..* In `config/example.com.conf` I have an example apache
virutal host config. I recommend creating a special user and group for this
 website to run as.
..* There is also a mandatory `config/wsgi.conf` you'll need to put in your
 apache config. You may also need to modify permissions for the socket file if
 you are running CentOS/RHEL, which will live in `/var/run/http`.

4. All changes to HTML, CSS, JS, Python, or your core YAML will require an
 apache restart.


Sample Site
-----------

The website this is based off of is http://jessebot.com

