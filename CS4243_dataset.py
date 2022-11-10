'''
Author: YuhaoWU
Date: 2022-11-09 18:11:44
LastEditors: YuhaoWU
LastEditTime: 2022-11-09 18:47:10
Description: 
'''
from torch.utils.data import Dataset
from PIL import Image
import torch
import os

class CS4243_dataset(Dataset): 
    
    
    def __init__(self, root_path , dataframe, transform=None):
        
        self.classes_mapping = {0:'normal', 1:'carrying', 2:'threat'}
        self.df = dataframe    
        self.transform = transform
        self.root_path = root_path
        
        self.image_paths = self.df['ID'] #image names
        self.labels = self.df['Label']
                

    def __getitem__(self, index):
        
        img_path = self.image_paths[index] # 没有class_file_path
        # print(img_path)
        # 声明class path from 
        class_path = self.classes_mapping[self.labels[index]]
        image = Image.open(os.path.join(self.root_path, class_path, img_path))
        
        target = torch.tensor(self.labels[index])
      
        if self.transform != None:
            image = self.transform(image)
          
        return [image, target]
       
    def __len__(self):
        return len(self.df)