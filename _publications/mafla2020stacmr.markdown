---
layout: publication
title: 'Stacmr: Scene-text Aware Cross-modal Retrieval'
authors: "Andr\xE9s Mafla, Rafael Sampaio de Rezende, Llu\xEDs G\xF3mez, Diane Larlus,\
  \ Dimosthenis Karatzas"
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: mafla2020stacmr
citations: 25
additional_links: [{name: Code, url: 'http://europe'}, {name: Paper, url: 'https://arxiv.org/abs/2012.04329'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Mafla et al.
---
Recent models for cross-modal retrieval have benefited from an increasingly
rich understanding of visual scenes, afforded by scene graphs and object
interactions to mention a few. This has resulted in an improved matching
between the visual representation of an image and the textual representation of
its caption. Yet, current visual representations overlook a key aspect: the
text appearing in images, which may contain crucial information for retrieval.
In this paper, we first propose a new dataset that allows exploration of
cross-modal retrieval where images contain scene-text instances. Then, armed
with this dataset, we describe several approaches which leverage scene text,
including a better scene-text aware cross-modal retrieval method which uses
specialized representations for text from the captions and text from the visual
scene, and reconcile them in a common embedding space. Extensive experiments
confirm that cross-modal retrieval approaches benefit from scene text and
highlight interesting research questions worth exploring further. Dataset and
code are available at http://europe.naverlabs.com/stacmr