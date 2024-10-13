---
layout: publication
title: Approximately Minwise Independence With Twisted Tabulation
authors: Dahlgaard Søren, Thorup Mikkel
conference: "Arxiv"
year: 2014
bibkey: dahlgaard2014approximately
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1404.6724"}
tags: ['ARXIV', 'FOCS', 'Independent']
---
<p>A random hash function <span class="math inline">\(h\)</span> is
<span class="math inline">\(\varepsilon\)</span>-minwise if for any set
<span class="math inline">\(S\)</span>, <span
class="math inline">\(|S|=n\)</span>, and element <span
class="math inline">\(x\in S\)</span>, <span
class="math inline">\(\Pr[h(x)=\min h(S)]=(1\pm\varepsilon)/n\)</span>.
Minwise hash functions with low bias <span
class="math inline">\(\varepsilon\)</span> have widespread applications
within similarity estimation. Hashing from a universe <span
class="math inline">\([u]\)</span>, the twisted tabulation hashing of
Ptracu and Thorup [SODA’13] makes <span
class="math inline">\(c=O(1)\)</span> lookups in tables of size <span
class="math inline">\(u^{1/c}\)</span>. Twisted tabulation was invented
to get good concentration for hashing based sampling. Here we show that
twisted tabulation yields <span class="math inline">\(\tilde
O(1/u^{1/c})\)</span>-minwise hashing. In the classic independence
paradigm of Wegman and Carter [FOCS’79] <span
class="math inline">\(\tilde
O(1/u^{1/c})\)</span>-minwise hashing requires <span
class="math inline">\(\Omega(\log u)\)</span>-independence [Indyk
SODA’99]. Ptracu and Thorup [STOC’11] had shown that simple tabulation,
using same space and lookups yields <span class="math inline">\(\tilde
O(1/n^{1/c})\)</span>-minwise independence, which is good for large
sets, but useless for small sets. Our analysis uses some of the same
methods, but is much cleaner bypassing a complicated induction
argument.</p>
