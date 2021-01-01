# Python

## Installation for certificate issue
Final options:
```
pip install --default-timeout=1000 --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org <package-name>
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

## Links
[Strategy and command pattern](https://medium.com/@rrfd/strategy-and-command-design-patterns-wizards-and-sandwiches-applications-in-python-d1ee1c86e00f)  
[deep learning Ph.d student, confident learning framework](https://l7.curtisnorthcutt.com/about)  
[Superset plugin](https://www.npmjs.com/package/@superset-ui/plugin-chart-table)
[Embed Dash in flask](https://hackersandslackers.com/plotly-dash-with-flask/)  
[ML pipeline with kafka, airflow and MLpipe](https://medium.com/vantageai/keeping-your-ml-model-in-shape-with-kafka-airflow-and-mlflow-143d20024ba6)
