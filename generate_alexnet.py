'''
Compute and save alexnet features.
@karen-poon
'''
import os
import numpy as np
import torch
import torchvision.models
import torchvision.transforms as transforms

def get_data_loader(path, batch_size):
    transform = transforms.Compose([transforms.Resize((128,128)), transforms.ToTensor()])
    dataset = torchvision.datasets.ImageFolder(path, transform=transform)
    loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, num_workers=1, shuffle=True)
    return loader

def create_alex_tensors(loader, data_type):
    n = 0
    for img, label in train_loader:
        features = alexnet.features(img)
        features_tensor = torch.from_numpy(features.detach().numpy())

        folder_name = master_path + data_type + str(classes[label])
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        torch.save(features_tensor.squeeze(0), folder_name + '/' + str(n) + '.tensor')
        n += 1

if __name__ == '__main__':
    alexnet = torchvision.models.alexnet(pretrained=True) # get alexnet
    master_path =  os.getcwd() + "/alex" # new folder name
    if os.path.exists(master_path):
        print("Please delete the alex folder.")
        exit()

    new_path = os.getcwd() + "/new_processed"
    print("Checking if new_processed exists...")
    if not os.path.exists(new_path):
        print("Please first run split_processed.py or rename the folder back to 'new_processed'")
        exit()

    print("Getting data loaders now...")
    train_loader = get_data_loader(os.getcwd() + "/new_processed/train", 1)
    val_loader = get_data_loader(os.getcwd() + "/new_processed/validation", 1)
    test_loader = get_data_loader(os.getcwd() + "/new_processed/test", 1)
    print("train_loader:", len(train_loader), "val_loader:", len(val_loader), "test_loader:", len(test_loader))

    classes = ["Children0-14", "Youth15-24", "Adults25-64", "Seniors65+"]

    print("Computing and saving training features now...")
    create_alex_tensors(train_loader, "/train/")
    print("training features done.")

    print("Computing and saving validation features now...")
    create_alex_tensors(val_loader, "/validation/")
    print("validation features done.")

    print("Computing and saving test features now...")
    create_alex_tensors(test_loader, "/test/")
    print("test features done.")
    print("All done :)")
    