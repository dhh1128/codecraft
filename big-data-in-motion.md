---
title: Big Data In Motion
date: 2012-11-07
slug: big-data-in-motion
redirect_from:
  - /2012/11/07/big-data-in-motion
---

I've been at Cloud Expo this week, listening to lots of industry hoopla about building cloud-centric apps, managing clouds, purchasing hardware for clouds, buying private clouds from public cloud providers, and so forth.

<figure><img alt="" src="http://farm6.staticflickr.com/5283/5247181522_d9884b37ac.jpg" height="332" width="500" /><figcaption>Photo credit: aquababe (Flickr)</figcaption></figure>

One interesting decision made by the organizers of the conference was to bring "<a class="zem_slink" title="Big data" href="http://en.wikipedia.org/wiki/Big_data" target="_blank" rel="wikipedia">big data</a>" under the same conference umbrella. There's a whole track here about big data, and it gets mentioned in almost every presentation.

And I've sensed a shift in the wind.

Years and months ago, "big data" was all about mining assets in a <a class="zem_slink" title="Data warehouse" href="http://en.wikipedia.org/wiki/Data_warehouse" target="_blank" rel="wikipedia">data warehouse</a>. You accumulated your big data over time. It sat in a big archive, and you planned to analyze it. You spun up hadoop or used some other <a class="zem_slink" title="MapReduce" href="http://en.wikipedia.org/wiki/MapReduce" target="_blank" rel="wikipedia">map-reduce</a>-style tool to crunch for days or weeks until you achieved some analytical goal.

What I'm hearing now is an acknowledgement that an important use case for big data &mdash; perhaps <em>the most</em> important use case &mdash; has little to do with data at rest. Instead, it recognizes that you'll never have time to go back and sift through a vast archive; you have to notice trends by analyzing data as it streams past and disappears into the bit bucket. The data is still big, but the bigness has more to do with volume/throughput, and less to do with cumulative size.

This has interesting implications. Algorithms that were written on the assumption that you can corral the data set under analysis need to be replaced by ones based on <a class="zem_slink" title="Sampling (statistics)" href="http://en.wikipedia.org/wiki/Sampling_%28statistics%29" target="_blank" rel="wikipedia">statistical sampling</a>; exactness needs to give way to fuzziness.

Interestingly, I think this will make computer-driven data analysis much more similar to the way humans process information. As I've said elsewhere, when faced with a difficult design problem, a smart question to ask is: <em>how does Mother Nature solve it?</em>
