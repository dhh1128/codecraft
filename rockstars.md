---
title: "Rockstar Developers" are a dangerous myth
date: 2015-03-04
slug: rockstars
redirect_from:
  - /2015/03/04/rockstars
comments:
  - author: Mick Oberlin
    date: 2015-03-06 01:41:00
    comment: |
      I can't agree with your last statement more. I have the same issue with "Guru". Rather than "Rockstar", couldn't we have something that at least incorporates the features of a winning programmer? You know, like "Savant", "Virtuoso", or even "Gladiator"? I don't even really listen to Rock & Roll.
  - author: Daniel Hardman
    date: 2015-03-06 07:29:41
    comment: |
      Ooh, I really like "virtuoso." Gladiator is an interesting one, too. I don't usually think of what we do as a battle, but now that I think about it, I do talk about having "battlescars"...
  - author: David H
    date: 2015-03-06 11:37:00
    comment: |
      Daniel, I'm really glad you wrote this post. I wish more people, especially managers, understood that a prima donna developer really undermines their organization and can torpedo their results. In one group I was in (company name shall remain anonymous) we had three "rock stars" on the same team all ignoring the others and writing redundant code at rapid velocity. They impressed the boss with their short-term results and then quit or changed to another group before the consequences had time to catch up to them. I got to clean up the mess.
      
      Oh, to add to your list: "unicorn developers." Heaven help us.
  - author: Daniel Hardman
    date: 2015-03-07 22:18:51
    comment: |
      Yes, it's really unfortunate that folks sometimes skip out just when the exacting work of maintaining a newly created codebase (finding and fixing all the subtle bugs, and trying to polish the rough edges) is beginning. What seemed like a good design early on can look pretty dismal when compromises begin to manifest their long-term consequences...
      
      I admire you for being the sort of guy who is in it for the long haul...
  - author: Andy Lawrence
    date: 2015-03-10 22:54:48
    comment: |
      Does this mean I should quit referring to you as the best rockstar, guru, code ninja that I know when people ask me "Do you know Daniel Hardman?"?
  - author: Daniel Hardman
    date: 2015-03-10 22:58:28
    comment: |
      Hah! Of course you should. You know lots of awesome coders (and you are one yourself). :-) Whenever I do something boneheaded (like when I wrote, recently, about taking forever to diagnose a simple missing mutex), I am reminded of my amazing capacity to not be very smart...
