---
    layout: publication
    title: "Convolutional Patch Representations for Image Retrieval: an Unsupervised Approach"
    authors: Paulin Mattis  LEAR, Mairal Julien  LEAR, Douze Matthijs  LEAR, Harchaoui Zaid  NYU, Perronnin Florent  LEAR, Schmid Cordelia  LEAR
    conference: Arxiv
    year: 2016
    bibkey: paulin2016convolutional
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1603.00438"}
    tags: ['Arxiv', 'CNN', 'Unsupervised', 'Image Retrieval', 'Supervised']
    ---
    {% raw %}
    Convolutional neural networks (CNNs) have recently received a lot of attention due to their ability to model local stationary structures in natural images in a multi-scale fashion, when learning all model parameters with supervision. While excellent performance was achieved for image classification when large amounts of labeled visual data are available, their success for un-supervised tasks such as image retrieval has been moderate so far. Our paper focuses on this latter setting and explores several methods for learning patch descriptors without supervision with application to matching and instance-level retrieval. To that effect, we propose a new family of convolutional descriptors for patch representation , based on the recently introduced convolutional kernel networks. We show that our descriptor, named Patch-CKN, performs better than SIFT as well as other convolutional networks learned by artificially introducing supervision and is significantly faster to train. To demonstrate its effectiveness, we perform an extensive evaluation on standard benchmarks for patch and image retrieval where we obtain state-of-the-art results. We also introduce a new dataset called RomePatches, which allows to simultaneously study descriptor performance for patch and image retrieval.
    {% endraw %}