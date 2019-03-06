# Final Project
## Welcome to GoTrees!

#### Introduction

**GoTrees** is a small web-application with the aim of making people more responsible and participative about environment. The idea is to turn this into a game by leaving to the users the opportunity to create their own virtual forest, which are virtual at the same time that are real, winning badges and getting discounts or gifts.

**In essence** after being create their user accounts they will be ably to go to the countryside with their own little trees and plant then there where they want and can. They can get points for every tree they plant and with those points they have options of getting coupons with discounts or gifts by external Companies or local business.

#### Let's go Through the Files

Inside the main folder 'Trees', we have two other folders: 'gotrees' and 'Trees'.

##### Trees

In the last one are all the root files created by Django when initializing a new project. In urls.py I've *include* the paths for my application 'gotrees', so I can edit my paths directly in the urls.py within my application's folder.

In DATABASES I've used a postgresql db hosted in Heroku to continue be more familiarized with those database.

##### gotrees

Here in the other folder is mostly everything. I'll try to explain the most relevant.

In **models** are all my models. Profiles for info relative to the users, Trees with the data for every tree, Badges to store which badges are active or inactive for every user, TreeCodes is to build an idea I had about getting one unique code for every single tree, to make harder to lie when submitting and planting 'new trees'. In offers I store all the data for the companies promotions.

**Helpers** is a file where I wrote three functions to make it easier for the views in views.py. The first is for upload images, the second is to fetch all data about a user in order to render later all that in the user's profile page, and the last one if for checking the actual history of badges of the user.

**Views** is the biggest file I wrote. Here we have all the views for the web application. The basics like 'index' page, to 'register' a user, to 'login' or 'logout'.

Also 'myforest' view. Here using one of the helpers functions I gather all data about a user to create a profile page with all important info about that user. Other users can see it but can not edit that data. Also they can see that user's virtual forest but can not delete trees for example. Many of that is happening with JavaScript so not so much to see in this view.

In edit profile user can change their data, user can only change their data not someone else, and here as in 'myforest' they have their unique url.

'new_tree' is the place where receive the data from the little form when *planting* a new tree. Here lat and lng are stored so trees can be represented in the map at their correct places.

'treecodes' is the view where a unique code is created for every tree. This is a step-first a user must do before go to the fields to plant. They need to generate one code for every tree and in the photo when *planting* that tree must appear that code so it's possible to have more control about the trees are planted. This code is created using some user data and datetime values.

'offer', 'myoffers' and 'coupon' are all relative to the idea of getting discounts with the points of planting more trees. Here points are subtracted, offers are show and coupons are also show.

The last three views are not for render templates but to serve data for XMLHttpRequest made using JavaScript and are all about the google maps and how to collect and show data relative to the virtual trees.

**Templates**

All the HTML code for the templates.

'index' is one of interest. There is a section where appear some nice info about last people that are planted trees. This information is updated every time the index page is render, and it's shown letting see the image of the user and the kind of three she or he planted with the dedication in the case it exist.

After that there is a section with 'cards' where will be easy to show some examples of companies who are supporting the project and their gifts of promotions.

Then we have the map. There are shown all virtual trees, at the place where they were planted using the Google API for JavaScript. The map is updated at every time the map is dragged or zoomed so it's doesn't overload the server for requesting all possible thousand trees.

In the map, when making click on the icons you can see info about that tree, and who planted it for example, and you can go visit his or her profile. Also every icon is different depending the kind of the tree, like for example evergreen trees or bushes are different.

Other template is 'myforest', what is thought to be like a simple user profile page. There are options to edit the data and to upload an image that is automatically resized to fit in the nice frame at the left. All that using JavaScript. As said before there is a map here too, but this is only to show that user's trees.
At the bottom of the page, there is a slideshow for offers, when clicking on you can go to the page where is possible to get that offer spending the amount of points necessary.

'treecodes' is other interesting template. Here the unique code generated by the view 'treecodes' are rendered in a nice appearance. The idea here is to print that page and cut with scissors in little pieces in order to let them appear in the photos with the already planted threes.

**Static**

This project has been making use of a local copy of Bootstrap stylesheets plus an customized stylesheet also stored in this folder. In addition to stylesheets, here are 'img' for images used in the structure of the application, 'offers' only for promotional banners, 'coupons' for coupons, and 'uploads' for user's profile images.

In helpers.js I implemented a function to make it easier all XMLHttpsRequest needed for the maps. Besides to give the url and the data to be send it's also necessary to provide the csrf token needed in Django.