---
Recently I've run across several uses of the phrase "rockstar developer" or "rockstar programmer" ("code ninja" is another hip variant). The term shows up on slashdot, for example. I've also seen it in job postings and in blogs.<sup>[<a target="_blank" href="http://www.infoworld.com/article/2886735/it-careers/should-you-hire-a-software-developer-talent-agent.html">1</a>],[<a target="_blank" href="http://sethgodin.typepad.com/seths_blog/2014/12/a-one-day-design-sprint-and-an-app-directory.html">2</a>],[<a target="_blank" href="http://skeptics.stackexchange.com/questions/7559/are-there-studies-clearly-illustrating-the-great-discrepancies-in-programmer-pro3">3</a>]</sup> A rockstar hacker archetype is standard fare in TV shows, where his or her computing feats are practically a superpower (<em>Agents of Shield</em>, <em>Person of Interest</em>, <em>Leverage</em>, <em>Scorpion</em>, ...) Of course Hollywood loves the notion, too; I thought <em>The Imitation Game</em> was fascinating, but besides taking liberties with history, it portrays Alan Turing in a distorted way that feeds such mystique. (Turing <em>was</em> absolutely brilliant, and certainly one of the most important pioneers in computing. But he <a href="http://www.slate.com/blogs/browbeat/2014/12/03/the_imitation_game_fact_vs_fiction_how_true_the_new_movie_is_to_alan_turing.html" target="_blank">didn't invent his codebreaking machine alone</a>.)

[caption id="attachment_6021" align="aligncenter" width="646"]<a href="http://youtu.be/j2jRs4EAvWM"><img src="https://codecraft.co/wp-content/uploads/2015/03/screen-shot-2015-03-05-at-6-52-57-pm.png?w=646" alt="Alan Turing and team members at Bletchley Park, with a forerunner of the modern computer &mdash;  technology invented by brilliant people to break the Nazi Enigma encryption. Screenshot from official trailer, under fair use." width="646" height="271" class="size-large wp-image-6021" /></a> from <em>The Imitation Game</em>: Alan Turing and team members at Bletchley Park, with a forerunner of the modern computer — technology invented by brilliant people to break the Nazi Enigma encryption. Screenshot from official trailer, under fair use.[/caption]

It's even in my inbox. After I began writing this post, I got an email from a recruiter on LinkedIn, looking for "superstars":

<img src="https://codecraft.co/wp-content/uploads/2015/03/superstar.png?w=646" alt="superstar" width="646" height="152" class="aligncenter size-large wp-image-6027" />

The buzz about these mythical supercoders has begun to raise my hackles.



Plenty of developers consider themselves gifted, and not infrequently, they are right; I've met amazingly smart people in this industry. It's also true that in software, the standouts are <em>way</em> more productive than their average or under-average peers. If memory serves, <em>Facts and Fallacies of Software Engineering</em> says the best programmers/coders/designers are up to 28x times better than the worst. The <a href="http://skeptics.stackexchange.com/questions/7559/are-there-studies-clearly-illustrating-the-great-discrepancies-in-programmer-pro" target="_blank">actual numbers are debated</a>, and I think it's possible to get carried away, but I could believe some big ratios.

Nonetheless, the worldview behind the "rockstar" label is naive and dangerous, and I urge you to help me correct it. Here's why:

<h3>My beefs</h3>

<dl>
<dt><strong>1. Making a <a href="features-are-not-chunks-of-code.md" title="Features are not chunks of code">more than writing clever code</a>.</strong></dt>
<dd>Understanding<a href="good-code-is-optimized.md" title="Good Code Is Optimized">need of your business to make a profit</a> is usually a good idea, too. Perhaps the vast residual work is what Thomas Edison had in mind when he said,
<blockquote>Genius is one percent inspiration, ninety nine percent perspiration.</blockquote></dd>
<dt><strong>2. The best developers are superb <a href="http://www.hanselman.com/b/TheMythOfTheRockstarProgrammer.aspx" target="_blank">team members</a>, not prima donnas.</strong></dt>
<dd>I don't care if you're in a startup and you can only afford to hire oneveloper &mdash; if you think that developer can ignore teamwork, you're foolish. On day 1, even a one-person dev phenom has to work with those who test or document or support or deploy or sell. And if your startup has staying power, the day will come when Codezilla has to work with a contractor, or an understudy, or a team in Johannesburg or Timbuktu that will take over or integrate with what they've built.</dd>
<dt><strong>3. If nobody understands your code, <a href="why-mental-models-matter.md" title="Why Mental Models Matter">you've failed</a>.</strong></dt>
<dd>How can there be a version 2.0 if there's <a href="comments-on-comments.md" title="// Comments on Comments">build upon your work</a>.</dd>
<dt><strong>4. Nobody knows everything.</strong></dt>
<dd>It might be possible to crank out dime-a-dozen websites without research or innovation, but most projects with genuine market value are broad enough that they demand more skills than exist in any one person. Wise developers (as opposed to simply clever ones) are <a href="julie-jones-learn-voraciously.md" title="Julie Jones: Learn voraciously.">interested in learning</a>.</dd>
<dt><strong>5. Relying on magicians stymies progress.</strong></dt>
<dd>When we attribute remarkable results to a murky thing called "genius", we abdicate the responsibility of other smart people to deliver. This makes good old-fashioned elbow grease seem dull, and shifts all the glamour to pulling a rabbit out of a hat. We all love the dazzle of a great show, but we're better served by figuring out how to predict, replicate, and optimize success, <a target="_blank" href="http://www.infoworld.com/article/2615814/it-training/6-home-truths-about-rockstar-developers.html">not treat it as a mystery</a>.
<dt><strong>6. The best metaphor for the pinnacle of our profession is a jaded, ego-centric, overpaid, dissolute show-off with a limited repertoire? Really?</strong></dt>
<dd>(Can you tell I'm not big on rockstars? :-)</dd>
</dl>

<h3>Standing ovations</h3>
To temper my complaining just a wee bit, perhaps it's worth acknowledging one way that the "rockstar" metaphor <em>does</em> work: I have seen many performances during my career that were worthy of admiration &mdash; even applause. Working with people who are humble and smart and generous, who push the limits and raise the bar in all the best ways &mdash; that's an experience as memorable as any rock concert. Definitely worth the price of admission.

Do you agree?
