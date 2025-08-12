---
layout: publication
title: Enhancing Visual Classification Using Comparative Descriptors
authors: Hankyeol Lee, Gawon Seo, Wonseok Choi, Geunyoung Jung, Kyungwoo Song, Jiyoung
  Jung
conference: Arxiv
year: 2024
bibkey: lee2024enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.05357'}]
tags: ["Evaluation", "Robustness"]
short_authors: Lee et al.
---
The performance of vision-language models (VLMs), such as CLIP, in visual
classification tasks, has been enhanced by leveraging semantic knowledge from
large language models (LLMs), including GPT. Recent studies have shown that in
zero-shot classification tasks, descriptors incorporating additional cues,
high-level concepts, or even random characters often outperform those using
only the category name. In many classification tasks, while the top-1 accuracy
may be relatively low, the top-5 accuracy is often significantly higher. This
gap implies that most misclassifications occur among a few similar classes,
highlighting the model's difficulty in distinguishing between classes with
subtle differences. To address this challenge, we introduce a novel concept of
comparative descriptors. These descriptors emphasize the unique features of a
target class against its most similar classes, enhancing differentiation. By
generating and integrating these comparative descriptors into the
classification framework, we refine the semantic focus and improve
classification accuracy. An additional filtering process ensures that these
descriptors are closer to the image embeddings in the CLIP space, further
enhancing performance. Our approach demonstrates improved accuracy and
robustness in visual classification tasks by addressing the specific challenge
of subtle inter-class differences.