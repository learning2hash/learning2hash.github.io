---
layout: publication
title: 'In-style: Bridging Text And Uncurated Videos With Style Transfer For Text-video
  Retrieval'
authors: Nina Shvetsova, Anna Kukleva, Bernt Schiele, Hilde Kuehne
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: shvetsova2023in
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.08928'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "ICCV", "Video Retrieval"]
short_authors: Shvetsova et al.
---
Large-scale noisy web image-text datasets have been proven to be efficient
for learning robust vision-language models. However, when transferring them to
the task of video retrieval, models still need to be fine-tuned on hand-curated
paired text-video data to adapt to the diverse styles of video descriptions. To
address this problem without the need for hand-annotated pairs, we propose a
new setting, text-video retrieval with uncurated & unpaired data, that during
training utilizes only text queries together with uncurated web videos without
any paired text-video data. To this end, we propose an approach, In-Style, that
learns the style of the text queries and transfers it to uncurated web videos.
Moreover, to improve generalization, we show that one model can be trained with
multiple text styles. To this end, we introduce a multi-style contrastive
training procedure that improves the generalizability over several datasets
simultaneously. We evaluate our model on retrieval performance over multiple
datasets to demonstrate the advantages of our style transfer framework on the
new task of uncurated & unpaired text-video retrieval and improve
state-of-the-art performance on zero-shot text-video retrieval.