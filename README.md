# whackfall2017
Project for WHACK Fall 2017
## Inspiration
One night in New York City, we saw a man eating a raw chicken leg out of a garbage bag. We realized that large institutions, 
such as colleges and universities, compost huge amounts of relatively safe, edible food at the end of each day. We wanted to 
come up with an easy way for such large institutions to make this food available to people in need, while also accommodating s
maller drops of food left over from events. From a social standpoint, we hope to reduce extreme hunger and allow people who 
can’t afford food to eat relatively fresh and presentable food, affording them greater dignity than dumpster diving. Our 
ecological goal is to eliminate food waste in America. Therefore, we decided to create a web app called Froodees, a portmanteau
of the words “free” and “foods.”

## What it does
Upon navigating to the website, a person can indicate that they have food they are looking to get rid or or that they are 
looking for food.

If a person has food, they insert the location they are going to leave it at and an estimate of how many servings they are 
leaving. This information, along with the timestamp of when they said they were leaving the food, is stored in a JSON file on 
the server.

If a person says they are looking for food, they are directed to a page that asks for their current location. Then, using 
Google Maps API, a static image of the person’s vicinity is displayed. This image has markers at all locations that have had 
food left at them.

## How we built it
The front-end templates were built with HTML and CSS. We used Canva, an poster/ logo making website, where I created each 
graphic and uploaded the pictures as URL’s that can be embedded into the HTML code. We used a google font to make the written 
portion consist and aesthetically pleasing. The back-end was built with Flask. At present, Froodie is run from localhost.

## Challenges we ran into
We ran into many obstacles in building this application, such as being able to display a user’s location who was seeking food 
relative to locations where food was dropped off. We had to figure out a way to use Google Maps API in order to do so, 
although we began by attempting to have a dynamic map that moved and was interactive, we were unable to integrate the server 
aspect as well. In order to still be able to display a map along with the information we wanted, we settled into using a 
static image that was generated using a user’s location. 

## Accomplishments that we're proud of
The accomplishment that we’re most proud of is using Flask, which is new to all of us, to create the back-end of our webapp 
and run it, albeit from localhost. We also learned how to use Javascript to add the Google Maps API. We are very proud of the 
fact that Froodie is functional; we are also proud of the images and design of the site.

## What we learned
Every member of this team learned a new skill this weekend. For some, it was HTML, for others, CSS or Javascript, and for 
others, Python and server-side coding. We learned how to use the Google Maps API as well. We are all relatively new to 
hackathons and to CS, with three of us being first-time hackers, one of us being a first-time coder, and all four of us being 
first years, and are very proud of the project we were able to complete this weekend. 

## What's next for Froodie
It is an unfortunate fact that the internet is full of trolls. Froodie has no measures in place to discourage or prevent 
trolling. Before this could be usable on a large scale, we’d want to prevent people from adding food to locations that aren’t 
near their current location, or from spam-adding locations. We also want to add a feature where we can let users upload images 
of the food when they indicated that “they have food.” Also, to eliminate inconvenience, we would add timestamps by the 
picture and have an icon that could count interest level for specific foods. This would help avoid too many people coming for 
the same food. We also assume that after a few hours the food would be either gone or spoiled, and would like to automatically 
be removed from the database at that time. In the distant future, we hope to have a strong mobile app to accompany the web 
app.
