---
layout: publication
title: 'Scenegraphloc: Cross-modal Coarse Visual Localization On 3D Scene Graphs'
authors: "Yang Miao, Francis Engelmann, Olga Vysotska, Federico Tombari, Marc Pollefeys,\
  \ D\xE1niel B\xE9la Bar\xE1th"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: miao2024scenegraphloc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.00469'}]
tags: [Evaluation]
short_authors: Miao et al.
---
We introduce a novel problem, i.e., the localization of an input image within
a multi-modal reference map represented by a database of 3D scene graphs. These
graphs comprise multiple modalities, including object-level point clouds,
images, attributes, and relationships between objects, offering a lightweight
and efficient alternative to conventional methods that rely on extensive image
databases. Given the available modalities, the proposed method SceneGraphLoc
learns a fixed-sized embedding for each node (i.e., representing an object
instance) in the scene graph, enabling effective matching with the objects
visible in the input query image. This strategy significantly outperforms other
cross-modal methods, even without incorporating images into the map embeddings.
When images are leveraged, SceneGraphLoc achieves performance close to that of
state-of-the-art techniques depending on large image databases, while requiring
three orders-of-magnitude less storage and operating orders-of-magnitude
faster. The code will be made public.