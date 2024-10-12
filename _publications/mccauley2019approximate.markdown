---
layout: publication
title: Approximate Similarity Search Under Edit Distance Using Locality-sensitive Hashing
authors: Mccauley Samuel
conference: "Arxiv"
year: 2019
bibkey: mccauley2019approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1907.01600"}
tags: ['ARXIV', 'Independent']
---
Edit distance similarity search, also called approximate pattern matching, is a fundamental problem with widespread database applications. The goal of the problem is to preprocess \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} strings of length \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\}, to quickly answer queries \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\} of the form: if there is a database string within edit distance \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}, return a database string within edit distance \{&#37; raw &#37;\}\\(cr\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(q\\)\{&#37; endraw &#37;\}. Previous approaches to this problem either rely on very large (superconstant) approximation ratios \{&#37; raw &#37;\}\\(c\\)\{&#37; endraw &#37;\}, or very small search radii \{&#37; raw &#37;\}\\(r\\)\{&#37; endraw &#37;\}. Outside of a narrow parameter range, these solutions are not competitive with trivially searching through all \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} strings. In this work give a simple and easy-to-implement hash function that can quickly answer queries for a wide range of parameters. Specifically, our strategy can answer queries in time \{&#37; raw &#37;\}\\(\tilde\{O\}(d3^rn^\{1/c\})\\)\{&#37; endraw &#37;\}. The best known practical results require \{&#37; raw &#37;\}\\(c \gg r\\)\{&#37; endraw &#37;\} to achieve any correctness guarantee; meanwhile, the best known theoretical results are very involved and difficult to implement, and require query time at least \{&#37; raw &#37;\}\\(24^r\\)\{&#37; endraw &#37;\}. Our results significantly broaden the range of parameters for which we can achieve nontrivial bounds, while retaining the practicality of a locality-sensitive hash function. We also show how to apply our ideas to the closely-related Approximate Nearest Neighbor problem for edit distance, obtaining similar time bounds.
