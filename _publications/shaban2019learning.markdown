---
layout: publication
title: Learning To Find Common Objects Across Few Image Collections
authors: Amirreza Shaban, Amir Rahimi, Shray Bansal, Stephen Gould, Byron Boots, Richard
  Hartley
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: shaban2019learning
citations: 9
additional_links: [{name: Code, url: 'https://github.com/haamoon/finding_common_object'},
  {name: Paper, url: 'https://arxiv.org/abs/1904.12936'}]
tags: ["Few Shot & Zero Shot", "ICCV"]
short_authors: Shaban et al.
---
Given a collection of bags where each bag is a set of images, our goal is to
select one image from each bag such that the selected images are from the same
object class. We model the selection as an energy minimization problem with
unary and pairwise potential functions. Inspired by recent few-shot learning
algorithms, we propose an approach to learn the potential functions directly
from the data. Furthermore, we propose a fast greedy inference algorithm for
energy minimization. We evaluate our approach on few-shot common object
recognition as well as object co-localization tasks. Our experiments show that
learning the pairwise and unary terms greatly improves the performance of the
model over several well-known methods for these tasks. The proposed greedy
optimization algorithm achieves performance comparable to state-of-the-art
structured inference algorithms while being ~10 times faster. The code is
publicly available on https://github.com/haamoon/finding_common_object.