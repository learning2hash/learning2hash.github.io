---
layout: publication
title: Space-efficient Algorithms For Computing Minimal/shortest Unique Substrings
authors: Mieno Takuya, Köppl Dominik, Nakashima Yuto, Inenaga Shunsuke, Bannai Hideo, Takeda Masayuki
conference: "Arxiv"
year: 2019
bibkey: mieno2019space
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1905.12854"}
tags: ['ARXIV']
---
<p>Given a string <span class="math inline">\(T\)</span> of length <span
class="math inline">\(n\)</span>, a substring <span
class="math inline">\(u = T[i..j]\)</span> of <span
class="math inline">\(T\)</span> is called a shortest unique substring
(SUS) for an interval <span class="math inline">\([s,t]\)</span> if (a)
<span class="math inline">\(u\)</span> occurs exactly once in <span
class="math inline">\(T\)</span>, (b) <span
class="math inline">\(u\)</span> contains the interval <span
class="math inline">\([s,t]\)</span> (i.e. <span class="math inline">\(i
\leq s \leq
t \leq j\)</span>), and (c) every substring <span
class="math inline">\(v\)</span> of <span
class="math inline">\(T\)</span> with <span class="math inline">\(|v|
&lt; |u|\)</span> containing <span class="math inline">\([s,t]\)</span>
occurs at least twice in <span class="math inline">\(T\)</span>. Given a
query interval <span class="math inline">\([s, t] \subset
[1, n]\)</span>, the interval SUS problem is to output all the SUSs for
the interval <span class="math inline">\([s,t]\)</span>. In this
article, we propose a <span class="math inline">\(4n + o(n)\)</span>
bits data structure answering an interval SUS query in output-sensitive
<span class="math inline">\(O(\mathit{occ})\)</span> time, where <span
class="math inline">\(\mathit{occ}\)</span> is the number of returned
SUSs. Additionally, we focus on the point SUS problem, which is the
interval SUS problem for <span class="math inline">\(s = t\)</span>.
Here, we propose a <span class="math inline">\(\lceil (\log_2{3} + 1)n
\rceil + o(n)\)</span> bits data structure answering a point SUS query
in the same output-sensitive time. We also propose space-efficient
algorithms for computing the minimal unique substrings of <span
class="math inline">\(T\)</span>.</p>
