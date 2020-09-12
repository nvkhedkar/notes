# Python

#### Installation for certificate issue
Final options:
```
pip install --default-timeout=1000 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org <package-name>
```

#### Strategy and command pattern python
[Strategy and command pattern](https://medium.com/@rrfd/strategy-and-command-design-patterns-wizards-and-sandwiches-applications-in-python-d1ee1c86e00f)

#### New Miniconda stuff
Use Miniconda prompt to do `conda install` or `conda create`  

## Links
[https://l7.curtisnorthcutt.com/about](https://l7.curtisnorthcutt.com/about) - deep learning Ph.d student, confident learning framework  

## Gnuicorn
#### Start flask server
```
gunicorn -w 4 --reload -b 0.0.0.0:8001 "app.main:create_app(testing=False)"
```
- -w: Number of workers
- --reload: Reload automatically when files are changed
- -b: Location of the flask app
