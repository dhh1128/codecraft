---
title: // Comments on Comments
date: 2012/10/31
slug: comments-on-comments
---

/*

We spend little or no time teaching programmers how to write good comments.

This is surprising, when you consider how often "total lack of comments" or "poor comments" are cited as evidence that certain modules (or the programmer who wrote them) are the worst thing that ever happened to the technoverse.

[caption id="" align="aligncenter" width="500"]<a href="http://xkcd.com/156/"><img alt="" src="http://imgs.xkcd.com/comics/commented.png" height="135" width="500" /></a> Comments shouldn't leave you--or anybody else--mystified. :-) Image credit: xkcd[/caption]

I happen to think that there are much yuckier tech things than poor or missing comments in code. But I still think our general level of comment proficiency is lower than it should be.

Here is my attempt to raise the bar a little.

<strong>Why We Comment</strong>

Sooner or later, most interesting programming problems require a sophisticated mental model of a problem. Building these models is hard work, and once we have them, <em>we are paid to share with our team (or our future selves)</em>.

The best way to share mental models with other engineers is<!--more--> to <a title="Good Code Is Named Right" href="/2012/08/28/good-code-is-named-right/" target="_blank">code with names and syntax that make our meaning crystal clear</a>. But formal expressions often lack the semantic richness, the subtlety, and the scope that we need for full knowledge transfer. So we comment to make sure the sharing succeeds.

It's critical that programmers get this.

Shared mental models make complex software possible. Shared mental models, not lines of code, not patents, are the most valuable embodiment of a company's IP and technical assets. (More about this in another post.)

A programmer that leaves critical knowledge unshared is seriously derelict in her or his duty, no matter how well the code works. I've quoted <a class="zem_slink" title="Martin Fowler" href="http://martinfowler.com/" target="_blank" rel="homepage">Martin Fowler</a> on this point before, but I'll do it again, because he's so, so right:
<blockquote>“Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”</blockquote>
Some of the more <a href="http://stackoverflow.com/questions/184618/what-is-the-best-comment-in-source-code-you-have-ever-encountered" target="_blank">hilarious comments</a> I've ever read are connected with moments when this principle goes out the window. (Go to the bathroom before you read this collection, so you don't wet your pants laughing.)

[caption id="" align="aligncenter" width="400"]<a href="http://xkcd.com/221/"><img alt="" src="http://imgs.xkcd.com/comics/random_number.png" height="144" width="400" /></a> No amount of commenting makes up for a silly algorithm. But you might give another programmer a good chuckle. Image credit: xkcd[/caption]

<strong>How to Write "Good" Comments</strong>

Seriously, make a habit of asking yourself: "What must I explain, that I can't easily say in code, that instills a healthy mental model of this class/module/function/app?" You can't go far wrong it that's your point of departure.

You'll find yourself naturally aligning with guidelines like this:
<p style="padding-left:30px;"><strong>Good comments supplement, never replace, what can be said with code.</strong></p>
<p style="padding-left:60px;">Instead of commenting that something is an "IN" parameter, make it const. Instead of commenting that a parameter should never be null, make it a reference or add a precondition. Instead of commenting the semantics of a variable, give it a name that make its semantics clear. Tools will then enforce what you say, and guarantee that it remains accurate.</p>
<p style="padding-left:60px;">When you have conveyed as much as you can with pure code--and only then--any important aspects of your mental model that don't come across go into comments.</p>
<p style="padding-left:30px;"><strong>Good comments explain the subtle and important, not the obvious or irrelevant.</strong></p>
<p style="padding-left:60px;">The comments of great coders tend to focus on why a particular tradeoff was chosen, what ramifications might surprise the next guy, or where a hidden dependency lurks. Those who follow gain expertise with less battle scars--or else they diagnose old mistakes with greater confidence.</p>
<p style="padding-left:60px;">Because good comments avoid trivia, they tend to remain accurate. Others appreciate their value and buy in to their upkeep. This becomes a way to reinforce effective communication and best practices for an entire team.</p>
<p style="padding-left:60px;">When comments become inaccurate, it is usually an indictment of their relevance, not of sloppy maintainers. Consider the mandated comments in "<a title="How to turn coding standards into epic fails — or not" href="/2012/09/27/coding-standards/">How to turn coding standards into epic fails — or not</a>."</p>
<p style="padding-left:30px;"><strong>Good comments are concise.</strong></p>
<p style="padding-left:60px;">Conscious of their supporting, not starring role, good comments read quickly and get out of the way. (Compare Yegge's silly counter-example in "<a title="example of ridiculously verbose comment" href="http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html" target="_blank">Portrait of a N00b</a>".) Rather than recapitulating an entire RFC, good comments use a hyperlink. They use formats friendly to the IDEs of the team, so you can collapse them as needed. They avoid repetition as much as possible.</p>
<p style="padding-left:30px;"><strong>Comments shouldn't be used to disable code blocks.</strong></p>
<p style="padding-left:60px;">Disabling code is worse than just a departure from the purpose of comments--it's actually a contradiction. When you disable a block of code, you tend to make it harder to understand, because the natural reaction of the next coder will be to wonder why the code is still there at all. And you have to write a (... wait for it ...) comment to explain yourself.</p>
<p style="padding-left:60px;">Commented-out blocks rarely get maintained or re-enabled. They clutter and obscure.</p>
<p style="padding-left:60px;">We have VCS technology, folks. Unless the disabling is very temporary, if you don't want the code to run, <em>delete it</em>. Or if you must retain it for post-mortem purposes, use an #ifdef. Or put it in an inert file and point people there.</p>
<strong>What About  Javadoc, Doxygen, $Id, and // TODO?</strong>

To make automated tools happy, we may be pressured to compromise a bit on the principles I've just offered. Some tools that process code comments complain unless you document every parameter, every return value, every possible exception. IDEs support snippet insertion to facilitate this, which leads to lots of boilerplate comments that have low value. The snippets make warnings go away, which encourages developers to be lazy.

I don't believe in generating documentation outside the code for internal developers, as a general rule. Developers are code-centric. I have never met a single developer that read external documentation on their own codebase (except overviews when they're first learning), but I have met many who think hard about comments left by co-workers. My conclusion is that comments intended only for an internal audience should be prejudiced toward consumption in your team's code editors, not prejudiced toward the needs of external views.

I would accept compromises to comment quality IFF there's an important audience for your functions outside your own internal dev team (e.g., you're writing an SDK), and your tools cannot be made happy with human-driven choices about comments.

*/
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Make thoughtful improvements to one function where you know it's hard for others to build a complete and accurate mental model.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://developers.slashdot.org/story/12/09/07/1241254/comments-on-code-comments" target="_blank">Comments On Code Comments?</a> (developers.slashdot.org)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.bitnative.com/2012/10/22/kill-the-zombies-in-your-code/" target="_blank">Kill the Zombies in Your Code</a> (bitnative.com)</li>
</ul>

