# -*- coding: utf-8 -*-
"""FSL_TieredImageNet_senet_eca_cbam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ufA14XdVQsgtvz9igd3f8WCybOkGduRE
"""

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import multiprocessing as mp
import os
import cv2

import torch
import torch.nn as nn
import torchvision
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torchvision.models import resnet18
from torchvision.models import ResNet

! pip install kaggle
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download arjun2000ashok/tieredimagenet

import pickle

! unzip tieredimagenet.zip -d tieredimagenet

from google.colab import drive
drive.mount('/content/drive')

test_dataset= "/content/tieredimagenet/tiered_imagenet/test"

from PIL import Image

# c_min=2000
# for filename in os.listdir(test_dataset): 
#   filepath=test_dataset+'/'+filename
#   c=0
#   for i in os.listdir(filepath):
#     c=c+1
#   #print(c)
#   if(c_min>c):
#     c_min=c
# print(c_min)



train_dataset= "/content/tieredimagenet/tiered_imagenet/train"

# c_min=2000
# for filename in os.listdir(train_dataset): 
#   filepath=train_dataset+'/'+filename
#   c=0
#   for i in os.listdir(filepath):
#     c=c+1
#   #print(c)
#   if(c_min>c):
#     c_min=c
# print(c_min)

val_dataset= "/content/tieredimagenet/tiered_imagenet/val"

# c_min=2000
# for filename in os.listdir(val_dataset): 
#   filepath=val_dataset+'/'+filename
#   c=0
#   for i in os.listdir(filepath):
#     c=c+1
#   #print(c)
#   if(c_min>c):
#     c_min=c
# print(c_min)

# Just needed in case you'd like to append it to an array
data = []
label=[]
flag=True
for filename in os.listdir(test_dataset): 
    # Your code comes here such as 
    #print(filename)
    indata=[]
    inlabel=[]
    filepath=test_dataset+'/'+filename
    c=0
    for i in os.listdir(filepath):
      if(c==300):
        flag=False
        break
      c=c+1
      img_path=filepath+'/'+i
      img = Image.open(img_path)
      img=img.resize((28, 28))
      img_as_array = np.array(img)/255
      #print(img_as_array.shape)
      if(img_as_array.shape==(28,28)):
        #print(img_as_array.shape)
        img_as_array=np.stack((img_as_array,)*3, axis=-1)
        #print(img_as_array.shape)
      indata.append(img_as_array[:,:,:3])
      
    
    data.append(indata)
    inlabel=[filename]*c
    inlabel=np.array(inlabel)
    label.append(inlabel)

data=np.array(data)



newtestdata=[]
for i in data:
  i=np.array(i)
  newtestdata.append(i)
newtestdata=np.array(newtestdata)

print(newtestdata)

newtestdata=newtestdata.reshape(-1,40,40,3)
newtestdata



data=data.reshape(-1,28,28,3)
data

data.shape

data=data/255

newtestdata=newtestdata/255
newtestdata

testlabel=np.array(label)
testlabel=testlabel.reshape(-1)
testlabel

testlabel.shape

np.save('/content/drive/MyDrive/newtestdata',data)
np.save('/content/drive/MyDrive/testlabel',testlabel)

del testlabel,newtestdata

del data,label,indata,inlabel

# Just needed in case you'd like to append it to an array
data =[]
label=[]
flag=True
for filename in os.listdir(train_dataset): 
        # Your code comes here such as 
    #print(filename)
    indata=[]
    inlabel=[]
    filepath=train_dataset+'/'+filename
    c=0
    for i in os.listdir(filepath):
      if(c==300):
        flag=False
        break
      c=c+1
      img_path=filepath+'/'+i
      img = Image.open(img_path)
      img=img.resize((28, 28))
      img_as_array = np.array(img)/255
      #print(img_as_array.shape)
      if(img_as_array.shape==(28,28)):
        #print(img_as_array.shape)
        img_as_array=np.stack((img_as_array,)*3, axis=-1)
        #print(img_as_array.shape)
      indata.append(img_as_array[:,:,:3])
      
    
    data.append(np.array(indata))
    inlabel=[filename]*c
    inlabel=np.array(inlabel)
    label.append(inlabel)



data=np.array(data)

data.shape

# newtraindata=[]
# for i in data:
#   i=np.array(i)
#   newtraindata.append(i)
# newtraindata=np.array(newtraindata)

# print(newtraindata)

