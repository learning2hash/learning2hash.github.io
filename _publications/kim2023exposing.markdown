---
layout: publication
title: Exposing And Mitigating Spurious Correlations For Cross-modal Retrieval
authors: Jae Myung Kim, A. Sophia Koepke, Cordelia Schmid, Zeynep Akata
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2023
bibkey: kim2023exposing
citations: 16
additional_links: [{name: Code, url: 'https://github.com/ExplainableML/Spurious_CM_Retrieval.'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.03391'}]
tags: ["CVPR", "Evaluation", "Multimodal Retrieval", "Robustness", "Text Retrieval"]
short_authors: Kim et al.
---
Cross-modal retrieval methods are the preferred tool to search databases for
the text that best matches a query image and vice versa. However, image-text
retrieval models commonly learn to memorize spurious correlations in the
training data, such as frequent object co-occurrence, instead of looking at the
actual underlying reasons for the prediction in the image. For image-text
retrieval, this manifests in retrieved sentences that mention objects that are
not present in the query image. In this work, we introduce ODmAP@k, an object
decorrelation metric that measures a model's robustness to spurious
correlations in the training data. We use automatic image and text
manipulations to control the presence of such object correlations in designated
test data. Additionally, our data synthesis technique is used to tackle model
biases due to spurious correlations of semantically unrelated objects in the
training data. We apply our proposed pipeline, which involves the finetuning of
image-text retrieval frameworks on carefully designed synthetic data, to three
state-of-the-art models for image-text retrieval. This results in significant
improvements for all three models, both in terms of the standard retrieval
performance and in terms of our object decorrelation metric. The code is
available at https://github.com/ExplainableML/Spurious_CM_Retrieval.