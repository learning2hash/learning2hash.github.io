---
    layout: publication
    title: "Deep Convolutional Features for Image Based Retrieval and Scene Categorization"
    authors: Mousavian Arsalan, Kosecka Jana
    conference: Arxiv
    year: 2015
    bibkey: mousavian2015deep
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1509.06033"}
    tags: ['Arxiv', 'Graph', 'CNN', 'Image Retrieval']
    ---
    {% raw %}
    Several recent approaches showed how the representations learned by Convolutional Neural Networks can be repurposed for novel tasks. Most commonly it has been shown that the activation features of the last fully connected layers (fc7 or fc6) of the network, followed by a linear classifier outperform the state-of-the-art on several recognition challenge datasets. Instead of recognition, this paper focuses on the image retrieval problem and proposes a examines alternative pooling strategies derived for CNN features. The presented scheme uses the features maps from an earlier layer 5 of the CNN architecture, which has been shown to preserve coarse spatial information and is semantically meaningful. We examine several pooling strategies and demonstrate superior performance on the image retrieval task (INRIA Holidays) at the fraction of the computational cost, while using a relatively small memory requirements. In addition to retrieval, we see similar efficiency gains on the SUN397 scene categorization dataset, demonstrating wide applicability of this simple strategy. We also introduce and evaluate a novel GeoPlaces5K dataset from different geographical locations in the world for image retrieval that stresses more dramatic changes in appearance and viewpoint.
    {% endraw %}