# Node.js framework for creating APIs and easily connecting to backend data sources. (StrongLoop)
* http://loopback.io/?_ga=1.188556072.1248229465.1419587235
* Package command line
  ```
  slc loopback:model
  ```
* Connect to database
  * MySQL : http://docs.strongloop.com/display/public/LB/Connect+your+API+to+a+data+source
  ```
  slc loopback:datasource
  ```
   * Install MySQL connector
   
    ```
     npm install loopback-connector-mysql --save
    ```
   * Configure data source: Edit /server/datasources.json
   
   ```
   {
     "db": {
       "name": "db",
       "connector": "memory"
     },
     "mysqlDs": {
       "name": "mysqlDs",
       "connector": "mysql",
       "host": "demo.strongloop.com",
       "port": 3306,
       "database": "demo",
       "username": "demo",
       "password": "L00pBack"
     }
   }
   ```
   * Connect CoffeeShop model to MySQL
   
   ```
   "CoffeeShop": {
     "dataSource": "db",
     "public": true
   }
   ```
   * [Creating a database schema from models](http://docs.strongloop.com/display/public/LB/Creating+a+database+schema+from+models)
   * [Define remote methods](http://docs.strongloop.com/display/public/LB/Remote+methods)
   * [Add a static web page](http://docs.strongloop.com/display/public/LB/Add+a+static+web+page)
   * [Define boot script](http://docs.strongloop.com/display/public/LB/Defining+boot+scripts)
   * [Tutorial and Examples](http://docs.strongloop.com/display/public/LB/Tutorials+and+examples)
   * [Execute Native SQL](http://docs.strongloop.com/display/public/LB/Executing+native+SQL)
   * [Version API](Versioning your API)
   * 
