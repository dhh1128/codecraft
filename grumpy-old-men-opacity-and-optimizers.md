---
title: Grumpy Old Men, Opacity, and Optimizers
date: 2014/09/09
slug: grumpy-old-men-opacity-and-optimizers
---

<p>Today I'm channeling my inner grumpy old man. And these guys are helping. (I am not old enough to pull off such a face by myself, although life is rapidly helping me get there. ;-)</p><p>[embed]https://www.flickr.com/photos/neilmoralee/6244499091/sizes/z/[/embed]</p><p>The reason I'm feeling grumpy is that I've had another in a long, long line of conversations about how to write faster code.</p><p>It's not that optimization experts are dumb. Far from it. They are invariably smart, and in general, they are better informed than I am about how pipeline burst cache and GPUs and RAM prefetch algorithms work. I generally learn a lot when I talk to guys like this.</p><p>I applaud their passion, even if I think <a title="3 Commandments of Performance Optimization" href="steve-tolman-it-depends.md">it depends</a>. :-)</p><p>My point today is not about inlines, though. It's not even about performance dogma. Rather, it's about opacity.</p><p>The optimization choices that a compiler makes about inlining and sundry other issues are <em>opaque</em> to most coders. And I claim that it is this fact--not irrational zealots--at the heart of a lot of holy wars, debates, and FUD about optimization. The classic paper by <a href="http://www.drdobbs.com/cpp/c-and-the-perils-of-double-checked-locki/184405726" target="_blank">Meyers and Alexandrescu about how compiler optimization defeats the intent of the double-checked locking pattern</a> provides eloquent examples of this opacity. If you haven't read it, I encourage you to do so.</p><p>We should fix this.</p><p>Compiler makers, I hereby request a feature. Please add the ability to generate an "optimization plan" for a function, analogous to the "explain query plan" feature that DB admins have used to tune their work for decades.</p><p>I can imagine this working as a compiler switch, similar to <code>-E</code> which dumps preprocessor output to stdout. If I add <code>--explain-optimizations</code> to the cmdline, I would like a report that tells me:</p><ul><li>What sorts of loop unwinding, reordering, and other shortcuts will be used. Please tie them back to the specific switches that are active.</li><li>How optimizations were constrained by block, function, and translation unit scope--and how optimizations might change naive assumptions about scope that a programmer would form by looking at the high-level representation of the code.</li><li>What additional optimizations might be possible if additional switches were added or removed.</li><li>What guesses were made about likely versus unlikely branches in conditionals.</li><li>What additional optimizations might be possible if not for a certain characteristic of the code. Please be specific: "I could not optimize out the extra assignment to foo, because codepath X requires it."</li><li>How micro optimization decisions conflict with macro ones, and what assumptions and priorities were used to resolve these conflicts.</li></ul><p>I realize I am not asking for something easy. But I believe explaining optimization choices cannot be harder than making those choices in the first place--and the problem must be somewhat tractable, since the SQL crowd has an analogous tool.</p><p>Let's shine some light on this black magic, and turn performance tradeoffs into a science based on common, abundant knowledge. I think it could improve the whole industry.</p><hr /><p style="text-align:right;color:gray;font-size:85%;">Image credit: <a href="https://www.flickr.com/photos/neilmoralee/6244499091/sizes/l">Neil. Moralee (Flickr)</a></p>