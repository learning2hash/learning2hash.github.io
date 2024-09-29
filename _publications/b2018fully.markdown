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
Feature hashing also known as 123;em the hashing trick125; introduced by Weinberger et al. (2009) is one of the key techniques used in scaling45;up machine learning algorithms. Loosely speaking feature hashing uses a random sparse projection matrix A R^n to R^m (where m ll n) in order to reduce the dimension of the data from n to m while approximately preserving the Euclidean norm. Every column of A contains exactly one non45;zero entry equals to either 45;1 or 1. Weinberger et al. showed tail bounds on Ax95;2^2. Specifically they showed that for every varepsilon δ if x95;123;∞125; / x95;2 is sufficiently small and m is sufficiently large then begin123;equation125;Pr ; ;Ax95;2^2 45; x95;2^2; < varepsilon x95;2^2 ; ge 1 45; δ ;.end123;equation125; These bounds were later extended by Dasgupta et al. (2010) and most recently refined by Dahlgaard et al. (2017) however the true nature of the performance of this key technique and specifically the correct tradeoff between the pivotal parameters x95;123;∞125; / x95;2 m varepsilon δ remained an open question. We settle this question by giving tight asymptotic bounds on the exact tradeoff between the central parameters thus providing a complete understanding of the performance of feature hashing. We complement the asymptotic bound with empirical data which shows that the constants hiding in the asymptotic notation are in fact very close to 1 thus further illustrating the tightness of the presented bounds in practice.
