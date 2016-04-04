# Express JS

1. [Route](Route.md)
2. Third-party Node modules: 
  * [Connect to Backend] (StrongLoop.md) 
3. [Template Engine](Consolidate.md): **need more research on each template engine to understand pro and corn**
  * [Use template engine](http://expressjs.com/guide/using-template-engines.html)
  * [Define new template engine](http://expressjs.com/advanced/developing-template-engines.html)
  * 
5. Serve static files from several directories
 * With the following middleware setup, and a request for GET /javascripts/jquery.js, the first check would be ./public/javascripts/jquery.js; if it does not exist, then the subsequent middleware will check ./files/javascripts/jquery.js.
 ```
 app.use(express.static('public'));
 app.use(express.static('files'));
  ```
 6. Prefix a pathname for serving static files
 ```
 app.use('/public', express.static('public'));
 ```
7. [Error handling](http://expressjs.com/guide/error-handling.html)
 * Handle 404s
 ```
 app.use(function(req, res, next){
   res.send(404, 'Sorry cant find that!');
 });
 ```
 * Define error handle: Define error-handling middleware like other middleware, except with four arguments instead of three, specifically with the signature (err, req, res, next)):
  ```
  app.use(function(err, req, res, next){
   console.error(err.stack);
   res.status(500).send('Something broke!');
 });
 
 app.use(logErrors);
 app.use(clientErrorHandler);
 app.use(errorHandler);
 
 function logErrors(err, req, res, next) {
   console.error(err.stack);
   next(err);
 }
 
 function clientErrorHandler(err, req, res, next) {
   if (req.xhr) {
     res.status(500).send({ error: 'Something blew up!' });
   } else {
     next(err);
   }
 }
 
 function errorHandler(err, req, res, next) {
   res.status(500);
   res.render('error', { error: err });
 }
  ```
8. Render plain HTML
 * If you have a specific file, use res.sendFile(). If you are serving many assets from a directory use the express.static() middleware.
9. [Moving (migration) Express 3 to Express 4] (http://expressjs.com/guide/migrating-4.html): **need more research how to implement, what changes in Express 4**
10. [Debugging] (http://expressjs.com/guide/debugging.html)
 ```
 npm install debug
 
 $ DEBUG=express:* node index.js
 
 set DEBUG=express:* & node index.js
 
 DEBUG=express:* node ./bin/www
  express:router:route new / +0ms
  express:router:layer new / +1ms
  express:router:route get / +1ms
  express:router:layer new / +0ms
  
  express sample-app
  DEBUG=sample-app node ./bin/www
  
  DEBUG=http,mail,express:* node index.js
 ```

11. [Express behind proxy](http://expressjs.com/guide/behind-proxies.html) **need more research**
12. Middleware
 * [Using middleware](http://expressjs.com/guide/behind-proxies.html) **need more research**
 * [Third Party Middleware](http://expressjs.com/resources/middleware.html)
13. [Express application sample](https://github.com/strongloop/express/tree/master/examples?_ga=1.197094316.1248229465.1419587235)
14. Security **need more research**
 * Injection Vulnerabilities (JavaScript, SQL, Mongo, HTML)
 * Session fixation and hijacking
 * Cross-Site Vulnerabilities (Scripting, Request Forgery)
 * Mass Assignment 
 * Excellent talk (11/2012): http://lanyrd.com/2012/asfws/sxzbm/ (see slides)
 * ServerFault question (2011-2012): http://serverfault.com/questions/285123/is-node-js-mature-for-enterprise-security
 * Blog post on topic (9/2012): http://codefol.io/posts/29-Why-Rails-and-not-Sinatra-or-Node-js-
 * Exploit tester: https://code.google.com/p/skipfish/
 * Passport Module: https://github.com/jaredhanson/passport
 * EveryAuth Module: https://github.com/bnoguchi/everyauth
 * [Writing security Express app](https://blog.liftsecurity.io/2012/12/07/writing-secure-express-js-apps)
 * [Express secure skeleton](https://github.com/evilpacket/express-secure-skeleton)
 * [csrf](http://www.senchalabs.org/connect/csrf.html): CRSF protection middleware.
 * [helmet](https://github.com/helmetjs/helmet): Middleware that implement various security headers
 * Sites
  * http://blog.liftsecurity.io/tag/security
  * 
