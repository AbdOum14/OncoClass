import torch
import torch.nn as nn

class DeepOncoClass(nn.Module):
    def __init__(self, input_dim, num_classes):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 128),
            nn.ReLU()
        )
        self.latent = nn.Linear(128, 64)
        self.classifier = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes)
        )

    def forward(self, x):
        x = self.encoder(x)
        z = self.latent(x)
        logits = self.classifier(z)
        return logits, z

def save_model(model, path="model.pth"):
    torch.save(model.state_dict(), path)
    print(f"Modelo guardado en {path}")