---

All I Really Need To Know I Didn&#8217;t Learn In Compugarten &laquo; Codecraft (2012-11-15 08:32:55)

[...] Effective commenting. [...]

---

Daniel (2012-10-31 15:05:30)

I don't think it's a coincidence that people who care about comments usually have battlescars... :-)

---

dougbert (2012-10-31 14:32:43)

Fowler's statement is my motto (separately generated) as well. My first 10  or so years were spent in maintainingsomeone else's code, trying to find a bug in a sea of statements.  Even a tidbit of comment to describe the WHAT the code was trying to do, would save much time "decoding" the HOW of the code back into the WHAT was intended, in order to find "the bug" of the bughunt.

Since code spends the majority of its "life cycle" in the maintenance phase, I found that trying to INFORM/TELL the maintainer of the code WHAT I intended at the time of writing new code to be at least as important trying to tell the computer what I wanted. I have sought to do that ever since.

---

How to turn coding standards into epic fails &#8212; or not | Codecraft (2013-04-18 17:33:45)

[...] Comment what can’t be made obvious. (Example where comment might be helpful: subtle precondition or postcondition on a function. Value: high. Cost: low.) [...]

---

Small Files Are Your Friends | Codecraft (2013-03-21 08:55:51)

[...] I find it telling that codebases with big files are also codebases where people lament the lack of comments the most, for example. Over the years, I’ve become convinced that a simple rule of thumb [...]

---

Virgil Ellsworth (2013-03-24 06:11:34)

Wow, incredible blog! How long have you ever been blogging for?

---

When good comments mean bad language | Codecraft (2013-08-22 08:57:27)

[…] years, I’ve urged developers to write better comments. I still claim that’s a good idea (a very good one), but as I’ve pondered what a better […]

---

Add some more extra redundancy again | Codecraft (2014-01-15 08:39:16)

[…] create redundancy that’s difficult to understand and maintain. Foolish coding standards and dumb comments are notorious for creating busywork this […]

---

Petra (2013-08-30 15:26:49)

Hello, I do believe your website could possibly be having internet browser compatibility issues.
When I take a look at your website in Safari, it looks fine but when opening in I.E., 
it has some overlapping issues. I just wanted to give you a quick 
heads up! Apart from that, fantastic website!

---

Carmon (2013-07-25 04:55:52)

Please let me know if you're looking for a article writer for your blog. You have some really good posts and I feel I would be a good asset. If you ever want to take some of the load off, I'd absolutely love to write some content 
for your blog in exchange for a link back to mine. Please blast 
me an email if interested. Many thanks!

---

&#8220;Rockstar Developers&#8221; are a dangerous myth | Codecraft (2015-03-05 20:15:42)

[…] How can there be a version 2.0 if there’s nobody who understands the groundbreaking ideas in 1.0? A big part of creating lasting value is communicating so others can appreciate and build upon your work. […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:46)

[…] was totally obscured and would never have been caught by a casual maintainer. It hadn’t been commented as a weirdness, […]

---

Lacunas Everywhere | Codecraft (2014-07-16 13:58:39)

[…] write comments that look like […]

---

Thoughts On Bridging the &#8220;Lacuna Humana&#8221; | Codecraft (2014-07-21 08:49:28)

[…] first written, and they tend to become more so over time, to the point where they actually create unnecessary confusion. They are not mandatory (except by human fiat, which is usually ignored), and everybody’s […]