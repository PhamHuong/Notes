# NodeJS Route

* Basic routing
```
// respond with "Hello World!" on the homepage
app.get('/', function (req, res) {
  res.send('Hello World!');
})

// accept POST request on the homepage
app.post('/', function (req, res) {
  res.send('Got a POST request');
})

// accept PUT request at /user
app.put('/user', function (req, res) {
  res.send('Got a PUT request at /user');
})

// accept DELETE request at /user
app.delete('/user', function (req, res) {
  res.send('Got a DELETE request at /user');
})
```
* restful-router https://github.com/expressjs/restful-router
* Routing list https://github.com/strongloop/express/blob/master/examples/route-separation/index.js?&&_ga=1.256188939.1248229465.1419587235#L19
```
/**
 * Module dependencies.
 */

var express = require('../..');
var app = express();
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');
var site = require('./site');
var post = require('./post');
var user = require('./user');

module.exports = app;

// Config

app.set('view engine', 'jade');
app.set('views', __dirname + '/views');

/* istanbul ignore next */
if (!module.parent) {
  app.use(express.logger('dev'));
}

app.use(methodOverride('_method'));
app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));

// General

app.get('/', site.index);

// User

app.get('/users', user.list);
app.all('/user/:id/:op?', user.load);
app.get('/user/:id', user.view);
app.get('/user/:id/view', user.view);
app.get('/user/:id/edit', user.edit);
app.put('/user/:id/edit', user.update);

// Posts

app.get('/posts', post.list);

/* istanbul ignore next */
if (!module.parent) {
  app.listen(3000);
  console.log('Express started on port 3000');
}
```
* Route map https://github.com/strongloop/express/blob/master/examples/route-map/index.js?_ga=1.256188939.1248229465.1419587235#L47
```
/**
 * Module dependencies.
 */

var express = require('../../lib/express');

var verbose = process.env.NODE_ENV != 'test';

var app = module.exports = express();

app.map = function(a, route){
  route = route || '';
  for (var key in a) {
    switch (typeof a[key]) {
      // { '/path': { ... }}
      case 'object':
        app.map(a[key], route + key);
        break;
      // get: function(){ ... }
      case 'function':
        if (verbose) console.log('%s %s', key, route);
        app[key](route, a[key]);
        break;
    }
  }
};

var users = {
  list: function(req, res){
    res.send('user list');
  },

  get: function(req, res){
    res.send('user ' + req.params.uid);
  },

  delete: function(req, res){
    res.send('delete users');
  }
};

var pets = {
  list: function(req, res){
    res.send('user ' + req.params.uid + '\'s pets');
  },

  delete: function(req, res){
    res.send('delete ' + req.params.uid + '\'s pet ' + req.params.pid);
  }
};

app.map({
  '/users': {
    get: users.list,
    delete: users.delete,
    '/:uid': {
      get: users.get,
      '/pets': {
        get: pets.list,
        '/:pid': {
          delete: pets.delete
        }
      }
    }
  }
});

/* istanbul ignore next */
if (!module.parent) {
  app.listen(3000);
  console.log('Express started on port 3000');
```
* Route middleware https://github.com/strongloop/express/blob/master/examples/route-middleware/index.js
* Namespace Route https://github.com/expressjs/express-namespace?_ga=1.196479916.1248229465.1419587235
```
GET /forum/12
GET /forum/12/view
GET /forum/12/edit
GET /forum/12/thread/5
DELETE /forum/12

app.namespace('/forum/:id', function(){
  app.get('/(view)?', function(req, res){
    res.send('GET forum ' + req.params.id);
  });

  app.get('/edit', function(req, res){
    res.send('GET forum ' + req.params.id + ' edit page');
  });

  app.namespace('/thread', function(){
    app.get('/:tid', function(req, res){
      res.send('GET forum ' + req.params.id + ' thread ' + req.params.tid);
    });
  });

  app.del('/', function(req, res){
    res.send('DELETE forum ' + req.params.id);
  });
});
```