data=data.reshape(-1,28,28,3)
data.shape

newtraindata.shape

newtraindata=newtraindata/255
newtraindata

trainlabel=np.array(label)
trainlabel=trainlabel.reshape(-1)
trainlabel

trainlabel.shape

np.save('/content/drive/MyDrive/newtraindata',data)

# np.save('/content/drive/MyDrive/newtraindata',newtraindata)
np.save('/content/drive/MyDrive/trainlabel',trainlabel)



# Just needed in case you'd like to append it to an array
data =[]
label=[]
flag=True
for filename in os.listdir(val_dataset): 
        # Your code comes here such as 
    #print(filename)
    indata=[]
    inlabel=[]
    filepath=val_dataset+'/'+filename
    c=0
    for i in os.listdir(filepath):
      if(c==732):
        flag=False
        break
      c=c+1
      img_path=filepath+'/'+i
      img = Image.open(img_path)
      img=img.resize((28, 28))
      img_as_array = np.array(img)/255
      #print(img_as_array.shape)
      if(img_as_array.shape==(28,28)):
        #print(img_as_array.shape)
        img_as_array=np.stack((img_as_array,)*3, axis=-1)
        #print(img_as_array.shape)
      indata.append(img_as_array[:,:,:3])
      
    
    data.append(np.array(indata))
    inlabel=[filename]*c
    inlabel=np.array(inlabel)
    label.append(inlabel)

data=np.array(data)

data.shape

data=data.reshape(-1,28,28,3)
data.shape

vallabel=np.array(label)
vallabel=vallabel.reshape(-1)
vallabel

np.save('/content/drive/MyDrive/newvaldata',data)

# np.save('/content/drive/MyDrive/newtraindata',newtraindata)
np.save('/content/drive/MyDrive/vallabel',vallabel)

del testlabel,trainlabel,vallabel

trainx=np.load('/content/drive/MyDrive/newtraindata.npy')
trainy=np.load('/content/drive/MyDrive/trainlabel.npy')

testx=np.load('/content/drive/MyDrive/newtestdata.npy')
testy=np.load('/content/drive/MyDrive/testlabel.npy')

valx=np.load('/content/drive/MyDrive/newvaldata.npy')
valy=np.load('/content/drive/MyDrive/vallabel.npy')

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(newdata, label, test_size=0.2)

from sklearn.model_selection import train_test_split

Xtrain, Xval, ytrain, yval = train_test_split(Xtrain, ytrain, test_size=0.2)

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

from sklearn.model_selection import train_test_split

Xtrain, Xval, ytrain, yval = train_test_split(Xtrain, ytrain, test_size=0.2)

Xtrain.shape

print(torch.cuda.is_available())

trainx, trainy = Xtrain,ytrain

testx, testy = Xtest,ytest

valx,valy=Xval,yval

trainx.shape, trainy.shape, testx.shape, testy.shape

torch.cuda.empty_cache()

def extract_sample(n_way, n_support, n_query, datax, datay):
  """
  Picks random sample of size n_support+n_querry, for n_way classes
  Args:
      n_way (int): number of classes in a classification task
      n_support (int): number of labeled examples per class in the support set
      n_query (int): number of labeled examples per class in the query set
      datax (np.array): dataset of images
      datay (np.array): dataset of labels
  Returns:
      (dict) of:
        (torch.Tensor): sample of images. Size (n_way, n_support+n_query, (dim))
        (int): n_way
        (int): n_support
        (int): n_query
  """
  sample = []
  K = np.random.choice(np.unique(datay), n_way, replace=False)
  for cls in K:
    datax_cls = datax[datay == cls]
    perm = np.random.permutation(datax_cls)
    sample_cls = perm[:(n_support+n_query)]
    sample.append(sample_cls)
  sample = np.array(sample)
  sample = torch.from_numpy(sample).float()
  sample = sample.permute(0,1,4,2,3)
  return({
      'images': sample,
      'n_way': n_way,
      'n_support': n_support,
      'n_query': n_query
      })

def display_sample(sample):
  """
  Displays sample in a grid
  Args:
      sample (torch.Tensor): sample of images to display
  """
  #need 4D tensor to create grid, currently 5D
  sample_4D = sample.view(sample.shape[0]*sample.shape[1],*sample.shape[2:])
  #make a grid
  out = torchvision.utils.make_grid(sample_4D, nrow=sample.shape[1])
  plt.figure(figsize = (16,7))
  plt.imshow(out.permute(1, 2, 0))

