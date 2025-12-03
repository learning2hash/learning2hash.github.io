---
layout: publication
title: Test-time Training For Data-efficient UCDR
authors: Soumava Paul, Titir Dutta, Aheli Saha, Abhishek Samanta, Soma Biswas
conference: Arxiv
year: 2022
bibkey: paul2022test
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09198'}]
tags: ["Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Paul et al.
---
Image retrieval under generalized test scenarios has gained significant
momentum in literature, and the recently proposed protocol of Universal
Cross-domain Retrieval is a pioneer in this direction. A common practice in any
such generalized classification or retrieval algorithm is to exploit samples
from many domains during training to learn a domain-invariant representation of
data. Such criterion is often restrictive, and thus in this work, for the first
time, we explore the generalized retrieval problem in a data-efficient manner.
Specifically, we aim to generalize any pre-trained cross-domain retrieval
network towards any unknown query domain/category, by means of adapting the
model on the test data leveraging self-supervised learning techniques. Toward
that goal, we explored different self-supervised loss functions~(for example,
RotNet, JigSaw, Barlow Twins, etc.) and analyze their effectiveness for the
same. Extensive experiments demonstrate the proposed approach is simple, easy
to implement, and effective in handling data-efficient UCDR.