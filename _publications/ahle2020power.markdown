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
The classic way of computing a \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-universal hash function is to use a random degree-\{&#37; raw &#37;\}\\((k-1)\\)\{&#37; endraw &#37;\} polynomial over a prime field \{&#37; raw &#37;\}\\(\mathbb Z\_p\\)\{&#37; endraw &#37;\}. For a fast computation of the polynomial, the prime \{&#37; raw &#37;\}\\(p\\)\{&#37; endraw &#37;\} is often chosen as a Mersenne prime \{&#37; raw &#37;\}\\(p=2^b-1\\)\{&#37; endraw &#37;\}. In this paper, we show that there are other nice advantages to using Mersenne primes. Our view is that the hash function's output is a \{&#37; raw &#37;\}\\(b\\)\{&#37; endraw &#37;\}-bit integer that is uniformly distributed in \{&#37; raw &#37;\}\\(\\{0, \dots, 2^b-1\\}\\)\{&#37; endraw &#37;\}, except that \{&#37; raw &#37;\}\\(p\\)\{&#37; endraw &#37;\} (the all \texttt1s value in binary) is missing. Uniform bit strings have many nice properties, such as splitting into substrings which gives us two or more hash functions for the cost of one, while preserving strong theoretical qualities. We call this trick Two for one hashing, and we demonstrate it on 4-universal hashing in the classic Count Sketch algorithm for second-moment estimation. We also provide a new fast branch-free code for division and modulus with Mersenne primes. Contrasting our analytic work, this code generalizes to any Pseudo-Mersenne primes \{&#37; raw &#37;\}\\(p=2^b-c\\)\{&#37; endraw &#37;\} for small \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}.
