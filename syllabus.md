# Syllabus

This class provides a practical introduction to deep learning, including theoretical motivations and how to implement it in practice. As part of the course we will cover multilayer perceptrons, backpropagation, automatic differentiation, and stochastic gradient descent. Moreover, we introduce convolutional networks for image processing, starting from the simple LeNet to more recent architectures such as ResNet for highly accurate models. Secondly, we discuss sequence models and recurrent networks, such as LSTMs, GRU, and the attention mechanism. Throughout the course we emphasize efficient implementation, optimization and scalability, e.g. to multiple GPUs and to multiple machines. The goal of the course is to provide both a good understanding and good ability to build modern nonparametric estimators. The course loosely follows [Dive into Deep Learning](http://d2l.ai) in terms of notebooks, slides and assignments.

| Date | Topics |
|------|--------|
| 1/22 | [Logistics, Software, Linear Algebra](units/introduction.html) |
| 1/24 | [Probability and Statistics (Bayes Rule, Sampling Naive Bayes, Sampling)](units/probability.html) |
| 1/29 | Arrays, Automatic differentiation, Chain Rule |
| 1/31 | Linear and Logistic regression, Learning rate, Batch size |
| 2/5  | Loss Functions, Likelihood |
| 2/7  | Multilayer Perceptron |
| 2/12 | Capacity Control (models, overfitting, underfitting, weight decay) |
| 2/14 | Making it work - Dropout, Preprocessing, Initialization |
| 2/26 | Environment |
| 2/28 | Layers, Blocks, Parameters and GPUs|
| 3/7  | Convolutional Neural Networks (padding, stride, pooling, channels) |
| 3/12 | LeNet, AlexNet, Blocks |
| 3/14 | Network in Network, Parallel Combination |
| 3/21 | Residual Networks, Batch Normalization |
| 4/2  | Making it work - 100 dogs (ImageNet subset, finetuning) |
| 4/4  | Sequence models and Language |
| 4/9  | Recurrent neural networks, Making it work - language modeling |
| 4/11 | Truncated Backprop, Gated Recurrent Unit, Long Short Term Memory |
| 4/16 | Bi-LSTM, Deep RNNs |
| 4/18 | Optimization Basics (convexity, gradient descent) |
| 4/23 | Stochastic gradient descent), Momentum |
| 4/25 | AdaGrad, Adam, Conditioning, Yogi |
| 4/30 | Parallel Computing (synchronous, asynchronous, parameter server) |
| 5/2  | Making it work - Large scale computer vision models |
