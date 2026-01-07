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

### 2.Training Curves (Loss & Accuracy)
<img width="1000" height="300" alt="Image" src="https://github.com/user-attachments/assets/316863dd-5e55-48c3-8b31-9bbf828a450b" />

***Figure 2: Learning dynamics across 15 epochs***

**Interpretation:** The training logs indicate a healthy convergence of the hybrid model. The Loss Curve shows a steady decline without significant gaps between training and validation sets, ruling out overfitting. The Accuracy Curve reaches a plateau near 98-99% within the first 10 epochs, demonstrating that the latent features extracted by the Autoencoder are highly linearly separable for the classification head.

### 3.SHAP for Biomarker Discovery
<img width="600" height="700" alt="Image" src="https://github.com/user-attachments/assets/d126a45e-b005-465a-95c5-6a11074dc860" />

***Figure 3: Learning dynamics across 15 epochs***

**Interpretation:** By applying SHAP (SHapley Additive exPlanations), we identified the top 15 genetic features that drive the model's decisions. Unlike a 'black-box' approach, this plot highlights specific gene indices that act as biomarkers. High SHAP values for a particular gene indicate a strong influence on the probability of a specific cancer class. This interpretability layer is crucial for validating the model against known oncogenic drivers in the TCGA dataset.




