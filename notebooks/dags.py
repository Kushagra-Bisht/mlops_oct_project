import dagshub

import mlflow

mlflow.set_tracking_uri("https://dagshub.com/Kushagra-Bisht/mlops_oct_project.mlflow")
dagshub.init(repo_owner='Kushagra-Bisht', repo_name='mlops_oct_project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

#token =b7cdd6a7f1c7cfd93d88dfbbc0322e6084f18a45