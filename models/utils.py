import torch
import torch.nn as nn
import torch.nn.functional as F

class AtrousSeparableConvolution(nn.Module):
    """ Atrous Separable Convolution
    """
    def __init__(self, in_channels, out_channels, kernel_size,
                            stride=1, padding=0, dilation=1, bias=True, momentum=0.1):
        super(AtrousSeparableConvolution, self).__init__()
        self.body = nn.Sequential(
            # Separable Conv
            nn.Conv2d( in_channels, in_channels, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation, bias=bias, groups=in_channels ),
            nn.BatchNorm2d( in_channels, momentum=momentum ),
            nn.ReLU(inplace=True),
            # PointWise Conv
            nn.Conv2d( in_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=bias),
            nn.BatchNorm2d( out_channels, momentum=momentum ),
            nn.ReLU(inplace=True)
        )


    def forward(self, x):
        return self.body(x)