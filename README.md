# OncoClass: Multi-Cancer Classification using Hybrid Autoencoders

## 🧬 Project Overview

OncoClass is a bioinformatics tool designed to classify cancer subtypes based on high dimensional RNA-seq data from the **TCGA Pan-Cancer Dataset**.

The project implements a custom neural network architecture called **Deep OncoClass**, which combines an **Autoencoder** for feature extraction with a robust classifier.This approach reduces 20000+ genetic features into a latent space to identify key biological signatures.

## 🏗️ Architecture: DeepOncoClass
This model is built with PyTorch and features:
***Encoder:*** Layers that compress the genomic fata into a 64 dimensional latent representation.
***Classifier:*** A specialized head that predicts tumor types (BRCA, COAD, KIRC, LUAD, PRAD).
***Interpretability:*** Integrated with **SHAP** for biomarker discovery and **UMAP** for manifold visualzation.

## 📊 Performance & Interpretability
