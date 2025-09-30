---
layout: publication
title: 'A Sketch Is Worth A Thousand Words: Image Retrieval With Text And Sketch'
authors: Patsorn Sangkloy, Wittawat Jitkrittum, Diyi Yang, James Hays
conference: Lecture Notes in Computer Science
year: 2022
bibkey: sangkloy2022a
citations: 25
additional_links: [{name: Code, url: 'https://janesjanes.github.io/tsbir/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2208.03354'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Large Scale Search"]
short_authors: Sangkloy et al.
---
We address the problem of retrieving images with both a sketch and a text
query. We present TASK-former (Text And SKetch transformer), an end-to-end
trainable model for image retrieval using a text description and a sketch as
input. We argue that both input modalities complement each other in a manner
that cannot be achieved easily by either one alone. TASK-former follows the
late-fusion dual-encoder approach, similar to CLIP, which allows efficient and
scalable retrieval since the retrieval set can be indexed independently of the
queries. We empirically demonstrate that using an input sketch (even a poorly
drawn one) in addition to text considerably increases retrieval recall compared
to traditional text-based image retrieval. To evaluate our approach, we collect
5,000 hand-drawn sketches for images in the test set of the COCO dataset. The
collected sketches are available a https://janesjanes.github.io/tsbir/.