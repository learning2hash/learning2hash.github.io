---
layout: publication
title: Detecting And Grounding Important Characters In Visual Stories
authors: Danyang Liu, Frank Keller
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2023
bibkey: liu2023detecting
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.17647'}]
tags: ["AAAI", "Datasets"]
short_authors: Danyang Liu, Frank Keller
---
Characters are essential to the plot of any story. Establishing the
characters before writing a story can improve the clarity of the plot and the
overall flow of the narrative. However, previous work on visual storytelling
tends to focus on detecting objects in images and discovering relationships
between them. In this approach, characters are not distinguished from other
objects when they are fed into the generation pipeline. The result is a
coherent sequence of events rather than a character-centric story. In order to
address this limitation, we introduce the VIST-Character dataset, which
provides rich character-centric annotations, including visual and textual
co-reference chains and importance ratings for characters. Based on this
dataset, we propose two new tasks: important character detection and character
grounding in visual stories. For both tasks, we develop simple, unsupervised
models based on distributional similarity and pre-trained vision-and-language
models. Our new dataset, together with these models, can serve as the
foundation for subsequent work on analysing and generating stories from a
character-centric perspective.