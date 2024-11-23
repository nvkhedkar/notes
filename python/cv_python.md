Using the PyTorch Dataset object, you can perform various operations to manage and manipulate your data effectively. Below are several important functionalities along with code snippets for each.
1. Iterating Through the Dataset
You can iterate over a dataset directly to access individual samples.
python
import torch
from torchvision import datasets, transforms

# Load dataset
transform = transforms.Compose([transforms.ToTensor()])
mnist_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# Iterate through the dataset
for img, label in mnist_dataset:
    print(img.shape, label)
    break  # Just to show the first sample

2. Accessing Samples by Index
You can access specific samples using indexing.
python
# Access the first sample
first_sample = mnist_dataset[0]
img, label = first_sample
print(f'Image shape: {img.shape}, Label: {label}')

3. Creating Subsets
You can create a subset of a dataset using torch.utils.data.Subset.
python
from torch.utils.data import Subset

# Create a subset of the first 100 samples
subset_indices = list(range(100))
mnist_subset = Subset(mnist_dataset, subset_indices)

# Iterate through the subset
for img, label in mnist_subset:
    print(img.shape, label)

4. Applying Transformations
You can apply transformations to your dataset during loading.
python
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Load dataset with transformations
cifar10_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)

# Check transformed image size
img, label = cifar10_dataset[0]
print(f'Transformed Image shape: {img.shape}')

5. Getting Dataset Length
You can retrieve the number of samples in your dataset using the __len__() method.
python
dataset_length = len(mnist_dataset)
print(f'Total number of samples in MNIST dataset: {dataset_length}')

6. Custom Dataset Creation
You can create your own custom dataset by subclassing torch.utils.data.Dataset.
python
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Example usage
data = torch.randn(100, 1)  # Random data
labels = torch.randint(0, 2, (100,))  # Random binary labels
custom_dataset = CustomDataset(data, labels)

7. Using DataLoader for Batching
You can use DataLoader to create batches from your dataset.
python
from torch.utils.data import DataLoader

data_loader = DataLoader(mnist_dataset, batch_size=32, shuffle=True)

for batch_idx, (images, labels) in enumerate(data_loader):
    print(f'Batch {batch_idx}: Image batch shape: {images.shape}, Labels batch shape: {labels.shape}')
    break  # Just show the first batch

8. Shuffling Data
You can shuffle your dataset during loading by setting the shuffle parameter in DataLoader.
python
data_loader = DataLoader(mnist_dataset, batch_size=32, shuffle=True)

for images, labels in data_loader:
    print('Shuffled batch of images and labels')
    break  # Show only one shuffled batch

9. Multi-Processing with DataLoader
You can use multiple workers for loading data to speed up the process.
python
data_loader = DataLoader(mnist_dataset, batch_size=32, shuffle=True, num_workers=4)

for images, labels in data_loader:
    print('Batch loaded with multiple workers')
    break  # Show only one batch loaded with multiple workers

These functionalities highlight the versatility of the PyTorch Dataset object and how it can be effectively utilized for various data handling tasks in machine learning workflows.
