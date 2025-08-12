---
layout: publication
title: How Many Van Goghs Does It Take To Van Gogh? Finding The Imitation Threshold
authors: Sahil Verma, Royi Rassin, Arnav Das, Gantavya Bhatt, Preethi Seshadri, Chirag
  Shah, Jeff Bilmes, Hannaneh Hajishirzi, Yanai Elazar
conference: Arxiv
year: 2024
bibkey: verma2024how
citations: 0
additional_links: [{name: Code, url: 'https://github.com/vsahil/MIMETIC-2.git'}, {
    name: Code, url: 'https://how-many-van-goghs-does-it-take.github.io'}, {name: Paper,
    url: 'https://arxiv.org/abs/2410.15002'}]
tags: []
short_authors: Verma et al.
---
Text-to-image models are trained using large datasets collected by scraping
image-text pairs from the internet. These datasets often include private,
copyrighted, and licensed material. Training models on such datasets enables
them to generate images with such content, which might violate copyright laws
and individual privacy. This phenomenon is termed imitation -- generation of
images with content that has recognizable similarity to its training images. In
this work we study the relationship between a concept's frequency in the
training dataset and the ability of a model to imitate it. We seek to determine
the point at which a model was trained on enough instances to imitate a concept
-- the imitation threshold. We posit this question as a new problem: Finding
the Imitation Threshold (FIT) and propose an efficient approach that estimates
the imitation threshold without incurring the colossal cost of training
multiple models from scratch. We experiment with two domains -- human faces and
art styles -- for which we create four datasets, and evaluate three
text-to-image models which were trained on two pretraining datasets. Our
results reveal that the imitation threshold of these models is in the range of
200-600 images, depending on the domain and the model. The imitation threshold
can provide an empirical basis for copyright violation claims and acts as a
guiding principle for text-to-image model developers that aim to comply with
copyright and privacy laws. We release the code and data at
https://github.com/vsahil/MIMETIC-2.git and the project's website is
hosted at https://how-many-van-goghs-does-it-take.github.io.