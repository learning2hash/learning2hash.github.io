---
layout: publication
title: Detecting Unseen Visual Relations Using Analogies
authors: Julia Peyre, Ivan Laptev, Cordelia Schmid, Josef Sivic
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: peyre2018detecting
citations: 117
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.05736'}]
tags: [Datasets, ICCV]
short_authors: Peyre et al.
---
We seek to detect visual relations in images of the form of triplets t =
(subject, predicate, object), such as "person riding dog", where training
examples of the individual entities are available but their combinations are
unseen at training. This is an important set-up due to the combinatorial nature
of visual relations : collecting sufficient training data for all possible
triplets would be very hard. The contributions of this work are three-fold.
First, we learn a representation of visual relations that combines (i)
individual embeddings for subject, object and predicate together with (ii) a
visual phrase embedding that represents the relation triplet. Second, we learn
how to transfer visual phrase embeddings from existing training triplets to
unseen test triplets using analogies between relations that involve similar
objects. Third, we demonstrate the benefits of our approach on three
challenging datasets : on HICO-DET, our model achieves significant improvement
over a strong baseline for both frequent and unseen triplets, and we observe
similar improvement for the retrieval of unseen triplets with out-of-vocabulary
predicates on the COCO-a dataset as well as the challenging unusual triplets in
the UnRel dataset.