---
layout: publication
title: 'Online Signature Verification Using Deep Representation: A New Descriptor'
authors: Mohammad Hajizadeh Saffar, Mohsen Fayyaz, Mohammad Sabokrou, Mahmood Fathy
conference: Arxiv
year: 2018
bibkey: saffar2018online
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.09986'}]
tags: []
short_authors: Saffar et al.
---
This paper presents an accurate method for verifying online signatures. The
main difficulty of signature verification come from: (1) Lacking enough
training samples (2) The methods must be spatial change invariant. To deal with
these difficulties and modeling the signatures efficiently, we propose a method
that a one-class classifier per each user is built on discriminative features.
First, we pre-train a sparse auto-encoder using a large number of unlabeled
signatures, then we applied the discriminative features, which are learned by
auto-encoder to represent the training and testing signatures as a self-thought
learning method (i.e. we have introduced a signature descriptor). Finally,
user's signatures are modeled and classified using a one-class classifier. The
proposed method is independent on signature datasets thanks to self-taught
learning. The experimental results indicate significant error reduction and
accuracy enhancement in comparison with state-of-the-art methods on SVC2004 and
SUSIG datasets.