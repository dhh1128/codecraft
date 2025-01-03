---
title: Encapsulation isn't just for code
date: 2013-08-02
slug: encapsulation-isnt-just-for-code
redirect_from:
  - /2013/08/02/encapsulation-isnt-just-for-code
comments:
  - author: SutoCom
    date: 2013-09-04 03:51:41
    comment: |
      Reblogged this on <a href="encapsulation-isnt-just-for-code.md" rel="nofollow">Sutoprise Avenue, A SutoCom Source</a>.
---
When computer science folks talk about encapsulation, they are usually thinking of how the principle applies to objects and functions inside a codebase. Best practice calls for a separation of concerns &mdash; each object responsible for one type of work, hiding all details from its neighbors.

That's great. But it's not the only way encapsulation ought to show up in software.

In actual deployment, software packages often manifest anti-patterns in the way that they are configured. A web server has to know all about three different database servers that contribute data for its pages; HA failover scripts must know the identity and responsibility of every actor in the system, as well as many particulars about how these entities use resources to accomplish their tasks.

No wonder our deployments are fragile and high-maintenance...

The cloud computing wave is raising the bar for encapsulation in the way applications &mdash; not just objects &mdash; discover and interact with one another. In this week's installment of my <a title="cloudify series" href="../../../category/cloudify">series of posts about how to "cloudify"</a>, I discuss how <a href="http://www.adaptivecomputing.com/blog-cloud/how-to-cloudify-your-software-part-3-do-you-want-fries-with-that/" target="top">role-based interactions insulate components</a> from details they don't need to know. It's encapsulation all over again. And this encapsulation pattern manifests itself in unlikely places &mdash; like the order queue at McDonald's...

<figure><img src="http://farm1.staticflickr.com/102/258253832_927e23b2b9.jpg" width="500" height="375" /><figcaption>What can McDonalds teach a develr of cloud-friendly software? <a href="http://www.flickr.com/photos/derfokel/258253832/sizes/m/in/photolist-oPBSh-F14J9-MQh6J-4c1HXK-4mEHoC-4ovGHD-4upuzt-4wYDLv-5jWmpq-5Xv7Wr-729ALs-76Locf-7E3LgF-9e8N8c-buruPp-bxadb4-biwGXv-e8ySUj-cEmmDf-ebusvW-8MBDdG-bvALeU-b5yiwg-9D3wMX/" target="_blank">photo credit: phogel (Flickr)</a></figcaption></figure>

Stay tuned for further installments of this series each Friday. As I said in <a title="learn how to cloudify" href="programmers-learn-how-to-cloudify.md">Part 1</a>, I believe that a competence with cloud&mdash;cloud-oriented programming, if you will&mdash;will be a checkbox on future tech resumes.
