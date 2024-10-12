---
layout: publication
title: A Hash Table Without Hash Functions And How To Get The Most Out Of Your Random Bits
authors: Kuszmaul William
conference: "Arxiv"
year: 2022
bibkey: kuszmaul2022hash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2209.06038"}
tags: ['ARXIV', 'Independent']
---
This paper considers the basic question of how strong of a probabilistic guarantee can a hash table, storing \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} \{&#37; raw &#37;\}\\((1 + \Theta(1)) \log n\\)\{&#37; endraw &#37;\}-bit key/value pairs, offer? Past work on this question has been bottlenecked by limitations of the known families of hash functions: The only hash tables to achieve failure probabilities less than \{&#37; raw &#37;\}\\(1 / 2^\{\polylog n\}\\)\{&#37; endraw &#37;\} require access to fully-random hash functions -- if the same hash tables are implemented using the known explicit families of hash functions, their failure probabilities become \{&#37; raw &#37;\}\\(1 / \poly(n)\\)\{&#37; endraw &#37;\}. To get around these obstacles, we show how to construct a randomized data structure that has the same guarantees as a hash table, but that \emph\{avoids the direct use of hash functions\}. Building on this, we are able to construct a hash table using \{&#37; raw &#37;\}\\(O(n)\\)\{&#37; endraw &#37;\} random bits that achieves failure probability $1 / n^\{n^\{1 - \epsilon\}\}\{&#37; raw &#37;\}\\( for an arbitrary positive constant \\)\{&#37; endraw &#37;\}\epsilon$. In fact, we show that this guarantee can even be achieved by a \emph\{succinct dictionary\}, that is, by a dictionary that uses space within a \{&#37; raw &#37;\}\\(1 + o(1)\\)\{&#37; endraw &#37;\} factor of the information-theoretic optimum. Finally we also construct a succinct hash table whose probabilistic guarantees fall on a different extreme, offering a failure probability of $1 / \poly(n)\{&#37; raw &#37;\}\\( while using only \\)\{&#37; endraw &#37;\}\tilde\{O\}(\log n)$ random bits. This latter result matches (up to low-order terms) a guarantee previously achieved by Dietzfelbinger et al., but with increased space efficiency and with several surprising technical components.
