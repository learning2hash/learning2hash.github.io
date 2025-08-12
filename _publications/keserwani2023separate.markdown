---
layout: publication
title: Separate Scene Text Detector For Unseen Scripts Is Not All You Need
authors: Prateek Keserwani, Taveena Lotey, Rohit Keshari, Partha Pratim Roy
conference: Arxiv
year: 2023
bibkey: keserwani2023separate
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.15991'}]
tags: []
short_authors: Keserwani et al.
---
Text detection in the wild is a well-known problem that becomes more
challenging while handling multiple scripts. In the last decade, some scripts
have gained the attention of the research community and achieved good detection
performance. However, many scripts are low-resourced for training deep
learning-based scene text detectors. It raises a critical question: Is there a
need for separate training for new scripts? It is an unexplored query in the
field of scene text detection. This paper acknowledges this problem and
proposes a solution to detect scripts not present during training. In this
work, the analysis has been performed to understand cross-script text
detection, i.e., trained on one and tested on another. We found that the
identical nature of text annotation (word-level/line-level) is crucial for
better cross-script text detection. The different nature of text annotation
between scripts degrades cross-script text detection performance. Additionally,
for unseen script detection, the proposed solution utilizes vector embedding to
map the stroke information of text corresponding to the script category. The
proposed method is validated with a well-known multi-lingual scene text dataset
under a zero-shot setting. The results show the potential of the proposed
method for unseen script detection in natural images.