# Project 3

## Web Programming with Python and JavaScript

In this project we're going to implement a web app where users can open an account, select some food from the available options and once done, go to the cart and simulate a payment using Stripe.

Into project3 there are two folders, in **pizza** our *SQLite3* database is configured, also our app *order* has been included in the INSTALLED_APPS, and in urls.py, an *include* redirect to our urls.py within the *orders* app.

At the other folder, **orders** we find our *views.py*. There we have our 'index', 'login_page', 'logout_page' and 'register' basic functions.
Also there is one view for every kind of food. Each of one is responsible to render all the data relative to that kind of food. So for example we have 'pizzas' to request to the database for all data relative to pizzas, or 'subs', for all data concerning subs, and so on.

Then we have 'added'. Which look more complex than the others. Here is where all actions of add new items to an order is executed. I've been using many `try`  because never is going to be a request with all kinds of food so I only take what matters and reduce to None all the other so I don't get errors in the next steps.

Once the order is created I add all extras based in ManyToMany fields and save it again. I also used a session variable called 'blue_cart', this is to switch to blue the cart icon. It's in blue when the user has orders and gray when not. This change of color is executed both from the server side as per JavaScript to make the change instant.

In 'cart', we find a simple view where all orders belonging to a user are requested and sent to render. A total amount is shown to let the user know the expenses.

'delete' takes care of receive the signal for deleting a row within the 'cart'. That's delete a order. When there is not other order in the 'cart' a special signal is sent, 'no-content', this will cause the cart icon to turn gray again.

The last one is 'checkout', which is my personal extension together with the code in the client side with the same purpose.

There are to streams here, if request.method is POST or not. In the first case a payment issue is issued. 'stripToken' is provided by Stripe, the amount is adjusted depending the order's volume and username is provided too. Then the charge is executed in usd dollars and a customized description is added to the payment for reference.

The other part of the view is when the method is GET. This is after the payment and all the 'orders' are now copies as 'confirmations' so the Restaurant Owner can see each of then in different tables.

The 'order_status' is set to *Confirmed* in the 'confirmation' just for clarify. The old 'orders'  are then all deleted.

At the end all confirmation data relative to that user is gather and send to render.

Other file, *urls.py* contain all internal path in the application and relates then with specific views.

*models.py* contains my models. One for each kind of food (pizza, sub, saldas, pasta, dinner platters, toppings, additions) and I difference between prices for Sicilian and Neapolitan pizzas. Two more models are established. One for orders which is able to contain all additions or toppings too, and other for Confirmations, just for easily difference between what is already paid and what is not.

In *admin* my models are registered so are visible from the admin app.

Then changing to other folder **static**, there we have another folder for bootstrap-4 files, from where mostly all CSS for the app is charged. Also img, for images in general.
Besides we have styles.css with custom CSS and make_order.js. This code is used in part of the templates, specially those who don't have extra options, additions or toppings, and help to make it easier the code in those templates. This control also the change of color for the cart icon.

Finally the **template** folder, containing all html and good part of the JavaScript.

There is a template for each kind of food, those with additions and toppings are a bit more elaborated due to the steps of choosing those extras. In these cases I opted to use modals (thanks to Bootstrap), with modal is easy to extend the options and make them appear when necessary.

In 'pizzas' for example, I had to check for option chosen how many toppings were available, and then clone the select field to let the user choose the available options, and then once done, append all of then to the XMLHttpRequest. On the other hand, if Cheese Pizza would be chosen, no options will appear and the process will be easier.

Something very similar to that happens in 'subs', but in this case to chose the 'Additions' and taking care of make the difference between those dish which accept additions and those who only have cheese as extra.

Then in 'cart' a table-like is generated with all orders stored for that single user. I chose to use divs and not a table because I thought it will be easier to make the CSS animation when deleting an item in the list. Actually in my computer Safari's version (which is a bit old) it doesn't work always fine, however in Google Chrome is always right.

Finally, 'confirmation', as briefly described before is the page that appear after the payment is executed, and shows the orders already confirmed for that user.

**Personal Touch**

Here my personal touch has been the implementation of a payment method using Stripe. 
