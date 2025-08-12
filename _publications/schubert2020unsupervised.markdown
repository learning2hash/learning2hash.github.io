---
layout: publication
title: Unsupervised Learning Methods For Visual Place Recognition In Discretely And
  Continuously Changing Environments
authors: Stefan Schubert, Peer Neubert, Peter Protzel
conference: 2020 IEEE International Conference on Robotics and Automation (ICRA)
year: 2020
bibkey: schubert2020unsupervised
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.08960'}]
tags: ["ICRA", "Unsupervised"]
short_authors: Stefan Schubert, Peer Neubert, Peter Protzel
---
Visual place recognition in changing environments is the problem of finding
matchings between two sets of observations, a query set and a reference set,
despite severe appearance changes. Recently, image comparison using CNN-based
descriptors showed very promising results. However, existing experiments from
the literature typically assume a single distinctive condition within each set
(e.g., reference: day, query: night). We demonstrate that as soon as the
conditions change within one set (e.g., reference: day, query: traversal
daytime-dusk-night-dawn), different places under the same condition can
suddenly look more similar than same places under different conditions and
state-of-the-art approaches like CNN-based descriptors fail. This paper
discusses this practically very important problem of in-sequence condition
changes and defines a hierarchy of problem setups from (1) no in-sequence
changes, (2) discrete in-sequence changes, to (3) continuous in-sequence
changes. We will experimentally evaluate the effect of these changes on two
state-of-the-art CNN-descriptors. Our experiments emphasize the importance of
statistical standardization of descriptors and shows its limitations in case of
continuous changes. To address this practically most relevant setup, we
investigate and experimentally evaluate the application of unsupervised
learning methods using two available PCA-based approaches and propose a novel
clustering-based extension of the statistical normalization.