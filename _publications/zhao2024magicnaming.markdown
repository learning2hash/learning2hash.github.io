---
layout: publication
title: 'Magicnaming: Consistent Identity Generation By Finding A "name Space" In T2I
  Diffusion Models'
authors: Jing Zhao, Heliang Zheng, Chaoyue Wang, Long Lan, Wanrong Hunag, Yuhua Tang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: zhao2024magicnaming
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.14902'}]
tags: ["AAAI"]
short_authors: Zhao et al.
---
Large-scale text-to-image diffusion models, (e.g., DALL-E, SDXL) are capable
of generating famous persons by simply referring to their names. Is it possible
to make such models generate generic identities as simple as the famous ones,
e.g., just use a name? In this paper, we explore the existence of a "Name
Space", where any point in the space corresponds to a specific identity.
Fortunately, we find some clues in the feature space spanned by text embedding
of celebrities' names. Specifically, we first extract the embeddings of
celebrities' names in the Laion5B dataset with the text encoder of diffusion
models. Such embeddings are used as supervision to learn an encoder that can
predict the name (actually an embedding) of a given face image. We
experimentally find that such name embeddings work well in promising the
generated image with good identity consistency. Note that like the names of
celebrities, our predicted name embeddings are disentangled from the semantics
of text inputs, making the original generation capability of text-to-image
models well-preserved. Moreover, by simply plugging such name embeddings, all
variants (e.g., from Civitai) derived from the same base model (i.e., SDXL)
readily become identity-aware text-to-image models. Project homepage:
https://magicfusion.github.io/MagicNaming/.