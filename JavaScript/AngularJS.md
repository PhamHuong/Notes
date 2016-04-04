# AngularJS from codeschool.com 
* http://campus.codeschool.com/courses/shaping-up-with-angular-js/level/1/section/1/creating-a-store-module
* https://www.codeschool.com/courses/staying-sharp-with-angular-js/?utm_medium=email&utm_campaign=course_complete&utm_source=mandrill&utm_content=null 

1. Module: ng-app
2. Controller: ng-controller
3. If/Expression: ng-show, ng-hide, ng-if
4. Loop/Repeat: ng-repeat
5. Filter: | currency, | date('dd-mm-YYYY')
6. Length array: product.images.length
7. Tab: ng-init, ng-click, ng-show

  ```javascript
  ng-init="tab =1 "
  ng-click="tab=1"
  ng-show="tab === 1"
  ```

8. ng-class="{[class]:[expression]}"

  ```javascript
  ng-class = "active: tab ===1"
  ```
9. ng-model: binds the form element value to the property
10. ng-options="stars for stars in [5,4,3,2,1]" 
11. form ng-submit="[controller].[method]"
12. Form validation : 

  - Turn off default HTML validation: novalidate
  - Required field: required
  - form validation - return true/false : {{[formName].$valid}}}
  - Email:
  - Url:
  - Number:

13. Directive View: Include file in html: 
  - ng-include="'[filename.html]'" 
  - as an a tag:  <[filename]></[filename]
  - as an attribute: <h3 [filename]></h3>

  ```javascript
  <product-title></product-title>
  app.directive("productTitle", function(){
    return {
      restrict: 'E', 
      templateUrl: 'product-title.html'
    };
  })
  
  <h3 product-title></h3>
  app.directive("productTitle", function(){
    return {
      restrict: 'A', 
      templateUrl: 'product-title.html'
    };
  })
  ```
14. Directive Controller 
  
  ```javascript
  app.directive("productTitle", function(){
      return {
        restrict: 'A', 
        templateUrl: 'product-title.html',
        controller: function(){
        },
        controllerAs: "[aliasName]"
      };
    })
  ```

15. Services
    ```javascript
    $http({method: "POST/GET/DELETE/", url: "<api-url>"});
    
    $http.get("<api-url>", {apiKey: "myAPIKey"})
    
    ```
16. Scope
   ```javascript
    scope: {
        name: "@",
        color: "=",
        reverse: "&"
    }
   "@"   (  Text binding / one-way binding )
   "="   ( Direct model binding / two-way binding )
   "&"   ( Behaviour binding / Method binding  )
  ```  
17. Factory, Service, Provider

 


16. Angular API: https://docs.angularjs.org/api?PHPSESSID=cae8e98e7ca559b4605d75c813b358ee
17. https://thinkster.io/a-better-way-to-learn-angularjs/
18. https://egghead.io/technologies/angularjs?order=desc&page=20

================================

# LEVEL 2
* Directives With Scope 0/9 Complete
* $SCOPE

   * $scope
   * Scope-a-dope
   * Inline Controller & $scope
   * Outside Controller & $scope
* SCOPE THE CONFIG OBJECT

   * Scope the Config Object
   * Default Scope
   * Setting on Scope
   * A Flexible Card Directive
   * Making Isolation Work for You
* LINK

   * Link
   * DOM Manipulation
   * Style the Tweeted Note
* Placeholder Badge
# LEVEL 3
* Services 0/9 Complete
* A SERVICE FOR OUR DATA CALLS

   * A Service for Our Data Calls
   * A Factory Recipe I
   * A Factory Recipe II
* A SERVICE FOR AN OUTSIDE API

   * A Service for an Outside API
   * A Tweetable Service
   * The Configurable Bits
* PROVIDERS

   * Providers
   * Configurable Bits Need a Provider
   * Configuring the Tweet Length
* $RESOURCE

    * $resource
    * $resource Refactor
    * Using a $resource-ful Note Service
    * A Custom Method for Our Note $resource
* Placeholder Badge
# LEVEL 4
* Reusable Directives 0/9 Complete
* HELPING CHILDREN AND PARENT COMMUNICATE

   * Helping Child and Parent Communicate
   * Glorious Directives for Our Navigation
   * The Parent Is Required
   * Using Parent Functionality
   * The Magic Revealed
* FILTER

   * Filter
   * Filter All the Things
   * Chaining Filters
   * A Date Filter
* EXTERNAL LIBRARY DIRECTIVE

   * External Library Directive
   * Make It Work
   * A Popover for Note Descriptions

