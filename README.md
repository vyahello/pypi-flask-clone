![Screenshot](logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)

# PYPI clone

> A clone of https://pypi.org based on **flask** python web framework. Please check http://178.62.222.165.

## Tools

### Production
- 3.7+
- [flask](https://flask.palletsprojects.com/en/2.0.x/) 
- sqlalchemy | mongodb
- html & css 
- uWSGI & nginx

### Development

- [black](https://black.readthedocs.io/en/stable/)
- [flake8](http://flake8.pycqa.org/en/latest/)
- pytest

## Usage

### Source code

```bash
git clone git@github.com:vyahello/pypi-flask-clone.git
python3 -m venv venv 
. venv/bin/activate
cd pypi-flask-clone
pip install -r requirements.txt
python pypi_org/app.py
```

Then please open http://0.0.0.0:5000 in your browser.

**[⬆ back to top](#pypi-clone)**

## Development notes

### DB migrations 
```bash
alembic init alembic
alembic current 
alembic revision --autogenerate -m 'Commit Msg'
alembic upgrade head
```

### Testing 

Please run the following tool to start unit (web) tests:
```bash
pytest tests
```

### CI

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Deployment

The app is deployed on the linux machine, please follow the next instructions to deploy your app:

```bash
# call setup only for the first run
./server/setup.sh
service nginx start
systemctl start pypi
```

Manual server verification:
```bash
# start nginx
service nginx start
# run wsgi
/apps/pypi_repo/venv/bin/uwsgi -H /apps/pypi_repo/venv --master --processes 4 --threads 2 --http :5000 --manage-script-name --python-path /apps/pypi_repo --mount /=wsgi:app
# check connection 
http localhost:5000
```

Manual service setup:
```bash
# setup wsgi
cp /apps/pypi_repo/server/pypi.service /etc/systemd/system/pypi.service
systemctl start pypi
systemctl status pypi
systemctl enable pypi  # run service during startup
reboot

# setup nginx
rm /etc/nginx/sites-enabled/default
cp /apps/pypi_repo/server/pypi.nginx /etc/nginx/sites-enabled/pypi.nginx
update-rc.d nginx enable
service nginx restart
```

### Meta

Author – _Vladimir Yahello_. Please check [authors](AUTHORS.md) file for more details.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/pypi/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#pypi-clone)**