sample_example = extract_sample(8, 5, 5, trainx, trainy)
display_sample(sample_example['images'])



class SE_Block(nn.Module):
    "credits: https://github.com/moskomule/senet.pytorch/blob/master/senet/se_module.py#L4"
    def __init__(self, c, r=16):
        super().__init__()
        self.squeeze = nn.AdaptiveAvgPool2d(1)
        self.excitation = nn.Sequential(
            nn.Linear(c, c // r, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(c // r, c, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        bs, c, _, _ = x.shape
        y = self.squeeze(x).view(bs, c)
        y = self.excitation(y).view(bs, c, 1, 1)
        return x * y.expand_as(x)

def conv3x3(in_planes, out_planes, stride=1, groups=1, dilation=1):
    """3x3 convolution with padding"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=dilation, groups=groups, bias=False, dilation=dilation)


def conv1x1(in_planes, out_planes, stride=1):
    """1x1 convolution"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)


def _resnet(arch, block, layers, pretrained, progress, **kwargs):
    model = ResNet(block, layers, **kwargs)
    return model



import torch
from torch import nn
from torch.nn.parameter import Parameter

class eca_layer(nn.Module):
    """Constructs a ECA module.
    Args:
        channel: Number of channels of the input feature map
        k_size: Adaptive selection of kernel size
    """
    def __init__(self, channel, k_size=3):
        super(eca_layer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.conv = nn.Conv1d(1, 1, kernel_size=k_size, padding=(k_size - 1) // 2, bias=False) 
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # feature descriptor on the global spatial information
        y = self.avg_pool(x)

        # Two different branches of ECA module
        y = self.conv(y.squeeze(-1).transpose(-1, -2)).transpose(-1, -2).unsqueeze(-1)

        # Multi-scale information fusion
        y = self.sigmoid(y)

        return x * y.expand_as(x)

import torch
import math
import torch.nn as nn
import torch.nn.functional as F

class BasicConv(nn.Module):
    def __init__(self, in_planes, out_planes, kernel_size, stride=1, padding=0, dilation=1, groups=1, relu=True, bn=True, bias=False):
        super(BasicConv, self).__init__()
        self.out_channels = out_planes
        self.conv = nn.Conv2d(in_planes, out_planes, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        self.bn = nn.BatchNorm2d(out_planes,eps=1e-5, momentum=0.01, affine=True) if bn else None
        self.relu = nn.ReLU() if relu else None

    def forward(self, x):
        x = self.conv(x)
        if self.bn is not None:
            x = self.bn(x)
        if self.relu is not None:
            x = self.relu(x)
        return x

class Flatten(nn.Module):
    def forward(self, x):
        return x.view(x.size(0), -1)

class ChannelGate(nn.Module):
    def __init__(self, gate_channels, reduction_ratio=16, pool_types=['avg', 'max']):
        super(ChannelGate, self).__init__()
        self.gate_channels = gate_channels
        self.mlp = nn.Sequential(
            Flatten(),
            nn.Linear(gate_channels, gate_channels // reduction_ratio),
            nn.ReLU(),
            nn.Linear(gate_channels // reduction_ratio, gate_channels)
            )
        self.pool_types = pool_types
    def forward(self, x):
        channel_att_sum = None
        for pool_type in self.pool_types:
            if pool_type=='avg':
                avg_pool = F.avg_pool2d( x, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( avg_pool )
            elif pool_type=='max':
                max_pool = F.max_pool2d( x, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( max_pool )
            elif pool_type=='lp':
                lp_pool = F.lp_pool2d( x, 2, (x.size(2), x.size(3)), stride=(x.size(2), x.size(3)))
                channel_att_raw = self.mlp( lp_pool )
            elif pool_type=='lse':
                # LSE pool only
                lse_pool = logsumexp_2d(x)
                channel_att_raw = self.mlp( lse_pool )

            if channel_att_sum is None:
                channel_att_sum = channel_att_raw
            else:
                channel_att_sum = channel_att_sum + channel_att_raw

        scale = F.sigmoid( channel_att_sum ).unsqueeze(2).unsqueeze(3).expand_as(x)
        return x * scale

def logsumexp_2d(tensor):
    tensor_flatten = tensor.view(tensor.size(0), tensor.size(1), -1)
    s, _ = torch.max(tensor_flatten, dim=2, keepdim=True)
    outputs = s + (tensor_flatten - s).exp().sum(dim=2, keepdim=True).log()
    return outputs

class ChannelPool(nn.Module):
    def forward(self, x):
        return torch.cat( (torch.max(x,1)[0].unsqueeze(1), torch.mean(x,1).unsqueeze(1)), dim=1 )

class SpatialGate(nn.Module):
    def __init__(self):
        super(SpatialGate, self).__init__()
        kernel_size = 7
        self.compress = ChannelPool()
        self.spatial = BasicConv(2, 1, kernel_size, stride=1, padding=(kernel_size-1) // 2, relu=False)
    def forward(self, x):
        x_compress = self.compress(x)
        x_out = self.spatial(x_compress)
        scale = F.sigmoid(x_out) # broadcasting
        return x * scale

class CBAM(nn.Module):
    def __init__(self, gate_channels, reduction_ratio=16, pool_types=['avg', 'max'], no_spatial=False):
        super(CBAM, self).__init__()
        self.ChannelGate = ChannelGate(gate_channels, reduction_ratio, pool_types)
        self.no_spatial=no_spatial
        if not no_spatial:
            self.SpatialGate = SpatialGate()
    def forward(self, x):
        x_out = self.ChannelGate(x)
        if not self.no_spatial:
            x_out = self.SpatialGate(x_out)
        return x_out

!pip install timm

import timm
model = timm.create_model('seresnet101', pretrained=True)

def se_resnet18(pretrained=False, progress=True, **kwargs):
    return _resnet('resnet18', SEBasicBlock, [2,2,2,2], pretrained, progress,
                   **kwargs)

def se_resnet34(pretrained=False, progress=True, **kwargs):
    return _resnet('resnet34', SEBasicBlock, [3, 4, 6, 3], pretrained, progress,
                   **kwargs)

class Flatten(nn.Module):
  def __init__(self):
    super(Flatten, self).__init__()

  def forward(self, x):
    return x.view(x.size(0), -1)

def load_protonet_conv_se(**kwargs):
  """
  Loads the prototypical network model
  Arg:
      x_dim (tuple): dimension of input image
      hid_dim (int): dimension of hidden layers in conv blocks
      z_dim (int): dimension of embedded image
  Returns:
      Model (Class ProtoNet)
  """
  x_dim = kwargs['x_dim']
  hid_dim = kwargs['hid_dim']
  z_dim = kwargs['z_dim']

  def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  def conv_block_se(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        SE_Block(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  encoder = nn.Sequential(
    conv_block(x_dim[0], hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block_se(hid_dim, z_dim),
    Flatten()
    )
    
  return ProtoNet(encoder)

def load_protonet_conv_eca(**kwargs):
  """
  Loads the prototypical network model
  Arg:
      x_dim (tuple): dimension of input image
      hid_dim (int): dimension of hidden layers in conv blocks
      z_dim (int): dimension of embedded image
  Returns:
      Model (Class ProtoNet)
  """
  x_dim = kwargs['x_dim']
  hid_dim = kwargs['hid_dim']
  z_dim = kwargs['z_dim']

  def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  def conv_block_eca(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        eca_layer(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  encoder = nn.Sequential(
    conv_block(x_dim[0], hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block_eca(hid_dim, z_dim),
    Flatten()
    )
    
  return ProtoNet(encoder)

def load_protonet_conv_cbam(**kwargs):
  """
  Loads the prototypical network model
  Arg:
      x_dim (tuple): dimension of input image
      hid_dim (int): dimension of hidden layers in conv blocks
      z_dim (int): dimension of embedded image
  Returns:
      Model (Class ProtoNet)
  """
  x_dim = kwargs['x_dim']
  hid_dim = kwargs['hid_dim']
  z_dim = kwargs['z_dim']

  def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  def conv_block_cbam(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        CBAM(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  encoder = nn.Sequential(
    conv_block(x_dim[0], hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block_cbam(hid_dim, z_dim),
    Flatten()
    )
    
  return ProtoNet(encoder)

def load_protonet_conv(**kwargs):
  """
  Loads the prototypical network model
  Arg:
      x_dim (tuple): dimension of input image
      hid_dim (int): dimension of hidden layers in conv blocks
      z_dim (int): dimension of embedded image
  Returns:
      Model (Class ProtoNet)
  """
  x_dim = kwargs['x_dim']
  hid_dim = kwargs['hid_dim']
  z_dim = kwargs['z_dim']

  def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  def conv_block_se(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        SE_Block(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
  encoder = nn.Sequential(
    conv_block(x_dim[0], hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, z_dim),
    Flatten()
    )
    
  return ProtoNet(encoder)

"""
class Flatten(nn.Module):
  def __init__(self):
    super(Flatten, self).__init__()

  def forward(self, x):
    return x.view(x.size(0), -1)

def load_protonet_conv(arg=18):
  """
  Loads the prototypical network model
  Arg:
      x_dim (tuple): dimension of input image
      hid_dim (int): dimension of hidden layers in conv blocks
      z_dim (int): dimension of embedded image
  Returns:
      Model (Class ProtoNet)
  """
  """x_dim = kwargs['x_dim']
  hid_dim = kwargs['hid_dim']
  z_dim = kwargs['z_dim']"""

  """def conv_block(in_channels, out_channels):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, 3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(),
        nn.MaxPool2d(2)
        )
    
  encoder = nn.Sequential(
    conv_block(x_dim[0], hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, hid_dim),
    conv_block(hid_dim, z_dim),
    Flatten()
    )"""
  if arg==18:
    convolutional_network = se_resnet18(pretrained=True)
    convolutional_network.fc = nn.Flatten()  
    return ProtoNet(convolutional_network)
  
  if arg==34:
    convolutional_network = se_resnet34(pretrained=True)
    convolutional_network.fc = nn.Flatten()  
    return ProtoNet(convolutional_network)

  if arg==101:
    convolutional_network = timm.create_model('seresnet101', pretrained=True)
    convolutional_network.fc = nn.Flatten()  
    return ProtoNet(convolutional_network)
    
  if arg==152:
    convolutional_network = timm.create_model('seresnet152', pretrained=True)
    convolutional_network.fc = nn.Flatten()  
    return ProtoNet(convolutional_network)
    """

class ProtoNet(nn.Module):
  def __init__(self, encoder):
    """
    Args:
        encoder : CNN encoding the images in sample
        n_way (int): number of classes in a classification task
        n_support (int): number of labeled examples per class in the support set
        n_query (int): number of labeled examples per class in the query set
    """
    super(ProtoNet, self).__init__()
    self.encoder = encoder.cuda()
    #self.encoder=encoder

  def set_forward_loss(self, sample):
    """
    Computes loss, accuracy and output for classification task
    Args:
        sample (torch.Tensor): shape (n_way, n_support+n_query, (dim)) 
    Returns:
        torch.Tensor: shape(2), loss, accuracy and y_hat
    """
    sample_images = sample['images'].cuda()
    #sample_images=sample['images']
    n_way = sample['n_way']
    n_support = sample['n_support']
    n_query = sample['n_query']

    x_support = sample_images[:, :n_support]
    x_query = sample_images[:, n_support:]
   
    #target indices are 0 ... n_way-1
    target_inds = torch.arange(0, n_way).view(n_way, 1, 1).expand(n_way, n_query, 1).long()
    target_inds = Variable(target_inds, requires_grad=False)
    target_inds = target_inds.cuda()
    
   
    #encode images of the support and the query set
    x = torch.cat([x_support.contiguous().view(n_way * n_support, *x_support.size()[2:]),
                   x_query.contiguous().view(n_way * n_query, *x_query.size()[2:])], 0)
   
    z = self.encoder.forward(x)
    z_dim = z.size(-1) #usually 64
    z_proto = z[:n_way*n_support].view(n_way, n_support, z_dim).mean(1)
    z_query = z[n_way*n_support:]

    #compute distances
    dists = euclidean_dist(z_query, z_proto)
    
    #compute probabilities
    log_p_y = F.log_softmax(-dists, dim=1).view(n_way, n_query, -1)
   
    loss_val = -log_p_y.gather(2, target_inds).squeeze().view(-1).mean()
    _, y_hat = log_p_y.max(2)
    acc_val = torch.eq(y_hat, target_inds.squeeze()).float().mean()
   
    return loss_val, {
        'loss': loss_val.item(),
        'acc': acc_val.item(),
        'y_hat': y_hat
        }

def euclidean_dist(x, y):
  """
  Computes euclidean distance btw x and y
  Args:
      x (torch.Tensor): shape (n, d). n usually n_way*n_query
      y (torch.Tensor): shape (m, d). m usually n_way
  Returns:
      torch.Tensor: shape(n, m). For each query, the distances to each centroid
  """
  n = x.size(0)
  m = y.size(0)
  d = x.size(1)
  assert d == y.size(1)

  x = x.unsqueeze(1).expand(n, m, d)
  y = y.unsqueeze(0).expand(n, m, d)

  return torch.pow(x - y, 2).sum(2)

from tqdm import tqdm_notebook
from tqdm import tnrange



def train_MIN(model, optimizer, train_x, train_y,val_x,val_y, n_way, n_support, n_query,max_epoch, epoch_size):
  """
  Trains the protonet
  Args:
      model
      optimizer
      train_x (np.array): images of training set
      train_y(np.array): labels of training set
      n_way (int): number of classes in a classification task
      n_support (int): number of labeled examples per class in the support set
      n_query (int): number of labeled examples per class in the query set
      max_epoch (int): max epochs to train on
      epoch_size (int): episodes per epoch
  """
  #divide the learning rate by 2 at each epoch, as suggested in paper
  scheduler = optim.lr_scheduler.StepLR(optimizer[0], 1, gamma=0.5, last_epoch=-1)
  epoch = 0 #epochs done so far
  stopf = False #status to know when to stop
  stoparr=[False,False,False,False]
  prev_loss=[9999,9999,9999,9999]

  while epoch<max_epoch:
    train_running_loss_nor = 0.0
    train_running_acc_nor = 0.0
    train_running_loss_se = 0.0
    train_running_acc_se = 0.0
    train_running_loss_cbam = 0.0
    train_running_acc_cbam = 0.0
    train_running_loss_eca = 0.0
    train_running_acc_eca = 0.0

    val_running_loss_nor = 0.0
    val_running_acc_nor = 0.0
    val_running_loss_se = 0.0
    val_running_acc_se = 0.0
    val_running_loss_cbam = 0.0
    val_running_acc_cbam = 0.0
    val_running_loss_eca = 0.0
    val_running_acc_eca = 0.0
    
    train_running_loss=[train_running_loss_nor,train_running_loss_se,train_running_loss_cbam,train_running_loss_eca]
    train_running_acc=[train_running_acc_nor,train_running_acc_se,train_running_acc_cbam,train_running_acc_eca]

    val_running_loss=[val_running_loss_nor,val_running_loss_se,val_running_loss_cbam,val_running_loss_eca]
    val_running_acc=[val_running_acc_nor,val_running_acc_se,val_running_acc_cbam,val_running_acc_eca]
    for episode in tnrange(epoch_size, desc="Epoch {:d} train".format(epoch+1)):
      sample = extract_sample(n_way, n_support, n_query, train_x, train_y)
      
      for i in range(len(model)): 
        optimizer[i].zero_grad()
        loss, output = model[i].set_forward_loss(sample)
        train_running_loss[i] += output['loss']
        train_running_acc[i] += output['acc']
        loss.backward()
        optimizer[i].step()
    for episode in tnrange(epoch_size):
      sample = extract_sample(n_way, n_support, n_query, val_x, val_y)
      for i in range(len(model)):
        loss, output = model[i].set_forward_loss(sample)
        val_running_loss[i] += output['loss']
        val_running_acc[i] += output['acc']
    for i in range(len(model)):
      avg_loss = val_running_loss[i] / epoch_size
      avg_acc = val_running_acc[i] / epoch_size
      print('Validation results -- Loss: {:.4f} Acc: {:.4f}'.format(avg_loss, avg_acc))
      if(prev_loss[i]-avg_loss<=0.01):
        print("Validation loss plateus for model",i)
        stoparr[i]=True
        temp=True
        for i in stoparr:
          if i==False:
            temp=False
        if temp==True:
          stopf=True
          break
      prev_loss[i]=avg_loss
      
    for i in range(len(model)):
      epoch_loss = train_running_loss[i] / epoch_size
      epoch_acc = train_running_acc[i] / epoch_size
      print('Training Results: Epoch {:d} -- Loss: {:.4f} Acc: {:.4f}'.format(epoch+1,epoch_loss, epoch_acc))
    epoch += 1
    scheduler.step()

pass
def test_MIN(model, test_x, test_y, n_way, n_support, n_query, test_episode):
  """
  Tests the protonet
  Args:
      model: trained model
      test_x (np.array): images of testing set
      test_y (np.array): labels of testing set
      n_way (int): number of classes in a classification task
      n_support (int): number of labeled examples per class in the support set
      n_query (int): number of labeled examples per class in the query set
      test_episode (int): number of episodes to test on
  """
    running_loss18 = 0.0
    running_acc18 = 0.0
    running_loss34 = 0.0
    running_acc34 = 0.0
    running_loss101 = 0.0
    running_acc101 = 0.0
    running_loss152 = 0.0
    running_acc152 = 0.0

    running_loss=[running_loss18,running_loss34,running_loss101,running_loss152]
    running_acc=[running_acc18,running_acc34,running_acc101,running_acc152]
  for episode in tnrange(test_episode):
    sample = extract_sample(n_way, n_support, n_query, test_x, test_y)
    for i in range(len(model)):
      loss, output = model[i].set_forward_loss(sample)
      running_loss[i] += output['loss']
      running_acc[i] += output['acc']
  for i in range(len(model)):
    avg_loss = running_loss[i] / test_episode
    avg_acc = running_acc[i] / test_episode
    print('Test results -- Loss: {:.4f} Acc: {:.4f}'.format(avg_loss, avg_acc))

pass
def train(model, optimizer, train_x, train_y, n_way, n_support, n_query, max_epoch, epoch_size):
  """
  Trains the protonet
  Args:
      model
      optimizer
      train_x (np.array): images of training set
      train_y(np.array): labels of training set
      n_way (int): number of classes in a classification task
      n_support (int): number of labeled examples per class in the support set
      n_query (int): number of labeled examples per class in the query set
      max_epoch (int): max epochs to train on
      epoch_size (int): episodes per epoch
  """
  #divide the learning rate by 2 at each epoch, as suggested in paper
  scheduler = optim.lr_scheduler.StepLR(optimizer[0], 1, gamma=0.5, last_epoch=-1)
  epoch = 0 #epochs done so far
  stop = False #status to know when to stop

  while epoch < max_epoch and not stop:
    running_loss18 = 0.0
    running_acc18 = 0.0
    running_loss34 = 0.0
    running_acc34 = 0.0
    running_loss101 = 0.0
    running_acc101 = 0.0
    running_loss152 = 0.0
    running_acc152 = 0.0
    
    running_loss=[running_loss18,running_loss34,running_loss101,running_loss152]
    running_acc=[running_acc18,running_acc34,running_acc101,running_acc152]
    for episode in tnrange(epoch_size, desc="Epoch {:d} train".format(epoch+1)):
      sample = extract_sample(n_way, n_support, n_query, train_x, train_y)
      
      for i in range(len(model)): 
        optimizer[i].zero_grad()
        loss, output = model[i].set_forward_loss(sample)
        running_loss[i] += output['loss']
        running_acc[i] += output['acc']
        loss.backward()
        optimizer[i].step()
    for i in range(len(model)):
      epoch_loss = running_loss[i] / epoch_size
      epoch_acc = running_acc[i] / epoch_size
      print('Epoch {:d} -- Loss: {:.4f} Acc: {:.4f}'.format(epoch+1,epoch_loss, epoch_acc))
    epoch += 1
    scheduler.step()

#model18 = load_protonet_conv(arg=18)
#model34 = load_protonet_conv(arg=34)
#model101 = load_protonet_conv(arg=101)
#model152 = load_protonet_conv(arg=152)

model_nor_5=load_protonet_conv(x_dim=(3,28,28),
    hid_dim=64,
    z_dim=64,)
model_se_5=load_protonet_conv_se(x_dim=(3,28,28),
    hid_dim=64,
    z_dim=64,)
model_cbam_5=load_protonet_conv_cbam(x_dim=(3,28,28),
    hid_dim=64,
    z_dim=64,)
model_eca_5=load_protonet_conv_eca(x_dim=(3,28,28),
    hid_dim=64,
    z_dim=64,)


optimizer_nor = optim.Adam(model_nor_5.parameters(), lr = 0.001)
optimizer_se = optim.Adam(model_se_5.parameters(), lr = 0.001)
optimizer_cbam = optim.Adam(model_cbam_5.parameters(), lr = 0.001)
optimizer_eca = optim.Adam(model_eca_5.parameters(), lr = 0.001)

model_5=[model_nor_5,model_se_5,model_cbam_5,model_eca_5]
optimizer_5=[optimizer_nor,optimizer_se,optimizer_cbam,optimizer_eca]

n_way = 20
n_support = 5
n_query = 15

train_x = trainx
train_y = trainy

val_x=valx
val_y=valy

#max_epoch = 5
#epoch_size = 2000

max_epoch = 5
epoch_size = 1000

train_MIN(model_5, optimizer_5, train_x, train_y,val_x,val_y, n_way, n_support, n_query,max_epoch, epoch_size)

#model18 = load_protonet_conv(arg=18)
#model34 = load_protonet_conv(arg=34)
#model101 = load_protonet_conv(arg=101)
#model152 = load_protonet_conv(arg=152)

model_nor_1=load_protonet_conv(x_dim=(3,40,40),
    hid_dim=64,
    z_dim=64,)
model_se_1=load_protonet_conv_se(x_dim=(3,40,40),
    hid_dim=64,
    z_dim=64,)
model_cbam_1=load_protonet_conv_cbam(x_dim=(3,40,40),
    hid_dim=64,
    z_dim=64,)
model_eca_1=load_protonet_conv_eca(x_dim=(3,40,40),
    hid_dim=64,
    z_dim=64,)

optimizer_nor = optim.Adam(model_nor_1.parameters(), lr = 0.001)
optimizer_se = optim.Adam(model_se_1.parameters(), lr = 0.001)
optimizer_cbam = optim.Adam(model_cbam_1.parameters(), lr = 0.001)
optimizer_eca = optim.Adam(model_eca_1.parameters(), lr = 0.001)

model_1=[model_nor_1,model_se_1,model_cbam_1,model_eca_1]
optimizer_1=[optimizer_nor,optimizer_se,optimizer_cbam,optimizer_eca]

n_way = 30
n_support = 1
n_query = 15

train_x = trainx
train_y = trainy

val_x=valx
val_y=valy

#max_epoch = 5
#epoch_size = 2000

max_epoch = 5
epoch_size = 1000

train_MIN(model_1, optimizer_1, train_x, train_y,val_x,val_y, n_way, n_support, n_query,max_epoch, epoch_size)

def test(model, test_x, test_y, n_way, n_support, n_query, test_episode):
  """
  Tests the protonet
  Args:
      model: trained model
      test_x (np.array): images of testing set
      test_y (np.array): labels of testing set
      n_way (int): number of classes in a classification task
      n_support (int): number of labeled examples per class in the support set
      n_query (int): number of labeled examples per class in the query set
      test_episode (int): number of episodes to test on
  """
  running_loss_nor = 0.0
  running_acc_nor = 0.0
  running_loss_se = 0.0
  running_acc_se = 0.0
  running_loss_cbam = 0.0
  running_acc_cbam = 0.0
  running_loss_eca = 0.0
  running_acc_eca = 0.0

  running_loss=[running_loss_nor,running_loss_se,running_loss_cbam,running_loss_eca]
  running_acc=[running_acc_nor,running_acc_se,running_acc_cbam,running_acc_eca]
  for episode in tnrange(test_episode):
    sample = extract_sample(n_way, n_support, n_query, test_x, test_y)
    for i in range(len(model)):
      loss, output = model[i].set_forward_loss(sample)
      running_loss[i] += output['loss']
      running_acc[i] += output['acc']
  for i in range(len(model)):
    avg_loss = running_loss[i] / test_episode
    avg_acc = running_acc[i] / test_episode
    print('Test results -- Loss: {:.4f} Acc: {:.4f}'.format(avg_loss, avg_acc))

"""###5 way 5 shot"""

n_way = 5
n_support = 5
n_query = 15

test_x = testx
test_y = testy

test_episode = 1000

test(model_5, test_x, test_y, n_way, n_support, n_query, test_episode)

"""###20 Way 5 shot"""

n_way = 20
n_support = 5
n_query = 15

test_x = testx
test_y = testy

test_episode = 1000

test(model_5, test_x, test_y, n_way, n_support, n_query, test_episode)



"""###5 way 1 shot"""

n_way = 5
n_support = 1
n_query = 15

test_x = testx
test_y = testy

test_episode = 1000

test(model_1, test_x, test_y, n_way, n_support, n_query, test_episode)

"""###20 Way 1 shot"""

n_way = 20
n_support = 1
n_query = 15

test_x = testx
test_y = testy

test_episode = 1000

test(model_1, test_x, test_y, n_way, n_support, n_query, test_episode)