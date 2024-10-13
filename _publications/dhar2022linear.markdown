---
layout: publication
title: Linear Hashing With ell_infty Guarantees And Two-sided Kakeya Bounds
authors: Dhar Manik, Dvir Zeev
conference: "TheoretiCS Volume"
year: 2022
bibkey: dhar2022linear
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.01665"}
tags: ['Independent']
---
<p>We show that a randomly chosen linear map over a finite field gives a
good hash function in the <span
class="math inline">\(\ell_\infty\)</span> sense. More concretely,
consider a set <span class="math inline">\(S
\subset \mathbb{F}_q^n\)</span> and a randomly chosen linear map <span
class="math inline">\(L : \mathbb{F}_q^n
\to \mathbb{F}_q^t\)</span> with <span
class="math inline">\(q^t\)</span> taken to be sufficiently smaller than
$ |S|$. Let <span class="math inline">\(U_S\)</span> denote a random
variable distributed uniformly on <span
class="math inline">\(S\)</span>. Our main theorem shows that, with high
probability over the choice of <span class="math inline">\(L\)</span>,
the random variable <span class="math inline">\(L(U_S)\)</span> is close
to uniform in the <span class="math inline">\(\ell_\infty\)</span> norm.
In other words, {} element in the range <span
class="math inline">\(\mathbb{F}_q^t\)</span> has about the same number
of elements in <span class="math inline">\(S\)</span> mapped to it. This
complements the widely-used Leftover Hash Lemma (LHL) which proves the
analog statement under the statistical, or <span
class="math inline">\(\ell_1\)</span>, distance (for a richer class of
functions) as well as prior work on the expected largest ‘bucket size’
in linear hash functions [ADMPT99]. By known bounds from the load
balancing literature [RS98], our results are tight and show that linear
functions hash as well as trully random function up to a constant factor
in the entropy loss. Our proof leverages a connection between linear
hashing and the finite field Kakeya problem and extends some of the
tools developed in this area, in particular the polynomial method.</p>
