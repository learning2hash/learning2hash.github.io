---
layout: publication
title: On Fast Bounded Locality Sensitive Hashing
authors: Piotr Wygocki
conference: Arxiv
year: 2017
bibkey: wygocki2017on
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.05902'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Piotr Wygocki
---
In this paper, we examine the hash functions expressed as scalar products,
i.e., \(f(x)=<v,x>\), for some bounded random vector \(v\). Such hash functions
have numerous applications, but often there is a need to optimize the choice of
the distribution of \(v\). In the present work, we focus on so-called
anti-concentration bounds, i.e. the upper bounds of \(\mathbb\{P\}\left[|<v,x>| <
\alpha \right]\). In many applications, \(v\) is a vector of independent random
variables with standard normal distribution. In such case, the distribution of
\(<v,x>\) is also normal and it is easy to approximate \(\mathbb\{P\}\left[|<v,x>| <
\alpha \right]\). Here, we consider two bounded distributions in the context of
the anti-concentration bounds. Particularly, we analyze \(v\) being a random
vector from the unit ball in \(l_\{\infty\}\) and \(v\) being a random vector from
the unit sphere in \(l_\{2\}\). We show optimal up to a constant anti-concentration
measures for functions \(f(x)=<v,x>\).
  As a consequence of our research, we obtain new best results for \newline
\textit\{\(c\)-approximate nearest neighbors without false negatives\} for \(l_p\) in
high dimensional space for all \(p\in[1,\infty]\), for
\(c=Ω(\max\\{\sqrt\{d\},d^\{1/p\}\\})\). These results improve over those
presented in [16]. Finally, our paper reports progress on answering the open
problem by Pagh~[17], who considered the nearest neighbor search without false
negatives for the Hamming distance.