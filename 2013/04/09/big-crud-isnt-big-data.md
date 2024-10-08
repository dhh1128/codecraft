---
title: Big Crud Isn't Big Data
date: 2013/04/09
slug: big-crud-isnt-big-data
---

"Big Data" is another one of those buzz words that seems to be everywhere these days. We hear stories regularly about how fast the world's data grows and how big it's going to be by 20xx. Vendors then reason that we should buy their wares to cope. This infographic is typical:

<a href="http://www.businessinsider.com.au/infographic-heres-how-much-data-is-created-on-the-web-every-minute-2015-8" target="_blank"><img class="alignnone size-full wp-image-6282" src="https://codecraft.co/wp-content/uploads/2013/04/dataneversleeps_2-0_v2.jpg" alt="dataneversleeps_2-0_v2" width="810" height="1287" /></a>

I have several deep professional connections to big data<sup>[<a href="#foot1">1</a>]</sup>, going back decades, so when I say I think a lot of it is manufactured silliness, I'm hoping you'll pause before laughing me off.

The fact is, most of the "data" that's exploding is not hard-won intellectual treasure for the ages; it's marginal stuff like the viewing history on Fred Flintstone's deleted Netflix account. More than big data, we're experiencing a "big crud" wave, because we're pack rats. This comic has it right:<!--more-->

[caption id="" align="aligncenter" width="441"]<a href="http://www.qwantz.com/index.php?comic=2292"><img class=" " src="http://www.qwantz.com/comics/comic2-2303.png" alt="" width="441" height="300" /></a> image credit: Ryan North (qwantz.com)[/caption]

I'm not claiming that all big data is worthless; some amazing things become possible at the scale of billions of records. For Netflix, maybe Fred Flintstone's viewing history <em>is</em> valuable. Maybe. However, big data is only an asset if we can derive some value from it. And an awful lot of big data doesn't pass that smell test, either because our tools are inadequate, or because the data becomes stale, or because it wasn't particularly interesting data to start with.

The value we want to derive is <em>insight</em>.

If you're willing to be serious about the big data wave, then find the best of breed tools that push what's possible. I recommend <a title="Perfect Search - speed, precision, performance" href="http://www.perfectsearchcorp.com" target="_blank">Perfect Search</a>, for example; running a query 100x to 1000x faster than Google or Oracle, on a dataset 100x bigger, is the kind of tool that you need. And of course there are tools like hadoop and <a class="zem_slink" title="BigQuery" href="http://code.google.com/apis/bigquery/" target="_blank" rel="homepage">Google BigQuery</a> and Amazon's bulk load and Glacier and ... Consider <a href="/2012/11/07/big-data-in-motion/">capturing value from big data while it's in flight</a>, and not storing it at all.

If you don't want to surf the wave, then I have a relatively easy<sup>[<a href="#foot2">2</a>]</sup> solution. It's called the delete button. Go watch an episode of "<a class="zem_slink" title="Hoarders" href="http://www.aetv.com/hoarders/" target="_blank" rel="homepage">Hoarders</a>" and tell me I'm wrong. :-)

<hr />

<div style="font-size:92%;padding:1em;">

[<a name="foot1"></a>1] I worked in the backup industry for over a decade, including on BackupExec and NetBackup, which collectively owned most of the world's backups. When hundreds or thousands of clients stream over infiniband to media servers backed by peta-scale tape farms, and then use backups for security auditing and disaster recovery planning and regulatory compliance, <em>that's</em> big data.

I also worked in the search industry. We used to get requirements like "We need to index 380 billion tweets. How long would that take?" Or, "We'd like to index each trade on the New York Stock Exchange, the FTSE, and the Tokyo Stock Exchange. We want to do it in realtime, and support thousands of queries per second at the same time." Yep. I wasn't kidding about the world needing Perfect Search technology.

Now I work at <a href="http://www.adaptivecomputing.com" target="_blank">Adaptive Computing</a>, which happens to A) make the scheduling software that runs the largest supercomputers on the planet; and B) sell cloud management software that's at the core of some of the world's largest private cloud deployments. <a href="http://www.adaptivecomputing.com/blog-cloud/cloud-meet-hpc-meet-big-data/" target="_blank">Each of these markets generates serious big data war stories</a>.

[<a name="foot2"></a>2] I know, I know. Deleting isn't easy. You have to know what can be deleted and what can't. You have regulatory compliance issues. I still claim that getting better at deleting is easier than getting better at big data. That's probably a good subject for another post...

</div>
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://workforceplanning.wordpress.com/2013/04/08/are-we-jumping-the-shark-on-big-data-for-hr/" target="_blank">Are we Jumping the Shark on Big Data for HR?</a> (workforceplanning.wordpress.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://blog.neolane.com/conversational-marketing/big-data/" target="_blank">Transforming Big Data Into Actionable Insight [Infographic]</a> (neolane.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.domo.com/blog/2011/08/data-data-everywhere/" target="_blank">How Are You Managing Big Data? Data, Data Everywhere | Domo | Blog</a> (domo.com)</li>
	<li class="zemanta-article-ul-li"><a style="font-size:13px;" href="http://www.informationweek.com/big-data/news/big-data-analytics/dont-confuse-big-data-with-storage/240152455" target="_blank">Don't Confuse Big Data With Storage</a><span style="color:#333333;font-size:13px;"> (informationweek.com)</span></li>
</ul>

---

Big data will rewire your brain | Tim Batchelder.com (2013-04-09 10:15:51)

[...] Big Crud Isn’t Big Data (codecraft.co) [...]

---

Jesse Harris (2013-04-09 20:48:42)

Data that isn't valuable today could be critical tomorrow, and getting rid of it is irreversible. The very nature of data forces us to become digital packrats, accumulating and maintaining bits (pun intended) of cruft for what seems like an incomprehensible period of time. With storage getting cheaper and cheaper, there's not much disincentive to do so.

I was really disappointed that Microsoft backed off of its ambitious WinFS project. It would have helped home users tame some of this ever-increasing data.

---

Looking to the Future of Computing in a Big Data Environment | Data Center PostData Center Post (2014-03-17 02:31:07)

[…] do is dump data onto massive tape libraries and archive it for a decade, it’s not really in the big data sweet spot. You may be wrestling data, and it may be big, but you’re not really pursuing the problem […]