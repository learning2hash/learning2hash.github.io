---
layout: publication
title: "Multi-View Complementary Hash Tables for Nearest Neighbor Search"
authors: Xianglong Liu, Lei Huang, Cheng Deng, Jiwen Lu and Bo Land
conference: ICCV
year: 2015
bibkey: liu2015multi
additional_links:
   - {name: "PDF", url: "http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Liu_Multi-View_Complementary_Hash_ICCV_2015_paper.pdf"} 
---
Recent years have witnessed the success of hashing techniques in fast nearest neighbor search. In practice many
applications (e.g., visual search, object detection, image
matching, etc.) have enjoyed the benefits of complementary hash tables and information fusion over multiple views.
However, most of prior research mainly focused on compact hash code cleaning, and rare work studies how to build
multiple complementary hash tables, much less to adaptively integrate information stemming from multiple views.
In
this paper we first present a novel multi-view complementary hash table method that learns complementary hash tables from the data with multiple views. For single multiview table, using exemplar based feature fusion, we approximate the inherent data similarities with a low-rank matrix,
and learn discriminative hash functions in an efficient way.
To build complementary tables and meanwhile maintain scalable training and fast out-of-sample extension, an exemplar reweighting scheme is introduced to update the induced low-rank similarity in the sequential table construction framework, which indeed brings mutual benefits between tables by placing greater importance on exemplars
shared by mis-separated neighbors. Extensive experiments
on three large-scale image datasets demonstrate that the
proposed method significantly outperforms various naive
solutions and state-of-the-art multi-table methods.
