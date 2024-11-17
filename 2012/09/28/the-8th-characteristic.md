---
title: The 8th Characteristic
date: 2012/09/28
slug: the-8th-characteristic
---

Biologists will tell you that life has 7 characteristics: organization, metabolism, irritability, reproduction, homeostasis, adaptation, and growth.

I think this list is missing something. It's foundational, indisputable, and familiar even to kindergartners. But perhaps only kindergartners would call it out; several generations of biologists seem not to notice it enough to add it to their short list. Pick up a biology textbook, and you are unlikely to find a single chapter devoted to it.

Are you ready?

The 8th characteristic of life: <strong>mortality</strong>.

All living things die.

<figure><img title="a dead deer..." alt="" src="http://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Roadkill_on_Route_170_Okatie_Hwy_by_the_Chechessee_River%2C_SC%2C_USA%2C_jjron_09.04.2012.jpg/320px-Roadkill_on_Route_170_Okatie_Hwy_by_the_Chechessee_River%2C_SC%2C_USA%2C_jjron_09.04.2012.jpg" width="320" height="210" /><figcaption>We see without seeing... Photo credit: John O'Neil (Wikimedia Commons)</figcaption></figure>

Think about the consequences for a few moments. Would any of the ecosystems that you see on nature documentaries be possible without death? Would human civilization, as we know it? Read Orson Scott Card's short story, "Mortal Gods," and ponder.

<strong>Community blindness</strong>

Why am I writing about this as a software guy?

<!--more-->As <a title="How Software Is Like Biology" href="/2012/08/14/how-software-is-like-biology/">I've written before</a>, I believe life has profound lessons for software engineers. And death is a biggie. (I'll probably devote at least one chapter to this in my forthcoming book.)

To be fair to biologists, their discipline takes death into account constantly. Its existence colors narrations about food webs, survival of the fittest, decomposers, and thousands of related topics. Biologists are well aware of its ramifications.

But the fact that death didn't make their distilled list of 7 fundamentals is telling. If brilliant minds forget to state the obvious in that context, would it be any surprise to see the mistake repeated in the world of bits and protocols?

<strong>Pervasive software death</strong>

Hardware dies. We usually get that one. We know all about MTBF (mean time between failures) for hard drives, RAM, and the like. Interestingly, this phenomenon sometimes gets labeled "half-life", which has roots in a biological metaphor despite its direct borrowing from nuclear physics.

The other kind of death that software engineers routinely acknowledge is the Blue Screen of Death and its cousins (the abend, the seg fault, the panic). Strictly speaking, this is the death of a <em>process</em> or <em>accumulated state</em>, not the death of the product engineers worked so hard to build, and although we try to prevent this type of death, we don't spend a lot of time pondering it.

What about sublter forms of death, though?

Software products die. Consider VisiCalc.

Software versions die. Seen any Windows 3.1 lately?

Software companies die. When was the last time you bought anything from Caldera?

Software protocols die. Software installations die. Software expertise dies. Software standards die. Software fads die. Software markets die. Vendor and OEM relationships die. Competitive advantages die. And on and on.

<strong>So what?</strong>

Software death is a good thing. As in biology, it makes room for new and more evolved growth. It gives me job security. :-)

