# async-api-sample

![image.png](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F285581%2F3a108dac-492c-77d2-7a09-f436b36a84b7.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=431dea4312fbb81c65bd3cb402934944)

## Requirement
```
serverless-framework
```

```yml
plugins:
  - serverless-step-functions
  - serverless-pseudo-parameters
```

## Usage
### Deployment
```shell
serverless deploy --stage $ENV
```

### How to use

```shell
# Set Api Endpoint
StartExecution=https://XXXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/dev/ramen/start-execution
DescribeExecution=https://XXXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/dev/ramen/describe-execution
```

```shell
# StartExecution
executionArn=$(curl -X POST -d '{"input1": "test1", "input2": "test2"}' $StartExecution | jq -r '.executionArn')

# DescribeExecution
curl -X POST -d '{"executionArn": "'$executionArn'"}' $DescribeExecution | jq
```
