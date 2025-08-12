---
layout: publication
title: Cross-x Learning For Fine-grained Visual Categorization
authors: Wei Luo, Xitong Yang, Xianjie Mo, Yuheng Lu, Larry S. Davis, Jun Li, Jian
  Yang, Ser-Nam Lim
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: luo2019cross
citations: 227
additional_links: [{name: Code, url: 'https://github.com/cswluo/CrossX'}, {name: Paper,
    url: 'https://arxiv.org/abs/1909.04412'}]
tags: ["ICCV"]
short_authors: Luo et al.
---
Recognizing objects from subcategories with very subtle differences remains a
challenging task due to the large intra-class and small inter-class variation.
Recent work tackles this problem in a weakly-supervised manner: object parts
are first detected and the corresponding part-specific features are extracted
for fine-grained classification. However, these methods typically treat the
part-specific features of each image in isolation while neglecting their
relationships between different images. In this paper, we propose Cross-X
learning, a simple yet effective approach that exploits the relationships
between different images and between different network layers for robust
multi-scale feature learning. Our approach involves two novel components: (i) a
cross-category cross-semantic regularizer that guides the extracted features to
represent semantic parts and, (ii) a cross-layer regularizer that improves the
robustness of multi-scale features by matching the prediction distribution
across multiple layers. Our approach can be easily trained end-to-end and is
scalable to large datasets like NABirds. We empirically analyze the
contributions of different components of our approach and demonstrate its
robustness, effectiveness and state-of-the-art performance on five benchmark
datasets. Code is available at https://github.com/cswluo/CrossX.