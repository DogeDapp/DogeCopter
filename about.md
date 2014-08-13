---
layout: page
title: About
---

##Tl;dr version:##
Doge obsessed developers attempt to build a semi autonomous quadcopter on a budget for a competition in their spare time.

Before we start:
--
We’re playing around with this project in our spare time. In no way does this resemble the type or quality of work we carry out in our day jobs as members of the IS team at BMT. As a lot of what we do is a bit secret squirrel we don’t have much of a footprint on the web and this is like a verruca or other revolting foot metaphor.

In short, if you are looking at this project and wondering if we are suitable employers or suppliers for you, please shut down your web browser and come and talk to us instead, or go to <www.bmtdsl.co.uk> to find out more. (That website is just a CMS though and not as cool as some of the awesome applications we do).

With that massive caveat over, what’s this all about?


##The Challenge##
Teams design and build a quadcopter to take part in various challenges in our offices. Format is as follows:

-	1 x timed automated race on a pre-programmed route
-	1 x timed manual race on same route
-	Various challenges to test teams and equipment i.e. 
- Hovering within specific range of target 
-	Land on specific target 
-	Navigation through/around various obstacles 
-	
All of the teams get a set budget, and build up and code the copter in their own time. There are teams from around the company with engineering and electronics experience and probably drones and wotnot too. Team Dogecopter is made up of humble coders. Our copter may not fly straight, but hell, we can fix that in code right?


##Team Dogecopter is made up of:##

- Doug McDonald (@dougajmcdonald)
- Richard Caunt
- Gareth Williams
- Henry Wood
- Conrad Jackson
- Luke McHale-Jones

*Doug* is the PM/Lead whatever. Like a true manager, his task seems to be to set up meetings and to repeat what everyone else said to make sure he’s understood what is going on, and some basic adding up. To be fair he also set up the Github repository, but no commits so far...

*Rich* is our resident quadcopter expert. He’s built a few in his time, and lends an air of confidence to the whole project that masks the panic quite well.

*Gareth* is in charge of branding guidelines, and something complicated to do with image recognition. He’s the reason why there is both an Arduino and a Raspberry Pi on board.

*Henry* is our master fabricator, and will craft the team a quadcopter body so beautiful that quadcopters for miles around will want to work out which bit of a quadcopter is the bottom so that they can sniff it.

*Conrad* is in charge of the entire Dogecopter Social Media platform. 

*Luke* was discovered after a nationwide search to find Britain’s top Boris Johnson lookalike. He is currently Gareths assistant. We assume he is plotting to usurp Gareth, but don’t think he has the memes. 

(This whole section was written for that one pun. It's OK, you don't need to thank me)

##Why “Dogecopter”?##

It’s true that this meme has long past its sell by date no matter whether you count in doge years or internet years, but you may have noticed that [Doge][urldoge] lives on in the BMT Web dev team. No-one knows why Gareth is obsessed by Doge, but he’s infected half of the team with his obsession. The other half cringe and watch on as gif wars break out on email threads for days on end. 



[urldoge]: http://knowyourmeme.com/memes/doge

The Plan /// todo

<gannt>

Contact us
We’re always on the lookout for new people to join our team. Hit us up at <https://twitter.com/BMTWebDevs> or whatever communication channel talented developers use nowadays.


<ul>
{% for contributor in site.github.contributors %}
  <li>
    <img src="{{ contributor.avatar_url }}" width="32" height="32" /> {{ contributor.login }}
  </li>
{% endfor %}
</ul>
