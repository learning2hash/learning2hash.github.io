---
layout: publication
title: Reading Scene Text In Deep Convolutional Sequences
authors: Pan He, Weilin Huang, Yu Qiao, Chen Change Loy, Xiaoou Tang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2016
bibkey: he2015reading
citations: 315
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1506.04395'}]
tags: ["AAAI"]
short_authors: He et al.
---
We develop a Deep-Text Recurrent Network (DTRN) that regards scene text
reading as a sequence labelling problem. We leverage recent advances of deep
convolutional neural networks to generate an ordered high-level sequence from a
whole word image, avoiding the difficult character segmentation problem. Then a
deep recurrent model, building on long short-term memory (LSTM), is developed
to robustly recognize the generated CNN sequences, departing from most existing
approaches recognising each character independently. Our model has a number of
appealing properties in comparison to existing scene text recognition methods:
(i) It can recognise highly ambiguous words by leveraging meaningful context
information, allowing it to work reliably without either pre- or
post-processing; (ii) the deep CNN feature is robust to various image
distortions; (iii) it retains the explicit order information in word image,
which is essential to discriminate word strings; (iv) the model does not depend
on pre-defined dictionary, and it can process unknown words and arbitrary
strings. Codes for the DTRN will be available.