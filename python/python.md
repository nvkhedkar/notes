# Python

## Installation for certificate issue
Final options:
```
pip install --default-timeout=1000 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org <package-name>
```

## Ignore packages while installing
Use the following to avoid packages from being uninstalled and re-installed
```
--ignore-installed <package>
```
## New Miniconda stuff
Use Miniconda prompt to do `conda install` or `conda create`  

## Gnuicorn
### Start flask server
```
gunicorn -w 4 --reload -b 0.0.0.0:8001 "app.main:create_app(testing=False)"
```
- -w: Number of workers
- --reload: Reload automatically when files are changed
- -b: Location of the flask app

## Pandas
### Rearrange columns
Move result columns to the end of all other columns.  
Re-create the dataframe by:
1. Iterate over all columns, but skip result columns
1. Added result columns at the end
```
result_columns = ['res1', 'res2']
df = df[[c for c in df if c not in result_columns] + result_columns]
```

## PySpark
### Pyspark on windows machine
Start master
```
spark-class org.apache.spark.deploy.master.Master
```
Start any number of workers (Master running on spark://192.168.56.1:7077)
```
spark-class org.apache.spark.deploy.worker.Worker spark://192.168.56.1:7077 --memory 2g
```
[Read a postgresql db](https://stackoverflow.com/questions/34948296/using-pyspark-to-connect-to-postgresql)

## Links
- [Strategy and command pattern](https://medium.com/@rrfd/strategy-and-command-design-patterns-wizards-and-sandwiches-applications-in-python-d1ee1c86e00f)  
- [deep learning Ph.d student, confident learning framework](https://l7.curtisnorthcutt.com/about)  
- [Superset plugin](https://www.npmjs.com/package/@superset-ui/plugin-chart-table)
- [Embed Dash in flask](https://hackersandslackers.com/plotly-dash-with-flask/)  
- [ML pipeline with kafka, airflow and MLpipe](https://medium.com/vantageai/keeping-your-ml-model-in-shape-with-kafka-airflow-and-mlflow-143d20024ba6)
- [Flask and angular example](https://realpython.com/flask-by-example-part-1-project-setup/)
- [tune-sklearn - Gid search for scikit learn](https://github.com/ray-project/tune-sklearn)
- [Ray - python supported api for distributed computing](https://docs.ray.io/en/master/)
- [Boruta feature selection](https://www.kaggle.com/residentmario/automated-feature-selection-with-boruta)
- [keras-redis-flask deep learning rest api](https://www.pyimagesearch.com/2018/01/29/scalable-keras-deep-learning-rest-api/)
- [Celery on windows](https://stackoverflow.com/questions/54717597/django-celery-scheduling-daily-tasks-on-windows-server)
- [Celery to Dramatiq tips](https://blog.narrativ.com/converting-celery-to-dramatiq-a-py3-war-story-23df217b426)

