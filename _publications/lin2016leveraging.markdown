---
layout: publication
title: Leveraging Visual Question Answering For Image-caption Ranking
authors: Xiao Lin, Devi Parikh
conference: Lecture Notes in Computer Science
year: 2016
bibkey: lin2016leveraging
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.01379'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Xiao Lin, Devi Parikh
---
Visual Question Answering (VQA) is the task of taking as input an image and a
free-form natural language question about the image, and producing an accurate
answer. In this work we view VQA as a "feature extraction" module to extract
image and caption representations. We employ these representations for the task
of image-caption ranking. Each feature dimension captures (imagines) whether a
fact (question-answer pair) could plausibly be true for the image and caption.
This allows the model to interpret images and captions from a wide variety of
perspectives. We propose score-level and representation-level fusion models to
incorporate VQA knowledge in an existing state-of-the-art VQA-agnostic
image-caption ranking model. We find that incorporating and reasoning about
consistency between images and captions significantly improves performance.
Concretely, our model improves state-of-the-art on caption retrieval by 7.1%
and on image retrieval by 4.4% on the MSCOCO dataset.