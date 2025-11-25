---
layout: publication
title: Cross-modal Attribute Insertions For Assessing The Robustness Of Vision-and-language
  Learning
authors: Shivaen Ramshetty, Gaurav Verma, Srijan Kumar
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: ramshetty2023cross
citations: 4
additional_links: [{name: Code, url: 'https://github.com/claws-lab/multimodal-robustness-xmai'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.11065'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Robustness"]
short_authors: Shivaen Ramshetty, Gaurav Verma, Srijan Kumar
---
The robustness of multimodal deep learning models to realistic changes in the
input text is critical for their applicability to important tasks such as
text-to-image retrieval and cross-modal entailment. To measure robustness,
several existing approaches edit the text data, but do so without leveraging
the cross-modal information present in multimodal data. Information from the
visual modality, such as color, size, and shape, provide additional attributes
that users can include in their inputs. Thus, we propose cross-modal attribute
insertions as a realistic perturbation strategy for vision-and-language data
that inserts visual attributes of the objects in the image into the
corresponding text (e.g., "girl on a chair" to "little girl on a wooden
chair"). Our proposed approach for cross-modal attribute insertions is modular,
controllable, and task-agnostic. We find that augmenting input text using
cross-modal insertions causes state-of-the-art approaches for text-to-image
retrieval and cross-modal entailment to perform poorly, resulting in relative
drops of 15% in MRR and 20% in \(F_1\) score, respectively. Crowd-sourced
annotations demonstrate that cross-modal insertions lead to higher quality
augmentations for multimodal data than augmentations using text-only data, and
are equivalent in quality to original examples. We release the code to
encourage robustness evaluations of deep vision-and-language models:
https://github.com/claws-lab/multimodal-robustness-xmai.