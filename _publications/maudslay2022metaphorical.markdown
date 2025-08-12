---
layout: publication
title: 'Metaphorical Polysemy Detection: Conventional Metaphor Meets Word Sense Disambiguation'
authors: Rowan Hall Maudslay, Simone Teufel
conference: Arxiv
year: 2022
bibkey: maudslay2022metaphorical
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08395'}]
tags: ["Evaluation"]
short_authors: Rowan Hall Maudslay, Simone Teufel
---
Linguists distinguish between novel and conventional metaphor, a distinction
which the metaphor detection task in NLP does not take into account. Instead,
metaphoricity is formulated as a property of a token in a sentence, regardless
of metaphor type. In this paper, we investigate the limitations of treating
conventional metaphors in this way, and advocate for an alternative which we
name 'metaphorical polysemy detection' (MPD). In MPD, only conventional
metaphoricity is treated, and it is formulated as a property of word senses in
a lexicon. We develop the first MPD model, which learns to identify
conventional metaphors in the English WordNet. To train it, we present a novel
training procedure that combines metaphor detection with word sense
disambiguation (WSD). For evaluation, we manually annotate metaphor in two
subsets of WordNet. Our model significantly outperforms a strong baseline based
on a state-of-the-art metaphor detection model, attaining an ROC-AUC score of
.78 (compared to .65) on one of the sets. Additionally, when paired with a WSD
model, our approach outperforms a state-of-the-art metaphor detection model at
identifying conventional metaphors in text (.659 F1 compared to .626).