But I think software companies--all organizations, not just the dev organ--would be happier if they acknowledged this death and planned for it explicitly. For example:
<ul>
	<li>We should announce a lifespan to a product that starts with its birth (release). Do we expect it to live 3 years? 5? How long is support on the hook to keep it on life support? (Some orgs do this, but it's a less common practice than it should be.)</li>
	<li>As humans cope with death through wills, trusts, and inheritance laws, so software orgs need to plan, carefully and well in advance, for the upgrade experience implicit in the next generation release. Otherwise we'll get mired in messy and expensive probate procedures. Is there a "death tax" that makes it hard to transmit hard-won earnings forward? If so, can we minimize it?</li>
	<li>Developers should recognize that the technologies they depend on today will eventually be buried. Plan to switch horses before the one you're riding kicks the bucket. (Hence the importance of <a title="Julie Jones: Learn voraciously." href="/2012/09/24/julie-jones-learn-voraciously/">continuous learning</a>.)</li>
	<li>In biology, some forms of death have warning signs. Does our software notice these, and take measures to protect itself? Do we tell the customer that software is in danger?</li>
	<li>Do we provide a way for the customer to take our product off life support if that's the right decision?</li>
</ul>
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Please reply to this post with your own thoughts about where death needs better explicit handling in the world of software.</span></em></p>

---

Alpheus (2012-10-06 22:25:08)

It is my understanding that, in biology, there's a concept called "biological immortality", in which, short of disease or injury, the organism simply won't die.  Perhaps there's room for such a thing in the software world.  Software, in a way, is the embodiment of ideas, and ideas are eternal--they exist before anyone thinks them, and continue to exist after they are forgotten.  (Even so, I consider them to be alive.)

Indeed, sometime code can achieve a certain toe of immortality--Eric S. Raymond, several weeks ago, blogged about how robust a certain image processing program was, decades after he first wrote it!  Sometimes our understanding of a given problem domain becomes so mature, there isn't much of a point in messing with the code--and there are more problems like this then we realise.

Having said that, I can't help but think about how, while certain tortoises may be immortal, humans literally have mortality encoded into their DNA--so mortality exists for a reason, and probably several.  Thus, planning for mortality, and occasionally checking up on the "immortal" stuff, to make sure it still deserves life, makes a lot of sense to me.

And now that I think about it, it drives me nuts that I have a tablet that is probably a little more powerful than a laptop that recently died on me, but is so Android-centric.  It ought to be able to run LaTeX just fine, but it cannot, because Android hides the processor from me!  The Linux ecosystem represents thousands, and perhaps hundreds of thousands, of man-hours of coding, in all sorts of languages beyond Java, all of which is out of reach unless you do drastic things to your device (namely, root it and install some form of Linux).

---

Daniel (2012-10-03 14:09:02)

Jesse: Amazing how old software gets! In the late '90s I was working on code that had comments from the early '70s. Crazy.

---

Jesse Harris (2012-10-03 13:37:36)

As recently as two years ago, I was still providing support for a product originally released in 1996, last updated in 2002, and still (at that time) being sold. The only reason it happened was because we charged an annual fee for support. That said, nobody had bothered to figure out if the cost of supporting this ancient product was exceeding the revenues generated by it, especially when considering that support resources would best be spent elsewhere.

I'm sure customers were thrilled that they could keep on using the same piece of software for 15 years, but it would have been a better service to them to help them transition to a newer platform, and it almost certainly would have made a lot more business sense.

---

Daniel (2012-10-07 12:50:47)

Alphy: thank you for pointing me to the "biological immortality" concept. I went and read the wikipedia article. Fascinating!

All rules have exceptions--even this one, I guess. :-)

---

Don&#8217;t forget the circuit breakers &laquo; Codecraft (2013-01-11 18:02:04)

[...] macro scales, in ways that software barely begins to contemplate. In fact, homeostasis is one of life’s 8 key characteristics. I find it interesting that in many cases, life achieves this balance using feedback loops that [...]

---

Adios to &#8220;computer programming&#8221; | Codecraft (2013-04-05 09:34:28)

[...] is just as interconnected. Individual chunks of code depend on one another being alive, can poison one another’s environment, must respect the constraints implied by one [...]

---

dougbert (2013-03-15 11:59:33)

great observation and life process event handler.
I have been offered several jobs in my 33 years to work on the back side of a 'system' who was on life support, but no one wanted to 'improve' the same. Just keep it ticking until the income dropped below some 'exit criteria' level.

I said, no thanks.  I prefer to be on the front side of the curve, thank you, and even at the point of conception. THAT is fun

---

Daniel Hardman (2013-03-16 14:24:56)

It *is* fun to work on the front side of the curve. No doubt about it. We became engineers because we liked building something new and wonderful. I wish business people would let go of the misconception that once a feature has been built, it is "done"--and that it will continue to make them money in perpetuity. The truth is, features have carrying costs, and the health of a codebase requires steady maintenance and periodic upgrades.

---

Farewell to Google Reader | Codecraft (2013-03-14 17:18:50)

[...] this is a great illustration of the phenomenon of software death that I wrote about a few months [...]

---

Why Your Software Should Cry | Codecraft (2013-05-06 11:50:37)

[...] to stimuli is one of the 8 characteristics of life. That means that living things are aware, in some sense, of their relationship to the larger [...]

---

On pains and brains | Codecraft (2016-01-01 14:30:16)

[…] or identified success criteria for install+configure phases of the system, or surfaced symptoms of system obsolescence and death that its owners should […]

---

&#8220;Rockstar Developers&#8221; are a dangerous myth | Codecraft (2015-03-05 20:15:33)

[…] doing the hard, unrewarding detail work to guarantee that their needs are addressed throughout the full lifecycle of what you build is usually way more important than inventing a new and mind-bending algorithm. Addressing the need […]

---

Stanley Sawyer (2022-06-14 18:37:58)

Intereesting read