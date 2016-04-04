
Start server 
```ruby
rackup -p 4567
rackup -p 4567 -h 0.0.0.0
```

Call VIEWS 

```ruby
get '/' do
  erb :hello_world
end
```

## Mongo with Sinatra
1. [Mongo Model] (http://recipes.sinatrarb.com/p/models/mongo)

```bash
sudo apt-get install mongodb
```

```ruby
gem install mongo
gem install mongodb
```

Migrate database

```ruby
rake db:create_migration NAME=create_public_bookmarks

```

2. [Mongo-Ruby driver] (https://github.com/mongodb/mongo-ruby-driver/wiki/Tutorial)
3. [MongoDB-Ruby driver] (http://docs.mongodb.org/ecosystem/drivers/ruby/)
4. [MongoMapper - Don't repeat] (https://speakerdeck.com/jnunemaker/dont-repeat-yourself-repeat-others)
5. [Mongo-Sinatra] (http://spf13.com/presentation/building-your-first-mongodb-app-in-ruby-strangeloop-2013/)
6. Mongo API - Document : http://docs.mongodb.org/ecosystem/tutorial/ruby-driver-tutorial/#ruby-driver-tutorial




