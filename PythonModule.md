## Common Modules in Python 
### Database:
- Alembic : upgrade, downgrade
- SQLAlchemy : Query, model

###  Framework:
- Flask

###Date
- python-dateutil

### Python format
https://pyformat.info/

###Request
A user requests the following URL:

    http://www.example.com/myapplication/page.html?x=y
In this case the values of the above mentioned attributes would be the following:

    path             /page.html
    script_root      /myapplication
    base_url         http://www.example.com/myapplication/page.html
    url              http://www.example.com/myapplication/page.html?x=y
    url_root         http://www.example.com/myapplication/

###Unit Test
- Jasmine
- Mocha
- Nose
```
 nosetests --with-coverage --cover-html test/scheduler/test_create_job.py
 python -m unittest discover
 ```
### Scheduler (Cron jobs)
- APScheduler

### Docker
- docker
- 
### Monitor folder:
- https://github.com/gorakhargosh/watchdog
- https://github.com/seb-m/pyinotify/wiki/Tutorial
- http://aws.amazon.com/blogs/aws/s3-event-notification/
 - Amazon Simple Notification Service Developer Guide http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html 
 - Create ARN Queue : http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/CreatingQueue.html
 - Python SQS Queue http://boto.readthedocs.org/en/latest/sqs_tut.html
 - Lambda Function http://aws.amazon.com/lambda/faqs/
 - http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html 
 - http://docs.aws.amazon.com/lambda/latest/dg/lambda-introduction.html
 - 
 ```
 console.log('Loading event');
var aws = require('aws-sdk');
var s3 = new aws.S3({apiVersion: '2006-03-01'});

exports.handler = function(event, context) {
   console.log('Received event:');
   console.log(JSON.stringify(event, null, '  '));
   // Get the object from the event and show its content type
   var bucket = event.Records[0].s3.bucket.name;
   var key = event.Records[0].s3.object.key;
   s3.getObject({Bucket:bucket, Key:key},
      function(err,data) {
        if (err) {
           console.log('error getting object ' + key + ' from bucket ' + bucket + 
               '. Make sure they exist and your bucket is in the same region as this function.');
           context.done('error','error getting file'+err);
        }
        else {
           console.log('CONTENT TYPE:',data.ContentType);
           context.done(null,'');
        }
      }
   );
};

 ```
 
- http://boto.readthedocs.org/en/latest/sqs_tut.html
 

 ```python
 https://<keyword-company>.signin.aws.amazon.com/console
MA2uw&Iwa3oy 
 ```

### Coding Standard
- Pylint
 
 ```python
 pylint --help
 pylint --rcfile=standard.rc --output-format=html --reports=y portal/apis > pylintResult.html
 ```
### Python debug
https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
```
import pdb
pdb.set_trace()
```
1. Execute the next statement… with “n” (next)
2. Repeating the last debugging command… with ENTER
3. Quitting it all… with “q” (quit)
4. Printing the value of variables… with “p” (print)
5. Turning off the (Pdb) prompt… with “c” (continue)
6. Seeing where you are… with “l” (list)


Python login sample: https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/

## Common function 
1. Get type of variable : 

```
N = [2,3,5]
P = 5

type(N).__name__ == 'list'
True

type(P).__name__ == 'int'
True
```
2. Between 2 numbers

```
r=range(1,4)

>>> 2 in r
True
>>> 1 in r
True
>>> 5 in r
False
>>> 0 in r
False
```
3. length of integer

```
>>> a=12345
>>> a.__str__().__len__()
5
```

4. [yield](http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

