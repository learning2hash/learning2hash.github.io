---
layout: publication
title: Fully Understanding The Hashing Trick
authors: Casper B. Freksen, Lior Kamma, Kasper Green Larsen
conference: "Neural Information Processing Systems"
year: 2018
bibkey: b2018fully
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2018/hash/7e83722522e8aeb7512b7075311316b7-Abstract.html"}
tags: ['Independent', 'NEURIPS']
---
Feature hashing, also known as \{\em the hashing trick\}, introduced by Weinberger et al. (2009), is one of the key techniques used in scaling-up machine learning algorithms. Loosely speaking, feature hashing uses a random sparse projection matrix \(A : \mathbb\{R\}^n \to \mathbb\{R\}^m\) (where \(m \ll n\)) in order to reduce the dimension of the data from \(n\) to \(m\) while approximately preserving the Euclidean norm. Every column of \(A\) contains exactly one non-zero entry, equals to either \(-1\) or \(1\). Weinberger et al. showed tail bounds on \(\\|Ax\\|_2^2\). Specifically they showed that for every \(\varepsilon, \delta\), if \(\\|x\\|_\{\infty\} / \\|x\\|_2\) is sufficiently small, and \(m\) is sufficiently large, then \begin\{equation*\}\Pr[ \; \| \;\\|Ax\\|\_2^2 - \\|x\\|\_2^2\; \| < \varepsilon \\|x\\|\_2^2 \;] \ge 1 - \delta \;.\end\{equation*\} These bounds were later extended by Dasgupta et al. (2010) and most recently refined by Dahlgaard et al. (2017), however, the true nature of the performance of this key technique, and specifically the correct tradeoff between the pivotal parameters \(\\|x\\|_\{\infty\} / \\|x\\|_2, m, \varepsilon, \delta\) remained an open question. We settle this question by giving tight asymptotic bounds on the exact tradeoff between the central parameters, thus providing a complete understanding of the performance of feature hashing. We complement the asymptotic bound with empirical data, which shows that the constants hiding in the asymptotic notation are, in fact, very close to \(1\), thus further illustrating the tightness of the presented bounds in practice.
