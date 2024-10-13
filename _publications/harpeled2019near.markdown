---
layout: publication
title: Near Neighbor Who Is The Fairest Of Them All
authors: Sariel Har-peled, Sepideh Mahabadi
conference: "Neural Information Processing Systems"
year: 2019
bibkey: harpeled2019near
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2019/hash/742141ceda6b8f6786609d31c8ef129f-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
<p>In this work we study a “fair” variant of the near neighbor problem.
Namely, given a set of <span class="math inline">\(n\)</span> points
<span class="math inline">\(P\)</span> and a parameter <span
class="math inline">\(r\)</span>, the goal is to preprocess the points,
such that given a query point <span class="math inline">\(q\)</span>,
any point in the <span class="math inline">\(r\)</span>-neighborhood of
the query, i.e., <span class="math inline">\(B(q,r)\)</span>, have the
same probability of being reported as the near neighbor.</p>
<p>We show that LSH based algorithms can be made fair, without a
significant loss in efficiency. Specifically, we show an algorithm that
reports a point <span class="math inline">\(p\)</span> in the <span
class="math inline">\(r\)</span>-neighborhood of a query <span
class="math inline">\(q\)</span> with almost uniform probability. The
time to report such a point is proportional to <span
class="math inline">\(O(\dns(q.r) Q(n,c))\)</span>, and its space is
<span class="math inline">\(O(S(n,c))\)</span>, where <span
class="math inline">\(Q(n,c)\)</span> and <span
class="math inline">\(S(n,c)\)</span> are the query time and space of an
LSH algorithm for <span class="math inline">\(c\)</span>-approximate
near neighbor, and <span class="math inline">\(\dns(q,r)\)</span> is a
function of the local density around <span
class="math inline">\(q\)</span>.</p>
<p>Our approach works more generally for sampling uniformly from a
sub-collection of sets of a given collection and can be used in a few
other applications. Finally, we run experiments to show performance of
our approach on real data.</p>
