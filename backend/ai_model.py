import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import os


class FilterDataset(Dataset):
    def __init__(self, dataframe):
        self.data = dataframe.values

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        delta_p = self.data[idx, 0]
        flow = self.data[idx, 1]
        target = self.data[idx, 2]
        return torch.tensor([delta_p, flow], dtype=torch.float32), torch.tensor(target / 100, dtype=torch.float32)


class TrainableFilterModel(nn.Module):
    def __init__(self, input_size=2):
        super(TrainableFilterModel, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
        self.register_buffer('delta_p_threshold', torch.tensor([5.0, 10.0]))
        self.register_buffer('flow_threshold', torch.tensor(0.95))

    def forward(self, x):
        wear_pred = self.fc(x)
        delta_p = x[:, 0]
        flow = x[:, 1]
        condition = torch.zeros_like(wear_pred, dtype=torch.long)

        mask_degrad = (delta_p > self.delta_p_threshold[0]) | (flow < self.flow_threshold)
        mask_failed = (delta_p > self.delta_p_threshold[1]) | (flow < 0.9)

        condition[mask_degrad] = 1
        condition[mask_failed] = 2

        return wear_pred.squeeze(), condition


def save_model(model, optimizer, path="model1"):
    """Сохраняет модель и оптимизатор"""
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }, f"{path}.pth")
    print(f"Model saved to {path}.pth")


def load_model(model, optimizer=None, path="model1"):
    """Загружает модель и оптимизатор"""
    if os.path.exists(f"{path}.pth"):
        checkpoint = torch.load(f"{path}.pth")
        model.load_state_dict(checkpoint['model_state_dict'])
        if optimizer:
            optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print(f"Model loaded from {path}.pth")
        return True
    return False


def learn(model, dataloader, criterion, optimizer, epochs=10):
    """Функция обучения модели"""
    for epoch in range(epochs):
        total_loss = 0
        for inputs, targets in dataloader:
            optimizer.zero_grad()
            wear_pred, _ = model(inputs)
            loss = criterion(wear_pred, targets)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.4f}')
    return model


def main():
    # Генерация синтетических данных
    data = {
        'delta_p': np.random.uniform(0, 15, 1000),
        'flow': np.random.uniform(80, 120, 1000),
        'wear_percent': np.random.uniform(0, 100, 1000)
    }
    df = pd.DataFrame(data)
    dataset = FilterDataset(df[['delta_p', 'flow', 'wear_percent']])
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Инициализация модели и оптимизатора
    model = TrainableFilterModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Попытка загрузки сохраненной модели
    if not load_model(model, optimizer):
        print("Training new model...")
        model = learn(model, dataloader, criterion, optimizer)
        save_model(model, optimizer)

    # Пример использования
    test_input = torch.tensor([[7.5, 95.0]], dtype=torch.float32)
    wear, condition = model(test_input)

    print("\nPredictions:")
    print("Wear (%):", (wear.detach().numpy() * 100).round(2))
    print("Conditions:", condition.detach().numpy())


if __name__ == "__main__":
    main()
