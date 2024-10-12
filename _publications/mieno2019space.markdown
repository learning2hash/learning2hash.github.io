---
layout: publication
title: Space-efficient Algorithms For Computing Minimal/shortest Unique Substrings
authors: Mieno Takuya, Köppl Dominik, Nakashima Yuto, Inenaga Shunsuke, Bannai Hideo, Takeda Masayuki
conference: "Arxiv"
year: 2019
bibkey: mieno2019space
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1905.12854"}
tags: ['ARXIV']
---
Given a string \{&#37; raw &#37;\}\\(T\\)\{&#37; endraw &#37;\} of length \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\}, a substring \{&#37; raw &#37;\}\\(u = T[i..j]\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(T\\)\{&#37; endraw &#37;\} is called a shortest unique substring (SUS) for an interval \{&#37; raw &#37;\}\\([s,t]\\)\{&#37; endraw &#37;\} if (a) \{&#37; raw &#37;\}\\(u\\)\{&#37; endraw &#37;\} occurs exactly once in \{&#37; raw &#37;\}\\(T\\)\{&#37; endraw &#37;\}, (b) \{&#37; raw &#37;\}\\(u\\)\{&#37; endraw &#37;\} contains the interval \{&#37; raw &#37;\}\\([s,t]\\)\{&#37; endraw &#37;\} (i.e. $i \leq s \leq t \leq j\{&#37; raw &#37;\}\\(), and (c) every substring \\)\{&#37; endraw &#37;\}v\{&#37; raw &#37;\}\\( of \\)\{&#37; endraw &#37;\}T\{&#37; raw &#37;\}\\( with \\)\{&#37; endraw &#37;\}|v| < |u|$ containing \{&#37; raw &#37;\}\\([s,t]\\)\{&#37; endraw &#37;\} occurs at least twice in \{&#37; raw &#37;\}\\(T\\)\{&#37; endraw &#37;\}. Given a query interval $[s, t] \subset [1, n]$, the interval SUS problem is to output all the SUSs for the interval \{&#37; raw &#37;\}\\([s,t]\\)\{&#37; endraw &#37;\}. In this article, we propose a \{&#37; raw &#37;\}\\(4n + o(n)\\)\{&#37; endraw &#37;\} bits data structure answering an interval SUS query in output-sensitive \{&#37; raw &#37;\}\\(O(\mathit\{occ\})\\)\{&#37; endraw &#37;\} time, where \{&#37; raw &#37;\}\\(\mathit\{occ\}\\)\{&#37; endraw &#37;\} is the number of returned SUSs. Additionally, we focus on the point SUS problem, which is the interval SUS problem for \{&#37; raw &#37;\}\\(s = t\\)\{&#37; endraw &#37;\}. Here, we propose a \{&#37; raw &#37;\}\\(\lceil (\log\_2\{3\} + 1)n \rceil + o(n)\\)\{&#37; endraw &#37;\} bits data structure answering a point SUS query in the same output-sensitive time. We also propose space-efficient algorithms for computing the minimal unique substrings of \{&#37; raw &#37;\}\\(T\\)\{&#37; endraw &#37;\}.
