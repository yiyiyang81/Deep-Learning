# Deep Learning

## Overview

This repository contains three deep learning projects, focusing on various deep learning techniques including Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Transformers. Each assignment is designed to provide practical experience with these models through hands-on projects.

## Repository Breakdown

## Project 1: Image Classification with Convolutional Neural Networks

### Objective

Develop a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset, aiming to achieve high accuracy and efficiency.

### What I Did

- **Dataset Preparation:** Loaded and preprocessed the CIFAR-10 dataset, normalizing images and converting labels.
- **Model Implementation:** Designed a CNN architecture using PyTorch, with convolutional, pooling, and fully connected layers.
- **Training:** Trained the CNN on the CIFAR-10 dataset, monitoring the training process and implementing early stopping.
- **Evaluation:** Evaluated the model on the test dataset, achieving reasonable accuracy and comparing performance with baseline models.

## Project 2: Text Generation with RNNs

### Objective

Implement a Recurrent Neural Network (RNN) to generate text data in the style of Shakespeare, demonstrating the capabilities of RNNs in sequence generation tasks.

### What I Did

- **Data Preprocessing:** Tokenized and cleaned the Shakespeare dataset, converting text into sequences for the RNN.
- **Model Implementation:** Implemented an LSTM model using PyTorch for character-level text generation.
- **Training:** Trained the LSTM on the processed dataset, incorporating dropout layers to prevent overfitting.
- **Text Generation:** Generated new text that mimics Shakespeare's style using the trained model.


## Project 3: Multi-class Text Classification using Transformers

### Objective

Utilize a Transformer model to perform multi-class text classification on the 20 Newsgroups dataset, achieving high performance and leveraging state-of-the-art deep learning techniques.

### What I Did

- **Data Preprocessing:** Tokenized and preprocessed the 20 Newsgroups dataset, preparing it for classification.
- **Model Implementation:** Used a pre-trained GPT-2 model and fine-tuned it for multi-class text classification.
- **Training:** Trained the transformer model on the processed dataset, implementing checkpoints and validation.
- **Evaluation:** Evaluated the model on a test set, achieving strong performance metrics and comparing with benchmarks.
