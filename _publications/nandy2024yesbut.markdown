---
layout: publication
title: 'Yesbut: A High-quality Annotated Multimodal Dataset For Evaluating Satire
  Comprehension Capability Of Vision-language Models'
authors: Abhilash Nandy, Yash Agarwal, Ashish Patwa, Millon Madhur Das, Aman Bansal,
  Ankit Raj, Pawan Goyal, Niloy Ganguly
conference: Arxiv
year: 2024
bibkey: nandy2024yesbut
citations: 0
additional_links: [{name: Code, url: 'https://github.com/abhi1nandy2/yesbut_dataset'},
  {name: Paper, url: 'https://arxiv.org/abs/2409.13592'}]
tags: ["Datasets", "Evaluation"]
short_authors: Nandy et al.
---
Understanding satire and humor is a challenging task for even current
Vision-Language models. In this paper, we propose the challenging tasks of
Satirical Image Detection (detecting whether an image is satirical),
Understanding (generating the reason behind the image being satirical), and
Completion (given one half of the image, selecting the other half from 2 given
options, such that the complete image is satirical) and release a high-quality
dataset YesBut, consisting of 2547 images, 1084 satirical and 1463
non-satirical, containing different artistic styles, to evaluate those tasks.
Each satirical image in the dataset depicts a normal scenario, along with a
conflicting scenario which is funny or ironic. Despite the success of current
Vision-Language Models on multimodal tasks such as Visual QA and Image
Captioning, our benchmarking experiments show that such models perform poorly
on the proposed tasks on the YesBut Dataset in Zero-Shot Settings w.r.t both
automated as well as human evaluation. Additionally, we release a dataset of
119 real, satirical photographs for further research. The dataset and code are
available at https://github.com/abhi1nandy2/yesbut_dataset.