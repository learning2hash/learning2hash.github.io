---
layout: publication
title: Why Is Winoground Hard? Investigating Failures In Visuolinguistic Compositionality
authors: Anuj Diwan, Layne Berry, Eunsol Choi, David Harwath, Kyle Mahowald
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: diwan2022why
citations: 14
additional_links: [{name: Code, url: 'https://github.com/ajd12342/why-winoground-hard'},
  {name: Paper, url: 'https://arxiv.org/abs/2211.00768'}]
tags: [EMNLP, Image Retrieval, Datasets]
short_authors: Diwan et al.
---
Recent visuolinguistic pre-trained models show promising progress on various
end tasks such as image retrieval and video captioning. Yet, they fail
miserably on the recently proposed Winoground dataset, which challenges models
to match paired images and English captions, with items constructed to overlap
lexically but differ in meaning (e.g., "there is a mug in some grass" vs.
"there is some grass in a mug"). By annotating the dataset using new
fine-grained tags, we show that solving the Winoground task requires not just
compositional language understanding, but a host of other abilities like
commonsense reasoning or locating small, out-of-focus objects in low-resolution
images. In this paper, we identify the dataset's main challenges through a
suite of experiments on related tasks (probing task, image retrieval task),
data augmentation, and manual inspection of the dataset. Our analysis suggests
that a main challenge in visuolinguistic models may lie in fusing visual and
textual representations, rather than in compositional language understanding.
We release our annotation and code at
https://github.com/ajd12342/why-winoground-hard .