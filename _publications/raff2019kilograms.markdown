---
layout: publication
title: 'Kilograms: Very Large N-grams For Malware Classification'
authors: Edward Raff, William Fleming, Richard Zak, Hyrum Anderson, Bill Finlayson,
  Charles Nicholas, Mark McLean
conference: Arxiv
year: 2019
bibkey: raff2019kilograms
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.00200'}]
tags: []
short_authors: Raff et al.
---
N-grams have been a common tool for information retrieval and machine
learning applications for decades. In nearly all previous works, only a few
values of \(n\) are tested, with \(n > 6\) being exceedingly rare. Larger values of
\(n\) are not tested due to computational burden or the fear of overfitting. In
this work, we present a method to find the top-\(k\) most frequent \(n\)-grams that
is 60\(\times\) faster for small \(n\), and can tackle large \(n\geq1024\). Despite
the unprecedented size of \(n\) considered, we show how these features still have
predictive ability for malware classification tasks. More important, large
\(n\)-grams provide benefits in producing features that are interpretable by
malware analysis, and can be used to create general purpose signatures
compatible with industry standard tools like Yara. Furthermore, the counts of
common \(n\)-grams in a file may be added as features to publicly available
human-engineered features that rival efficacy of professionally-developed
features when used to train gradient-boosted decision tree models on the EMBER
dataset.