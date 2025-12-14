---
layout: publication
title: 'Cebin: A Cost-effective Framework For Large-scale Binary Code Similarity Detection'
authors: Hao Wang, Zeyu Gao, Chao Zhang, Mingyang Sun, Yuchen Zhou, Han Qiu, Xi Xiao
conference: Proceedings of the 33rd ACM SIGSOFT International Symposium on Software
  Testing and Analysis
year: 2024
bibkey: wang2024cebin
citations: 14
additional_links: [{name: Code, url: 'https://github.com/Hustcw/CEBin'}, {name: Paper,
    url: 'https://arxiv.org/abs/2402.18818'}]
tags: [Compact Codes, Evaluation, Efficiency, Datasets, Scalability, Tools & Libraries]
short_authors: Wang et al.
---
Binary code similarity detection (BCSD) is a fundamental technique for
various application. Many BCSD solutions have been proposed recently, which
mostly are embedding-based, but have shown limited accuracy and efficiency
especially when the volume of target binaries to search is large. To address
this issue, we propose a cost-effective BCSD framework, CEBin, which fuses
embedding-based and comparison-based approaches to significantly improve
accuracy while minimizing overheads. Specifically, CEBin utilizes a refined
embedding-based approach to extract features of target code, which efficiently
narrows down the scope of candidate similar code and boosts performance. Then,
it utilizes a comparison-based approach that performs a pairwise comparison on
the candidates to capture more nuanced and complex relationships, which greatly
improves the accuracy of similarity detection. By bridging the gap between
embedding-based and comparison-based approaches, CEBin is able to provide an
effective and efficient solution for detecting similar code (including
vulnerable ones) in large-scale software ecosystems. Experimental results on
three well-known datasets demonstrate the superiority of CEBin over existing
state-of-the-art (SOTA) baselines. To further evaluate the usefulness of BCSD
in real world, we construct a large-scale benchmark of vulnerability, offering
the first precise evaluation scheme to assess BCSD methods for the 1-day
vulnerability detection task. CEBin could identify the similar function from
millions of candidate functions in just a few seconds and achieves an
impressive recall rate of \(85.46%\) on this more practical but challenging
task, which are several order of magnitudes faster and \(4.07\times\) better than
the best SOTA baseline. Our code is available at
https://github.com/Hustcw/CEBin.