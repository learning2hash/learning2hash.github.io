---
layout: publication
title: Improving The Latent Space Of Image Style Transfer
authors: Yunpeng Bai, Cairong Wang, Chun Yuan, Yanbo Fan, Jue Wang
conference: Arxiv
year: 2022
bibkey: bai2022improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.12135'}]
tags: []
short_authors: Bai et al.
---
Existing neural style transfer researches have studied to match statistical
information between the deep features of content and style images, which were
extracted by a pre-trained VGG, and achieved significant improvement in
synthesizing artistic images. However, in some cases, the feature statistics
from the pre-trained encoder may not be consistent with the visual style we
perceived. For example, the style distance between images of different styles
is less than that of the same style. In such an inappropriate latent space, the
objective function of the existing methods will be optimized in the wrong
direction, resulting in bad stylization results. In addition, the lack of
content details in the features extracted by the pre-trained encoder also leads
to the content leak problem. In order to solve these issues in the latent space
used by style transfer, we propose two contrastive training schemes to get a
refined encoder that is more suitable for this task. The style contrastive loss
pulls the stylized result closer to the same visual style image and pushes it
away from the content image. The content contrastive loss enables the encoder
to retain more available details. We can directly add our training scheme to
some existing style transfer methods and significantly improve their results.
Extensive experimental results demonstrate the effectiveness and superiority of
our methods.