---
layout: publication
title: Faster And Simpler Online Computation Of String Net Frequency
authors: Shunsuke Inenaga
conference: Arxiv
year: 2024
bibkey: inenaga2024faster
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.06837'}]
tags: ["Efficiency"]
short_authors: Shunsuke Inenaga
---
An occurrence of a repeated substring \(u\) in a string \(S\) is called a net
occurrence if extending the occurrence to the left or to the right decreases
the number of occurrences to 1. The net frequency (NF) of a repeated substring
\(u\) in a string \(S\) is the number of net occurrences of \(u\) in \(S\). Very
recently, Guo et al. [SPIRE 2024] proposed an online \(O(n log \sigma)\)-time
algorithm that maintains a data structure of \(O(n)\) space which answers
Single-NF queries in \(O(mlog \sigma + \sigma^2)\) time and reports all answers
of the All-NF problem in \(O(n\sigma^2)\) time. Here, \(n\) is the length of the
input string \(S\), \(m\) is the query pattern length, and \(\sigma\) is the alphabet
size. The \(\sigma^2\) term is a major drawback of their method since computing
string net frequencies is originally motivated for Chinese language processing
where \(\sigma\) can be thousands large. This paper presents an improved online
\(O(n log \sigma)\)-time algorithm, which answers Single-NF queries in \(O(m log
\sigma)\) time and reports all answers to the All-NF problem in output-optimal
\(O(|\mathsf\{NF\}^+(S)|)\) time, where \(\mathsf\{NF\}^+(S)\) is the set of substrings
of \(S\) paired with their positive NF values. We note that \(|\mathsf\{NF\}^+(S)| =
O(n)\) always holds. In contract to Guo et al.'s algorithm that is based on
Ukkonen's suffix tree construction, our algorithm is based on Weiner's suffix
tree construction.