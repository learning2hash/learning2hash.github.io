---
layout: publication
title: Fast Nearest Neighbor Machine Translation
authors: Yuxian Meng, Xiaoya Li, Xiayu Zheng, Fei Wu, Xiaofei Sun, Tianwei Zhang,
  Jiwei Li
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: meng2021fast
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.14528'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Meng et al.
---
Though nearest neighbor Machine Translation (\\(k\\)NN-MT)
\citep\{khandelwal2020nearest\} has proved to introduce significant performance
boosts over standard neural MT systems, it is prohibitively slow since it uses
the entire reference corpus as the datastore for the nearest neighbor search.
This means each step for each beam in the beam search has to search over the
entire reference corpus. \\(k\\)NN-MT is thus two-orders slower than vanilla MT
models, making it hard to be applied to real-world applications, especially
online services. In this work, we propose Fast \\(k\\)NN-MT to address this issue.
Fast \\(k\\)NN-MT constructs a significantly smaller datastore for the nearest
neighbor search: for each word in a source sentence, Fast \\(k\\)NN-MT first
selects its nearest token-level neighbors, which is limited to tokens that are
the same as the query token. Then at each decoding step, in contrast to using
the entire corpus as the datastore, the search space is limited to target
tokens corresponding to the previously selected reference source tokens. This
strategy avoids search through the whole datastore for nearest neighbors and
drastically improves decoding efficiency. Without loss of performance, Fast
\\(k\\)NN-MT is two-orders faster than \\(k\\)NN-MT, and is only two times slower than
the standard NMT model. Fast \\(k\\)NN-MT enables the practical use of \\(k\\)NN-MT
systems in real-world MT applications. The code is available at
https://github.com/ShannonAI/fast-knn-nmt