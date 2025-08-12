---
layout: publication
title: Two-stream Fcns To Balance Content And Style For Style Transfer
authors: Duc Minh Vo, Akihiro Sugimoto
conference: Machine Vision and Applications
year: 2020
bibkey: vo2019two
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.08079'}]
tags: []
short_authors: Duc Minh Vo, Akihiro Sugimoto
---
Style transfer is to render given image contents in given styles, and it has
an important role in both computer vision fundamental research and industrial
applications. Following the success of deep learning based approaches, this
problem has been re-launched recently, but still remains a difficult task
because of trade-off between preserving contents and faithful rendering of
styles. Indeed, how well-balanced content and style are is crucial in
evaluating the quality of stylized images. In this paper, we propose an
end-to-end two-stream Fully Convolutional Networks (FCNs) aiming at balancing
the contributions of the content and the style in rendered images. Our proposed
network consists of the encoder and decoder parts. The encoder part utilizes a
FCN for content and a FCN for style where the two FCNs have feature injections
and are independently trained to preserve the semantic content and to learn the
faithful style representation in each. The semantic content feature and the
style representation feature are then concatenated adaptively and fed into the
decoder to generate style-transferred (stylized) images. In order to train our
proposed network, we employ a loss network, the pre-trained VGG-16, to compute
content loss and style loss, both of which are efficiently used for the feature
injection as well as the feature concatenation. Our intensive experiments show
that our proposed model generates more balanced stylized images in content and
style than state-of-the-art methods. Moreover, our proposed network achieves
efficiency in speed.