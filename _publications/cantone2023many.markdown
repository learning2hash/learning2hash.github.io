---
layout: publication
title: The Many Qualities Of A New Directly Accessible Compression Scheme
authors: Domenico Cantone, Simone Faro
conference: Arxiv
year: 2023
bibkey: cantone2023many
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.18063'}]
tags: ["Efficiency"]
short_authors: Domenico Cantone, Simone Faro
---
We present a new variable-length computation-friendly encoding scheme, named
SFDC (Succinct Format with Direct aCcesibility), that supports direct and fast
accessibility to any element of the compressed sequence and achieves
compression ratios often higher than those offered by other solutions in the
literature. The SFDC scheme provides a flexible and simple representation
geared towards either practical efficiency or compression ratios, as required.
For a text of length \(n\) over an alphabet of size \(\sigma\) and a fixed
parameter \(\lambda\), the access time of the proposed encoding is proportional
to the length of the character's code-word, plus an expected
\(\mathcal\{O\}((F_\{\sigma - \lambda + 3\} - 3)/F_\{\sigma+1\})\) overhead, where
\(F_j\) is the \(j\)-th number of the Fibonacci sequence. In the overall it uses
\(N+\mathcal\{O\}\big(n \left(\lambda - (F_\{\sigma+3\}-3)/F_\{\sigma+1\}\big) \right)
= N + \mathcal\{O\}(n)\) bits, where \(N\) is the length of the encoded string.
Experimental results show that the performance of our scheme is, in some
respects, comparable with the performance of DACs and Wavelet Tees, which are
among of the most efficient schemes. In addition our scheme is configured as a
*computation-friendly compression* scheme, as it counts several features
that make it very effective in text processing tasks. In the string matching
problem, that we take as a case study, we experimentally prove that the new
scheme enables results that are up to 29 times faster than standard
string-matching techniques on plain texts.