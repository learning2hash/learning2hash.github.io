---
layout: publication
title: The Power Of Hashing With Mersenne Primes
authors: Ahle Thomas Dybdahl, Knudsen Jakob Tejs Bæk, Thorup Mikkel
conference: "Arxiv"
year: 2020
bibkey: ahle2020power
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2008.08654"}
tags: ['ARXIV', 'Independent']
---
<p>The classic way of computing a <span
class="math inline">\(k\)</span>-universal hash function is to use a
random degree-<span class="math inline">\((k-1)\)</span> polynomial over
a prime field <span class="math inline">\(\mathbb Z_p\)</span>. For a
fast computation of the polynomial, the prime <span
class="math inline">\(p\)</span> is often chosen as a Mersenne prime
<span class="math inline">\(p=2^b-1\)</span>. In this paper, we show
that there are other nice advantages to using Mersenne primes. Our view
is that the hash function’s output is a <span
class="math inline">\(b\)</span>-bit integer that is uniformly
distributed in <span class="math inline">\(\{0, \dots, 2^b-1\}\)</span>,
except that <span class="math inline">\(p\)</span> (the all s value in
binary) is missing. Uniform bit strings have many nice properties, such
as splitting into substrings which gives us two or more hash functions
for the cost of one, while preserving strong theoretical qualities. We
call this trick “Two for one” hashing, and we demonstrate it on
4-universal hashing in the classic Count Sketch algorithm for
second-moment estimation. We also provide a new fast branch-free code
for division and modulus with Mersenne primes. Contrasting our analytic
work, this code generalizes to any Pseudo-Mersenne primes <span
class="math inline">\(p=2^b-c\)</span> for small <span
class="math inline">\(c\)</span>.</p>
