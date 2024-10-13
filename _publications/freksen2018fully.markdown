---
layout: publication
title: Fully Understanding The Hashing Trick
authors: Freksen Casper Benjamin, Kamma Lior, Larsen Kasper Green
conference: "Arxiv"
year: 2018
bibkey: freksen2018fully
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1805.08539"}
tags: ['ARXIV', 'Independent']
---
<p>Feature hashing, also known as {}, introduced by Weinberger et
al. (2009), is one of the key techniques used in scaling-up machine
learning algorithms. Loosely speaking, feature hashing uses a random
sparse projection matrix <span class="math inline">\(A : \mathbb{R}^n
\to \mathbb{R}^m\)</span> (where <span class="math inline">\(m \ll
n\)</span>) in order to reduce the dimension of the data from <span
class="math inline">\(n\)</span> to <span
class="math inline">\(m\)</span> while approximately preserving the
Euclidean norm. Every column of <span class="math inline">\(A\)</span>
contains exactly one non-zero entry, equals to either <span
class="math inline">\(-1\)</span> or <span
class="math inline">\(1\)</span>. Weinberger et al. showed tail bounds
on <span class="math inline">\(\|Ax\|_2^2\)</span>. Specifically they
showed that for every <span class="math inline">\(\varepsilon,
\delta\)</span>, if <span class="math inline">\(\|x\|_{\infty} /
\|x\|_2\)</span> is sufficiently small, and <span
class="math inline">\(m\)</span> is sufficiently large, then <span
class="math display">\[\Pr[ \; |
\;\|Ax\|_2^2 - \|x\|_2^2\; | &lt; \varepsilon \|x\|_2^2 \;] \ge 1 -
\delta \;.\]</span> These bounds were later extended by Dasgupta (2010)
and most recently refined by Dahlgaard et al. (2017), however, the true
nature of the performance of this key technique, and specifically the
correct tradeoff between the pivotal parameters <span
class="math inline">\(\|x\|_{\infty} / \|x\|_2, m, \varepsilon,
\delta\)</span> remained an open question. We settle this question by
giving tight asymptotic bounds on the exact tradeoff between the central
parameters, thus providing a complete understanding of the performance
of feature hashing. We complement the asymptotic bound with empirical
data, which shows that the constants “hiding” in the asymptotic notation
are, in fact, very close to <span class="math inline">\(1\)</span>, thus
further illustrating the tightness of the presented bounds in
practice.</p>
