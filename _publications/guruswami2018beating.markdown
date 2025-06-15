---
layout: publication
title: 'Beating Fredman-koml\''{o}s For Perfect \(k\)-hashing'
authors: Venkatesan Guruswami, Andrii Riazanov
conference: "Arxiv"
year: 2018
citations: 9
bibkey: guruswami2018beating
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1805.04151'}
tags: ['Cross-Modal', 'Independent', 'Shallow', 'Vector Indexing', 'Training Strategy', 'Hashing']
---
We say a subset \\(C \subseteq \\{1,2,\dots,k\\}^n\\) is a \\(k\\)-hash code (also
called \\(k\\)-separated) if for every subset of \\(k\\) codewords from \\(C\\), there
exists a coordinate where all these codewords have distinct values.
Understanding the largest possible rate (in bits), defined as \\((log_2 |C|)/n\\),
of a \\(k\\)-hash code is a classical problem. It arises in two equivalent
contexts: (i) the smallest size possible for a perfect hash family that maps a
universe of \\(N\\) elements into \\(\\{1,2,\dots,k\\}\\), and (ii) the zero-error
capacity for decoding with lists of size less than \\(k\\) for a certain
combinatorial channel.
  A general upper bound of \\(k!/k^\{k-1\}\\) on the rate of a \\(k\\)-hash code (in the
limit of large \\(n\\)) was obtained by Fredman and Koml\'\{o\}s in 1984 for any \\(k
\geq 4\\). While better bounds have been obtained for \\(k=4\\), their original bound
has remained the best known for each \\(k \ge 5\\). In this work, we obtain the
first improvement to the Fredman-Koml\'\{o\}s bound for every \\(k \ge 5\\). While we
get explicit (numerical) bounds for \\(k=5,6\\), for larger \\(k\\) we only show that
the FK bound can be improved by a positive, but unspecified, amount. Under a
conjecture on the optimum value of a certain polynomial optimization problem
over the simplex, our methods allow an effective bound to be computed for every
\\(k\\).
