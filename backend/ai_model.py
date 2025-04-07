import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd
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
        return (
            torch.tensor([delta_p, flow], dtype=torch.float32),
            torch.tensor(target, dtype=torch.long)
        )


class FilterConditionModel(nn.Module):
    def __init__(self, input_size=2, num_classes=3):
        super(FilterConditionModel, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes)
        )

    def forward(self, x):
        return self.fc(x)


def save_model(model, optimizer, path="filter_model"):
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }, f"{path}.pth")
    print(f"Model saved to {path}.pth")


def load_model(model, optimizer=None, path="filter_model"):
    if os.path.exists(f"{path}.pth"):
        checkpoint = torch.load(f"{path}.pth")
        model.load_state_dict(checkpoint['model_state_dict'])
        if optimizer:
            optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print(f"Model loaded from {path}.pth")
        return True
    return False


def train_model(model, dataloader, criterion, optimizer, epochs=10):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        for inputs, targets in dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()

        avg_loss = total_loss / len(dataloader)
        accuracy = 100 * correct / total
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.4f}, Accuracy: {accuracy:.2f}%")
    return model


def main():
    df = pd.read_csv("data.csv")  

    dataset = FilterDataset(df[['Value1', 'Value2', 'Empty']])
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Инициализация модели
    model = FilterConditionModel(num_classes=3)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Загрузка сохраненной модели
    if not load_model(model, optimizer):
        print("Training new model...")
        model = train_model(model, dataloader, criterion, optimizer, epochs=20)
        save_model(model, optimizer)

    # Пример предсказания
    model.eval()
    test_data = torch.tensor([[5.5, 100.0], [12.0, 85.0]], dtype=torch.float32)
    with torch.no_grad():
        outputs = model(test_data)
        predictions = torch.argmax(outputs, dim=1)
        print("\nPredictions:", predictions.numpy())


if __name__ == "__main__":
    main()
