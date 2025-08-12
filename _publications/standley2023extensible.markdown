---
layout: publication
title: An Extensible Multimodal Multi-task Object Dataset With Materials
authors: Trevor Standley, Ruohan Gao, Dawn Chen, Jiajun Wu, Silvio Savarese
conference: Arxiv
year: 2023
bibkey: standley2023extensible
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.14352'}]
tags: ["Datasets"]
short_authors: Standley et al.
---
We present EMMa, an Extensible, Multimodal dataset of Amazon product listings
that contains rich Material annotations. It contains more than 2.8 million
objects, each with image(s), listing text, mass, price, product ratings, and
position in Amazon's product-category taxonomy. We also design a comprehensive
taxonomy of 182 physical materials (e.g., Plastic \(\rightarrow\) Thermoplastic
\(\rightarrow\) Acrylic). Objects are annotated with one or more materials from
this taxonomy. With the numerous attributes available for each object, we
develop a Smart Labeling framework to quickly add new binary labels to all
objects with very little manual labeling effort, making the dataset extensible.
Each object attribute in our dataset can be included in either the model inputs
or outputs, leading to combinatorial possibilities in task configurations. For
example, we can train a model to predict the object category from the listing
text, or the mass and price from the product listing image. EMMa offers a new
benchmark for multi-task learning in computer vision and NLP, and allows
practitioners to efficiently add new tasks and object attributes at scale.