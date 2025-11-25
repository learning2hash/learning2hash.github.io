---
layout: publication
title: 'Aeye: A Visualization Tool For Image Datasets'
authors: "Florian Gr\xF6tschla, Luca A. Lanzend\xF6rfer, Marco Calzavara, Roger Wattenhofer"
conference: Arxiv
year: 2024
bibkey: "gr\xF6tschla2024aeye"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.04072'}]
tags: ["Datasets", "Tools & Libraries"]
short_authors: "Gr\xF6tschla et al."
---
Image datasets serve as the foundation for machine learning models in
computer vision, significantly influencing model capabilities, performance, and
biases alongside architectural considerations. Therefore, understanding the
composition and distribution of these datasets has become increasingly crucial.
To address the need for intuitive exploration of these datasets, we propose
AEye, an extensible and scalable visualization tool tailored to image datasets.
AEye utilizes a contrastively trained model to embed images into semantically
meaningful high-dimensional representations, facilitating data clustering and
organization. To visualize the high-dimensional representations, we project
them onto a two-dimensional plane and arrange images in layers so users can
seamlessly navigate and explore them interactively. AEye facilitates semantic
search functionalities for both text and image queries, enabling users to
search for content. We open-source the codebase for AEye, and provide a simple
configuration to add datasets.