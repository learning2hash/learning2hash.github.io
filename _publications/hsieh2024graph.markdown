---
layout: publication
title: 'Graph-based Captioning: Enhancing Visual Descriptions By Interconnecting Region
  Captions'
authors: "Yu-Guan Hsieh, Cheng-Yu Hsieh, Shih-Ying Yeh, Louis B\xE9thune, Hadi Pour\
  \ Ansari, Pavan Kumar Anasosalu Vasu, Chun-Liang Li, Ranjay Krishna, Oncel Tuzel,\
  \ Marco Cuturi"
conference: Arxiv
year: 2024
bibkey: hsieh2024graph
citations: 0
additional_links: [{name: Code, url: 'https://github.com/apple/ml-gbc'}, {name: Code,
    url: 'https://huggingface.co/graph-based-captions'}, {name: Paper, url: 'https://arxiv.org/abs/2407.06723'}]
tags: []
short_authors: Hsieh et al.
---
Humans describe complex scenes with compositionality, using simple text
descriptions enriched with links and relationships. While vision-language
research has aimed to develop models with compositional understanding
capabilities, this is not reflected yet in existing datasets which, for the
most part, still use plain text to describe images. In this work, we propose a
new annotation strategy, graph-based captioning (GBC) that describes an image
using a labeled graph structure, with nodes of various types. The nodes in GBC
are created through a two-stage process: first, identifying and describing
entity nodes; second, linking these nodes by highlighting \textit\{compositions\}
and \textit\{relations\} among them. Since \textit\{all\} GBC nodes hold plain text
descriptions, GBC retains the flexibility found in natural language, but can
also encode hierarchical information in its edges. We demonstrate that GBC can
be produced automatically, using off-the-shelf multimodal LLMs and object
detection models, by building a new dataset GBC10M that gathers GBC annotations
for about 10M images of the CC12M dataset. Through CLIP training on GBC10M, we
show that leveraging GBC nodes' annotations -- particularly those in
composition and relation nodes -- significantly boosts the model's performance
across various benchmarks compared to when other annotations are used. To
further explore the opportunities provided by GBC, we also investigate the use
of GBC as middleware for text-to-image generation, and show the extra benefits
of incorporating the graph structure in this task. Our code and datasets are
released at https://github.com/apple/ml-gbc and
https://huggingface.co/graph-based-captions.