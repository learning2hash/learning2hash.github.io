---
layout: publication
title: Paired Cross-modal Data Augmentation For Fine-grained Image-to-text Retrieval
authors: Hao Wang, Guosheng Lin, Steven C. H. Hoi, Chunyan Miao
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: wang2022paired
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.14428'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Wang et al.
---
This paper investigates an open research problem of generating text-image
pairs to improve the training of fine-grained image-to-text cross-modal
retrieval task, and proposes a novel framework for paired data augmentation by
uncovering the hidden semantic information of StyleGAN2 model. Specifically, we
first train a StyleGAN2 model on the given dataset. We then project the real
images back to the latent space of StyleGAN2 to obtain the latent codes. To
make the generated images manipulatable, we further introduce a latent space
alignment module to learn the alignment between StyleGAN2 latent codes and the
corresponding textual caption features. When we do online paired data
augmentation, we first generate augmented text through random token
replacement, then pass the augmented text into the latent space alignment
module to output the latent codes, which are finally fed to StyleGAN2 to
generate the augmented images. We evaluate the efficacy of our augmented data
approach on two public cross-modal retrieval datasets, in which the promising
experimental results demonstrate the augmented text-image pair data can be
trained together with the original data to boost the image-to-text cross-modal
retrieval performance.