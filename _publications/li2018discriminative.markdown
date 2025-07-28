---
layout: publication
title: Discriminative Multi-view Privileged Information Learning For Image Re-ranking
authors: Jun Li, Chang Xu, Wankou Yang, Changyin Sun, Dacheng Tao, Hong Zhang
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: li2018discriminative
citations: 162
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.04437'}]
tags: ["CVPR", "Re-Ranking"]
short_authors: Li et al.
---
Conventional multi-view re-ranking methods usually perform asymmetrical
matching between the region of interest (ROI) in the query image and the whole
target image for similarity computation. Due to the inconsistency in the visual
appearance, this practice tends to degrade the retrieval accuracy particularly
when the image ROI, which is usually interpreted as the image objectness,
accounts for a smaller region in the image. Since Privileged Information (PI),
which can be viewed as the image prior, enables well characterizing the image
objectness, we are aiming at leveraging PI for further improving the
performance of the multi-view re-ranking accuracy in this paper. Towards this
end, we propose a discriminative multi-view re-ranking approach in which both
the original global image visual contents and the local auxiliary PI features
are simultaneously integrated into a unified training framework for generating
the latent subspaces with sufficient discriminating power. For the on-the-fly
re-ranking, since the multi-view PI features are unavailable, we only project
the original multi-view image representations onto the latent subspace, and
thus the re-ranking can be achieved by computing and sorting the distances from
the multi-view embeddings to the separating hyperplane. Extensive experimental
evaluations on the two public benchmarks Oxford5k and Paris6k reveal our
approach provides further performance boost for accurate image re-ranking,
whilst the comparative study demonstrates the advantage of our method against
other multi-view re-ranking methods.