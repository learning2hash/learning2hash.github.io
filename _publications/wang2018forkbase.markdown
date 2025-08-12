---
layout: publication
title: 'Forkbase: An Efficient Storage Engine For Blockchain And Forkable Applications'
authors: Sheng Wang, Tien Tuan Anh Dinh, Qian Lin, Zhongle Xie, Meihui Zhang, Qingchao
  Cai, Gang Chen, Wanzeng Fu, Beng Chin Ooi, Pingcheng Ruan
conference: Arxiv
year: 2018
bibkey: wang2018forkbase
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.04949'}]
tags: []
short_authors: Wang et al.
---
Existing data storage systems offer a wide range of functionalities to
accommodate an equally diverse range of applications. However, new classes of
applications have emerged, e.g., blockchain and collaborative analytics,
featuring data versioning, fork semantics, tamper-evidence or any combination
thereof. They present new opportunities for storage systems to efficiently
support such applications by embedding the above requirements into the storage.
  In this paper, we present ForkBase, a storage engine specifically designed to
provide efficient support for blockchain and forkable applications. By
integrating the core application properties into the storage, ForkBase not only
delivers high performance but also reduces development effort. Data in ForkBase
is multi-versioned, and each version uniquely identifies the data content and
its history. Two variants of fork semantics are supported in ForkBase to
facilitate any collaboration workflows. A novel index structure is introduced
to efficiently identify and eliminate duplicate content across data objects.
Consequently, ForkBase is not only efficient in performance, but also in space
requirement. We demonstrate the performance of ForkBase using three
applications: a blockchain platform, a wiki engine and a collaborative
analytics application. We conduct extensive experimental evaluation of these
applications against respective state-of-the-art system. The results show that
ForkBase achieves superior performance while significantly lowering the
development cost.