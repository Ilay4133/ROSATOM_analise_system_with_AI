import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os
from rosatom_project.backend.math_model_analise import *


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


def save_model(model, optimizer, path="C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filter_model"):
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }, f"{path}.pth")
    print(f"Model saved to {path}.pth")


def load_model(model, optimizer=None, path="C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filter_model") -> bool:
    if os.path.exists(f"{path}.pth"):
        checkpoint = torch.load(f"{path}.pth")
        model.load_state_dict(checkpoint['model_state_dict'])
        if optimizer:
            optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        print(f"Model loaded from {path}.pth")
        return True
    return False


def train_model(model, dataloader, criterion, optimizer, epochs=20):
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


def main1() -> list:
    df = pd.read_csv("C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/data.csv")

    dataset = FilterDataset(df[['Value1', 'Value2', 'Empty']])
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = FilterConditionModel(num_classes=3)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    if not load_model(model, optimizer):
        print("Training new model...")
        model = train_model(model, dataloader, criterion, optimizer, epochs=20)
        save_model(model, optimizer)

    data_list = start_api1()
    print(data_list)
    model.eval()
    data = torch.tensor([data_list], dtype=torch.float32)
    with torch.no_grad():
        outputs = model(data)
        predictions = torch.argmax(outputs, dim=1)
        print("\nPredictions:", predictions.numpy())
    return [predictions[0].item(),data_list[1], data_list[0]]


def model_start1() -> list:
    list_data=main1()
    return list_data


