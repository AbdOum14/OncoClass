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
### 1.Manifold Learning (UMAP)
<img width="800" height="500" alt="Image" src="https://github.com/user-attachments/assets/cf04656b-3b85-4bab-b542-2d9b9b269e04" />

***Figure 1: UMAP visualization of the latent space***

**Interpretation:** The UMAP plot shows a clear spatial separation of cancer subtypes. Each cluster represents a distinct transcriptomic signature captured by the **DeepOncoClass** encoder. The high degree of clustering suggests that the model effectively reduced the 20,531 dimensions into a meaningful 64-dimensional latent space, separating biological categories(e.g., BRCA,LUAD) with minimal overlap.
