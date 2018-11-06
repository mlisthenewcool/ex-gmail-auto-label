# mailautolabel

## Quick start

In order to use this project, you should already have installed :
  - python3
    - https://www.python.org/
  - virtualenv
    - https://virtualenv.pypa.io/en/latest/
  - make
    - https://www.gnu.org/software/make/

Then just navigate at the root of this project and run :
  - virtualenv env
  - source env/bin/activate
  - make

Configure the connection editing :
  - mailautolabel/data/config.ini
    - by default that configuration should work !
      - hostname: imap.gmail.com
      - username: m1.autolabel1@gmail.com
      - password: m1-luminy

At this point you should be able to run the script :
  - python mailautolabel/launcher.py

## Todo, to improve

- comment the code !

- laucher.py
  - make it usable with args, for example :
    - --verbose(default)
    - --quiet
    - --from-remote(then ask for hostname, username, password in terminal)
    - --from-csv csv_filename
    - --ml-methode [supervised, unsupervised]
  - make it colorful !
    - https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
  - indent the outputs

- data/
  - add a method to save the mails we download (which format should we use ?)
  - add a method to download only the mails we don't have on a local file
  - remove the config.ini file when the arg --from-remote is done in the launcher
  - make two repositories, one to deal with local files, the other one to deal with imap connection
  - gmail only
    - generate an oauth2 token to log in

- ml/
  - add a method to determine if we can use supervised algorithm
  - add a supervised algorithm
  - improve unsupervised algorithm

- docs/
  - add documentation generated by Sphinx from comments

- tests/
  - add tests ?

- user interface
  - only if we got time since we already have rich outputs from notebooks !
