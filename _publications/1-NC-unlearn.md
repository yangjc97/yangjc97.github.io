---
title: "Resistive Memory based Efficient Machine Unlearning and Continual Learning"
collection: publications
category: manuscripts
permalink: /publication/1-NC-unlearn
date: 2026-01-15
venue: 'Under Review'
excerpt: 'Ning Lin†, <b>Jichang Yang†</b>, Yangu He†, Zijian Ye, Kwun Hang Wong, Xinyuan Zhang, Songqi Wang, Yi Li, Kemi Xu, Leo Yu Zhang, Xiaoming Chen, Dashan Shang, Han Wang, Xiaojuan Qi, Zhongrui Wang'
paperurl: 'https://arxiv.org/abs/2601.10037'
---

Resistive memory (RM) based neuromorphic systems can emulate synaptic plasticity and thus support continual learning, but they generally lack biologically inspired mechanisms for active forgetting, which are critical for meeting modern data privacy requirements. Algorithmic forgetting, or machine unlearning, seeks to remove the influence of specific data from trained models to prevent memorization of sensitive information and the generation of harmful content, yet existing exact and approximate unlearning schemes incur prohibitive programming overheads on RM hardware owing to device variability and iterative write-verify cycles. Analogue implementations of continual learning face similar barriers. Here we present a hardware-software co-design that enables an efficient training, deployment and inference pipeline for machine unlearning and continual learning on RM accelerators. At the software level, we introduce a low-rank adaptation (LoRA) framework that confines updates to compact parameter branches, substantially reducing the number of trainable parameters and therefore the training cost. At the hardware level, we develop a hybrid analogue-digital compute-in-memory system in which well-trained weights are stored in analogue RM arrays, whereas dynamic LoRA updates are implemented in a digital computing unit with SRAM buffer. This hybrid architecture avoids costly reprogramming of analogue weights and maintains high energy efficiency during inference. Fabricated in a 180 nm CMOS process, the prototype achieves up to a 147.76-fold reduction in training cost, a 387.95-fold reduction in deployment overhead and a 48.44-fold reduction in inference energy across privacy-sensitive tasks including face recognition, speaker authentication and stylized image generation, paving the way for secure and efficient neuromorphic intelligence at the edge.
