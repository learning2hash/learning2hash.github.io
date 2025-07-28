---
layout: publication
title: Achieve Efficient Position-heap-based Privacy-preserving Substring-of-keyword
  Query Over Cloud
authors: Fan Yin, Rongxing Lu, Yandong Zheng, Jun Shao, Xue Yang, Xiaohu Tang
conference: Computers &amp; Security
year: 2021
bibkey: yin2021achieve
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.08455'}]
tags: ["Efficiency"]
short_authors: Yin et al.
---
The cloud computing technique, which was initially used to mitigate the
explosive growth of data, has been required to take both data privacy and
users' query functionality into consideration. Symmetric searchable encryption
(SSE) is a popular solution to supporting efficient keyword queries over
encrypted data in the cloud. However, most of the existing SSE schemes focus on
the exact keyword query and cannot work well when the user only remembers the
substring of a keyword, i.e., substring-of-keyword query. This paper aims to
investigate this issue by proposing an efficient and privacy-preserving
substring-of-keyword query scheme over cloud. First, we employ the position
heap technique to design a novel tree-based index to match substrings with
corresponding keywords. Based on the tree-based index, we introduce our
substring-of-keyword query scheme, which contains two consecutive phases. The
first phase queries the keywords that match a given substring, and the second
phase queries the files that match a keyword in which people are really
interested. In addition, detailed security analysis and experimental results
demonstrate the security and efficiency of our proposed scheme.