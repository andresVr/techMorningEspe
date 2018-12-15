# Lab setup guide

This guide was made to be used on Ubuntu 16.04

## Verify python 3 installation

```
python3 --version
```

If python3 is not installed, follow any [installation guide](https://docs.python-guide.org/starting/install3/linux/).

## Install dependences

Install PIP with apt:

```
sudo apt-get install -y python3-pip
```

Install Virtualenv:

```
pip3 install virtualenv 
```

Create a virtualenv:

```
virtualenv reservation app
```

Activate virtualenv:

```
source venv/bin/activate
```

Install prerequisites:

```
pip3 install -r requirements.txt
```


## Test project

```
cd tech_mornings
./manage.py runserver
```

You should see something on http://localhost:8000
