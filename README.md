OrderAPI
========
<p>This is what the internal API for an ecommerce business might look like. This system allows you
to create and store orders in a database and associate them with customers and various related metadata. Features include
basic authentication and a web browsable API. All responses return json by default and html when opened in a browser. 
For sake of convenience, most fields have been made optional, so you can create an order with just empty dict {}. </p>

<h2>Authentication</h2>
<p>This api uses basic authentication. For testing purposes, use this login:</p>
<h5>Username: test</h5>
<h5>Password: test</h5>

<h2>Web Browsable API</h2>
<p>This is a web browsable API, which means if you visit an endpoint from your browser, you'll see a nice gui representation of the API, returned in html. Try it out - visit https://orderapi.herokuapp.com/api/orders/ </p>

<h2>Response Format</h2>
<p>If you'd like to bypass the web browsable api and return JSON from your browser, then add '.json' at the end of the path like so:</p>
``` orderapi.herokuapp.com/api/orders/.json ```
<p>You may also pass in the format like so:</p>
``` orderapi.herokuapp.com/api/orders/?format=json ```
<p>Conversely, if you'd like to return HTML programatically, then add '.api' at the end of the path.</p>

<h2>Endpoints</h2>
<h6>Root URL: https://orderapi.herokuapp.com</h6>
Method | Endpoint          | Description                 | Example
-------|-------------------|-----------------------------|-------------------------------
GET    | /api/orders/      | Gets a list of all orders   | ``` curl -i orderapi.herokuapp.com/api/orders/ -u test:test```
POST   | /api/orders/      | Creates a new order         | ``` curl -i -X POST -d '{}' orderapi.herokuapp.com/api/orders/ -u test:test ```
GET    | /api/orders/{id}/ | Gets detailed view of order | ``` curl -i orderapi.herokuapp.com/api/orders/1/ -u test:test ```
PUT    | /api/orders/{id}/ | Updates an order            | ``` curl -i -X PUT -d total_price=20.57 orderapi.herokuapp.com/api/orders/1/ -u test:test ```
DELETE | /api/orders/{id}/ | Deletes an order            | ``` curl -i -X DELETE orderapi.herokuapp.com/api/orders/1/ -u test:test ```
||
GET | /api/customers/ | Gets a list of all customers | ```curl -i orderapi.herokuapp.com/api/customers/ -u test:test ```
POST | /api/customers/ | Creates a new customer | ```curl -i -X POST -d "first_name=foo&last_name=bar&email=foo@bar.com" orderapi.herokuapp.com/api/customers/ -u test:test ```
GET | /api/customers/{id}/ | Gets detailed view of customer | ```curl -i orderapi.herokuapp.com/api/customers/1/ -u test:test ```
PUT | /api/customers/{id}/ | Updates a customer's info | ```curl -i -X PUT -d first_name=john orderapi.herokuapp.com/api/customers/1/ -u test:test ```
DELETE | /api/customers/{id}/ | Deletes a customer | ```curl -i -X DELETE orderapi.herokuapp.com/api/customers/2/ -u test:test ```

<h2>Local Testing</h2>
<p>Follow these instructions if you'd like to run this api locally.</p>
<ol>
  <li>Clone repo.</li>
  <li>From project root, run:</li>
</ol>
```
>> $ source venv/bin/activate
>> (venv) $ python manage.py syncdb
...
>> (venv) $ foreman start
17:09:33 web.1  | started with pid 24227
17:09:33 web.1  | [2014-11-28 17:09:33 -0600] [24227] [INFO] Starting gunicorn 19.1.1
17:09:33 web.1  | [2014-11-28 17:09:33 -0600] [24227] [INFO] Listening at: http://0.0.0.0:5000 (24227)
17:09:33 web.1  | [2014-11-28 17:09:33 -0600] [24227] [INFO] Using worker: sync
17:09:33 web.1  | [2014-11-28 17:09:33 -0600] [24230] [INFO] Booting worker with pid: 24230
```
