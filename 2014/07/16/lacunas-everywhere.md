---
title: Lacunas Everywhere
date: 2014/07/16
slug: lacunas-everywhere
---

I'm <a href="http://matadornetwork.com/abroad/20-awesomely-untranslatable-words-from-around-the-world/" target="_blank">told</a> that in Czech, the word "prozvonit" means "to call a mobile phone and let it ring once so that the other person will call back, saving the first caller money."

<figure><img src="https://farm5.staticflickr.com/4113/5080987526_cdbf30487f_z_d.jpg" alt="" width="640" height="421" /><figcaption>Image credit: AstridWestvang (Flickr)</figcaption></figure>

How would you translate this word to someone in New Guinea who has never experienced electricity, let alone a telephone or a bill from Verizon? You wouldn't. This is an example of a "<a href="http://en.wikipedia.org/wiki/Untranslatability" target="_blank">lacuna</a>"--a translation problem caused by semantic gaps in a target language. Lacunas occur in programming languages. You might know a few; maybe you wish C++ had python-style generators--or that Java had Haskell's notion of pure functions--or that C supported PHP-style string interpolation. But what if I told you that semantic misalignment between any pair of programming languages is just minor details? What if I claimed that all programming languages I've used have numerous, pernicious, and expensive semantic gaps? That we don't see these gaps for the same reasons that a stone-age hunter-gatherer fails to notice his inability to discuss patterns of cell phone usage? Would you think I'm crazy? <!--more-->
<h3>Symptoms</h3>
Well, how many of the following scenarios sound familiar? (If this list gets too long, just read a few--but I wanted to show you how pervasive the problem is...)
<ul>
	<li>You've just written the definitive implementation of CIDR parsing (or printer detection, or timezone handling, or whatever), and you worry about somebody else <a title="Why Weakened Dev Teams Suffer From NIH Syndrome" href="../../../2008/07/30/weakened-dev-teams-nih/">re-inventing the wheel</a>. (Imagine if you could assert that no functions having the same semantics and intent as yours get introduced in the future, without triggering a warning message and a judicious human override...)</li>
	<li>You shipped prototype code (or a stub, or an ugly kludge) that was okay once upon a time, but should never have seen the light of day. (Imagine if you could tell a compiler that certain code is iffy, and run a test before release to guarantee that none of that existed in shipping code paths...)</li>
	<li>You maintain design docs on a wiki, a network share, a CMS, or similar--and the relationship between these artifacts and the source code that embodies/implements them is stored nowhere except the heads of the dev team and maybe an occasional comment. As a result, coders refer to them only occasionally; they decay over time and may not have high ROI. (Imagine if your IDE could knit together all these sources, because your programming language could directly express the idea of attachments and hyperlinks... Imagine if you could implement a business rule such as "all dialogs in the UI must be linked to a usability eval plan" -- and have tests fail where such relationships don't exist...)</li>
	<li>For security purposes, you need to know which public functions are callable by external entities, which contextual constraints would make them safe, and which parts of your code execute with which elevated privileges. You spend hours building a spreadsheet, but it's out-of-date almost immediately. (Imagine that security semantics were directly declarable in code in such a way that the compiler and other tools could inspect them, warn about them, and report them on demand...)</li>
	<li>You have methods that are only callable at certain phases in the lifecycle of an object. Your only mechanism for enforcing conformity is documentation, plus throwing exceptions/SIGABRT if they're ignored. (Imagine if temporal semantics were declarable and enforceable...)</li>
	<li>You write code that validates parameters at the top of a function, and then you regurgitate those same semantics in redundant javadoc-style comments, so human consumers of the function learn about the constraints without needing to see the impl. (Imagine if preconditions were treated as an essential characteristic of a function's interface, making them as visible as parameter names. No doc necessary...)</li>
	<li>You waste time writing boilerplate code that does nothing more than assign args to member variables in constructors: <code>this.size = size; this.color = color</code>. (Imagine if you could simply note a "copy args" intention and have the compiler generate the rest--automatically updating the assignments as code evolves...)</li>
	<li>You write <a title="// Comments on Comments" href="../../../2012/10/31/comments-on-comments/">comments</a> that look like this:
<pre style="margin:1em;padding:1em;color:green;">// IF YOU EVER MODIFY THIS ARRAY, MAKE SURE YOU ALSO
// MODIFY THE HANDLING ROUTINES IN xyz AND abc !!!</pre>
(Imagine if semantic coupling were directly expressible to a compiler...)</li>
	<li>You write code that forwards parameters (static factory method takes args A, B, and C, then calls constructor with args A, B, and C). The names and constraints on parameters are identical in both contexts, but you have to repeat precondition code and javadoc for them as many times as they occur. (Imagine if you could simply note a correspondence and have the compiler forward and document semantics for you automatically...)</li>
	<li>You'd like to <a title="How to turn coding standards into epic fails — or not" href="../../../2012/09/27/coding-standards/">enforce coding standards</a>--formatting and naming conventions, maybe, but also trickier stuff, like "we strictly obey the <a href="http://en.wikipedia.org/wiki/Liskov_substitution_principle" target="_blank">Liskov Substitution Principle</a>." (Imagine if any given file or folder could hyperlink to formally defined conventions, and then the compiler would enforce them...)</li>
	<li>You receive an edict from on high that, on all shipping projects, you can't use any code with a GPL license--or you are asked to evaluate the IP of an M&A candidate for all open source usage--or you want to know what attribution you should put in your product's about box. You need to know which components and libraries have which licenses. You grep the code and hope your report is comprehensive and accurate, but you aren't totally confident. (Imagine if the license for a piece of code could be directly expressed in the syntax of your programming language... Imagine if you could tell a compiler to refuse to use code with a license you don't like...)</li>
	<li>You'd like to identify code paths that are invoked by admins, and diff those against code paths that are invoked by less privileged users. Or you'd like to find code paths used by customer X. Or you'd like to guarantee that the latest round of testing exercises every function that's been changed in the past 3 weeks. (Imagine if people, use cases, security profiles, and other "business concerns" could be associated with places in code... Imagine if, at compile time, you could generate unions and intersections of call trees based on arbitrary criteria that your team dreamed up...)</li>
	<li>You endlessly fiddle with "signed/unsigned comparison" warnings, even though the two numbers you're comparing invariably have ranges that are small and positive. (Imagine if the range of the operands in a comparison, rather than just their types, were known to compilers...)</li>
	<li>You want a particular class to be threadsafe, and you go to considerable trouble to make it so, but you worry that later maintainers won't understand key subtleties. (Imagine if you could assert thread safety, and the compiler would enforce it forever...)</li>
	<li>For performance or scale reasons, you need to guarantee that a particular function, throughout its maintenance lifetime, never triggers file I/O, never uses the network, always runs faster than a reference impl, performs as <em><strong>O(n)</strong></em> with respect to a given parameter, etc. (Imagine that all standard library calls "knew" their resource usage characteristics. Imagine that a compiler could validate rich assertions about the call tree of any compilation target...)</li>
	<li>You want to make a variable "read-only" or "final" -- but partway through a function, rather than at declaration time. (Imagine if semantics could be attached anywhere, not just in declarations...)</li>
</ul>
I could go on. All day long, every day, developers around the world wrestle to codify constructs that really don't map well onto the semantic space that their chosen language provides. Their language may be Turing-complete, but that doesn't mean it's semantically rich. The problem, I think, is caused by our industry <a title="Why People Are Part of A Software Architecture" href="../../../2008/06/25/why-people-are-part-of-a-software-architecture/">undervaluing the human dimension</a> of software development. We are taught to analyze and create context-free grammars. That's a hard task, and perhaps we can be forgiven for thinking that once we get there, with a fast and robust compiler, a nice runtime, documentation, and other tools, we've mostly achieved the mandate of a programming language. <a title="When good comments mean bad language" href="../../../2013/08/22/when-good-comments-mean-bad-language/">Everything else goes in the comments</a>. But programming languages have a dual audience (humans as well as compilers)--and the thinking, messy half of it gets neglected. We have a <em>lacuna humana</em>.
<h3>Workarounds Don't Cut It</h3>
Perhaps you're saying to yourself: "Language X has a way to solve problem Y." At the micro level, I don't necessarily disagree. I have written unit tests that (sort of) proved thread-safety in a codebase. I've created scripts that proved copyright/license compliance. I have found clever ways to enforce one or two high-value coding standards. I know about Ada's numeric range types. I've decorated python code in such a way that prototype code was discoverable, so we wouldn't ship it. I've used <code>@Override</code> in java. The <code>const</code> and <code>constexpr</code> keywords in C++ tell you <a title="How Sutter’s Wrong About const in C++ 11" href="../../../2013/01/02/how-sutters-wrong-about-const-in-cpp-11/">something about thread safety</a>. But collectively, I claim that today's programming languages do a poor job addressing any needs that are not tied pretty directly to deciding what machine code gets put in a binary--even though the discipline of software development <a title="Good Code Is Balanced" href="../../../2012/08/27/good-code-is-balanced/">subsumes many other concerns</a>. If you're hoping to <a title="Users Aren’t The Only People In Your Software" href="../../../2012/09/04/users-arent-the-only-people-in-your-software/">solve human problems</a>, your coding tools are crippled by the narrow scope of the language they support. How much wasted time is attributable to issues like what I've listed?
<h3>Passing the Buck Doesn't Cut It</h3>
Perhaps you're saying to yourself: "Use the right tool for the right job. A programming language shouldn't have the fuzzy jobs in the examples above." Really? Almost every piece of code on the planet ends up having some kind of copyright/license associated with it. The license can be described in text, and it directly impacts how the software is produced and consumed--but the language of the software should only concern itself with classes and functions, and ignore this issue? A language shouldn't be indicted for creating useless redundancy that undermines <a title="Good fences make good neighbors" href="../../../2013/05/15/good-fences-make-good-neighbors/">encapsulation</a> and the accuracy of docs? A language is well designed, even if it generates tons of useless warnings, displayed redundantly, for all time, to all coders who work on a codebase? I'm not claiming that tech writers should create content in the same programming language as developers, or that graphic artists should start coding instead of photoshopping their icons. We don't need to compile gantt charts. I'm just saying that even within the domain of problems that software engineers usually own, our languages are too semantically barren to solve lots of real-world problems. This costs us real time and money.
<h3>Plugging the Gaps</h3>
It doesn't have to be this way. If you're following my blog, you know that I've been designing a new programming language. One of its most important innovations offers a quantum leap in semantic density, without lots of noise or bother. I'll be explaining this feature, "marks," in a series of <a href="../../../2014/07/21/bridging-the-lacuna-humana/">follow-on posts</a>. I hope you'll subscribe or check back to see where I'm headed.

---

Mountains, Molehills, and Markedness | Codecraft (2014-07-28 08:44:36)

[…] my previous three posts, I explained why the semantics of programming languages are not as rich as they could be. I pointed out some symptoms of that deficit, and then made recommendations about bridging the gap. […]

---

Taming Side Agreements | Codecraft (2014-10-28 08:35:58)

[…] although I think docs and comments are often a band-aid. The proxy technique that I recommended, to codify human concerns in a codebase, is another way of adding sunshine. The “marks” feature that I’m […]

---

How to point in code | Codecraft (2014-09-25 08:39:07)

[…] and triangulation still aren’t enough. I’ve alluded on previous posts to the idea that code should be able to describe constructs that are not coded today: use cases, personas, business requirements, […]

---

&#8220;Rockstar Developers&#8221; are a dangerous myth | Codecraft (2015-03-05 20:15:39)

[…] can there be a version 2.0 if there’s nobody who understands the groundbreaking ideas in 1.0? A big part of creating lasting value is communicating so others can appreciate and build […]

---

Exploring the Power of Deixis | Codecraft (2014-09-23 08:34:43)

[…] happy–if a persona isn’t even a valid topic for your source code? (This is the whole lacuna humana topic that I recently […]

---

David H (2014-07-17 07:29:40)

Hi Daniel -
You've definitely got me curious!
Can you give us your reasoning why a whole new language vs. extending an existing language to solve your use cases? Becaues the problems you cite sound more like a wish list for additional features to a language, not complaints about features you want removed from any given language.
Also, what you've written so far reminds me of Donald Knuth and his "literate programming", which was intended to address your concerns about the human aspect of programming. If I understand correctly, in Knuth's system you write a document whose primary language is English (or Spanish or whatever your human language is) and the compiler extracts embedded code out of it and creates the program. That way the code and documentation are never far apart. Comments on that?
David H

---

AFK &amp; Reading Material | UpEndian (2014-07-17 07:58:31)

[…] In the mean time, Daniel Hardman over at Codecraft has given the software devs among us some interesting thoughts to chew on: Lacunas Everywhere […]

---

Daniel Hardman (2014-07-17 08:41:10)

David: the problem I'm highlighting doesn't require a new programming language; it could easily be solved by extending existing ones. In fact, I even toyed with the idea of writing up a proposal for C++17... However, "extending" doesn't just mean adding a library or package into the core runtime; it would require a change in assumptions about what we believe is valid content for code. For that reason, I suspect that existing languages won't glom onto it.

In my next couple posts, I'll describe the solution. I've been slow to post, lately, but I'll try to write them quickly so you're not left hanging for too long. :-) I'm not trying to be mysterious; I'm just having a dickens of a time pulling half a dozen mental threads into a coherent tapestry.

Your connection with Knuth is an interesting one. I've heard of literate programming, and I've read some stuff by him before, but I am not very familiar with the specific idea you describe, so now I've got a new homework assignment.

---

In Which Warnings Evolve Wings | Codecraft (2014-08-06 08:46:10)

[…] evidence that the compiler needs to know more about your intent. (Does this sound like the “lacuna humana” that I have been harping on […]

---

Thoughts On Bridging the &#8220;Lacuna Humana&#8221; | Codecraft (2014-07-21 08:49:07)

[…] my previous post, I discussed the semantic gaps that afflict current programming languages. These gaps are caused by […]

---

Introducing Marks | Codecraft (2014-07-24 08:49:20)

[…] my previous two posts (here and here), I described how and why programming languages can’t talk about many issues that […]