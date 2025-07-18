---
layout: publication
title: Zero-shot Hashing Via Transferring Supervised Knowledge
authors: Yang et al.
conference: Proceedings of the 24th ACM international conference on Multimedia
year: 2016
bibkey: yang2016zero
citations: 138
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.05032'}]
tags: [Image Retrieval, DATASETS, Hashing Methods, Efficiency And Optimization, Compact
    Codes, Alt, Tools & Libraries, Evaluation]
---
Hashing has shown its efficiency and effectiveness in facilitating
large-scale multimedia applications. Supervised knowledge e.g. semantic labels
or pair-wise relationship) associated to data is capable of significantly
improving the quality of hash codes and hash functions. However, confronted
with the rapid growth of newly-emerging concepts and multimedia data on the
Web, existing supervised hashing approaches may easily suffer from the scarcity
and validity of supervised information due to the expensive cost of manual
labelling. In this paper, we propose a novel hashing scheme, termed
*zero-shot hashing* (ZSH), which compresses images of "unseen" categories
to binary codes with hash functions learned from limited training data of
"seen" categories. Specifically, we project independent data labels i.e.
0/1-form label vectors) into semantic embedding space, where semantic
relationships among all the labels can be precisely characterized and thus seen
supervised knowledge can be transferred to unseen classes. Moreover, in order
to cope with the semantic shift problem, we rotate the embedded space to more
suitably align the embedded semantics with the low-level visual feature space,
thereby alleviating the influence of semantic gap. In the meantime, to exert
positive effects on learning high-quality hash functions, we further propose to
preserve local structural property and discrete nature in binary codes.
Besides, we develop an efficient alternating algorithm to solve the ZSH model.
Extensive experiments conducted on various real-life datasets show the superior
zero-shot image retrieval performance of ZSH as compared to several
state-of-the-art hashing methods.