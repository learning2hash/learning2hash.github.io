---
layout: publication
title: 'Fusion Hashing: A General Framework For Self-improvement Of Hashing'
authors: Xingbo Liu, Xiushan Nie, Yilong Yin
conference: Arxiv
year: 2018
bibkey: liu2018fusion
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.00644'}]
tags: [Efficiency, Hashing Methods, Datasets, Evaluation, Tools & Libraries, Similarity
    Search]
short_authors: Xingbo Liu, Xiushan Nie, Yilong Yin
---
Hashing has been widely used for efficient similarity search based on its
query and storage efficiency. To obtain better precision, most studies focus on
designing different objective functions with different constraints or penalty
terms that consider neighborhood information. In this paper, in contrast to
existing hashing methods, we propose a novel generalized framework called
fusion hashing (FH) to improve the precision of existing hashing methods
without adding new constraints or penalty terms. In the proposed FH, given an
existing hashing method, we first execute it several times to get several
different hash codes for a set of training samples. We then propose two novel
fusion strategies that combine these different hash codes into one set of final
hash codes. Based on the final hash codes, we learn a simple linear hash
function for the samples that can significantly improve model precision. In
general, the proposed FH can be adopted in existing hashing method and achieve
more precise and stable performance compared to the original hashing method
with little extra expenditure in terms of time and space. Extensive experiments
were performed based on three benchmark datasets and the results demonstrate
the superior performance of the proposed framework