---
layout: publication
title: 'Dyartbank: Diverse Artistic Style Transfer Via Pre-trained Stable Diffusion
  And Dynamic Style Prompt Artbank'
authors: Zhanjie Zhang, Quanwei Zhang, Guangyuan Li, Junsheng Luan, Mengyuan Yang,
  Yun Wang, Lei Zhao
conference: Knowledge-Based Systems
year: 2025
bibkey: zhang2025dyartbank
citations: 3
additional_links: [{name: Code, url: 'https://github.com/Jamie-Cheung/DyArtbank'},
  {name: Paper, url: 'https://arxiv.org/abs/2503.08392'}]
tags: ["Tools & Libraries"]
short_authors: Zhang et al.
---
Artistic style transfer aims to transfer the learned style onto an arbitrary
content image. However, most existing style transfer methods can only render
consistent artistic stylized images, making it difficult for users to get
enough stylized images to enjoy. To solve this issue, we propose a novel
artistic style transfer framework called DyArtbank, which can generate diverse
and highly realistic artistic stylized images. Specifically, we introduce a
Dynamic Style Prompt ArtBank (DSPA), a set of learnable parameters. It can
learn and store the style information from the collection of artworks,
dynamically guiding pre-trained stable diffusion to generate diverse and highly
realistic artistic stylized images. DSPA can also generate random artistic
image samples with the learned style information, providing a new idea for data
augmentation. Besides, a Key Content Feature Prompt (KCFP) module is proposed
to provide sufficient content prompts for pre-trained stable diffusion to
preserve the detailed structure of the input content image. Extensive
qualitative and quantitative experiments verify the effectiveness of our
proposed method. Code is available: https://github.com/Jamie-Cheung/DyArtbank