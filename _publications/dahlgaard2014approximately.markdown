---
layout: publication
title: Approximately Minwise Independence With Twisted Tabulation
authors: Dahlgaard Søren, Thorup Mikkel
conference: "Arxiv"
year: 2014
bibkey: dahlgaard2014approximately
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1404.6724"}
tags: ['ARXIV', 'FOCS', 'Independent']
---
A random hash function \{&#37; raw &#37;\}\\(h\\)\{&#37; endraw &#37;\} is \{&#37; raw &#37;\}\\(\varepsilon\\)\{&#37; endraw &#37;\}-minwise if for any set \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\}, \{&#37; raw &#37;\}\\(|S|=n\\)\{&#37; endraw &#37;\}, and element \{&#37; raw &#37;\}\\(x\in S\\)\{&#37; endraw &#37;\}, \{&#37; raw &#37;\}\\(\Pr[h(x)=\min h(S)]=(1\pm\varepsilon)/n\\)\{&#37; endraw &#37;\}. Minwise hash functions with low bias \{&#37; raw &#37;\}\\(\varepsilon\\)\{&#37; endraw &#37;\} have widespread applications within similarity estimation. Hashing from a universe \{&#37; raw &#37;\}\\([u]\\)\{&#37; endraw &#37;\}, the twisted tabulation hashing of P\v\{a\}tra\c\{s\}cu and Thorup [SODA'13] makes \{&#37; raw &#37;\}\\(c=O(1)\\)\{&#37; endraw &#37;\} lookups in tables of size \{&#37; raw &#37;\}\\(u^\{1/c\}\\)\{&#37; endraw &#37;\}. Twisted tabulation was invented to get good concentration for hashing based sampling. Here we show that twisted tabulation yields $\tilde O(1/u^\{1/c\})$-minwise hashing. In the classic independence paradigm of Wegman and Carter [FOCS'79] $\tilde O(1/u^\{1/c\})\{&#37; raw &#37;\}\\(-minwise hashing requires \\)\{&#37; endraw &#37;\}\Omega(\log u)$-independence [Indyk SODA'99]. P\v\{a\}tra\c\{s\}cu and Thorup [STOC'11] had shown that simple tabulation, using same space and lookups yields \{&#37; raw &#37;\}\\(\tilde O(1/n^\{1/c\})\\)\{&#37; endraw &#37;\}-minwise independence, which is good for large sets, but useless for small sets. Our analysis uses some of the same methods, but is much cleaner bypassing a complicated induction argument.
