# Run app

Microservice created with FastAPI to get order of tasks for build by name.

Create virtual env for this project via command:

```
python3 -m venv venv
```

Activate it:

- Windows:

```
venv\Scripts\activate
```

- Linux

```
source venv/bin/activate
```

Installing requirements:
```
pip install -r requirements.txt
```

Run service:
```
uvicorn main:app
```

Now service running at [localhost:8000](http://localhost:8000/) as default. Visit this link to get Swagger documentation of service.

And now you can test /get_tasks endpoint using Swagger Doc or using curl query like (replace build_name):
```
curl -X 'POST' \
  'http://localhost:8000/get_tasks' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "build": "build_name"
}'
```
