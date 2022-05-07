# fourthbrain-mlops03-week4
fourthbrain-mlops03-week4


### Steps to install and operate Dockerized sentiment app
Clone Git repository
``` bash
git clone https://github.com/tearheart/fourthbrain-mlops03-week4.git
```

`cd` into new directory `fourthbrain-mlops03-week4`
``` bash
cd fourthbrain-mlops03-week4
```

Build Docker image (this may take a few  minutes)
``` bash
docker build -t mlops_week4:1.0 .
```

Run Docker container with newly created image `mlops_week4:1.0`
``` bash
docker run -p 8000:8000 mlops_week4:1.0
```

Go to web browser location `127.0.0.1:8000` to see initial root end point

Go to `127.0.0.1:8000/docs` to try out the sentiment analysis functionality.  Click on `POST /sentiment` then `Try it out`.  In the `Request body` section, replace `"string"` with the sentence you want to test.  For example "Sentiment analysis is really cool".  Then hit `Execute` to get the sentiment results.

```
"Sentiment test: Sentiment analysis is really cool == [{'label': 'POSITIVE', 'score': 0.9998300075531006}]"
```
