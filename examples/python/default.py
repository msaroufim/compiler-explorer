import torch
import torch.nn as nn
import torch._dynamo
from torch._functorch.aot_autograd import aot_module_simplified

class ToyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        import torch #idk why things break otherwise
        self.l1 = torch.nn.Linear(10,10)
        self.l2 = torch.nn.Linear(10,100)
        
    def forward(self, x):
        return self.l1(self.l2(x))

m = ToyModel()

def toy_backend(gm, sample_inputs):
    print(gm.print_readable())
    return gm.forward

fn = torch.compile(backend=toy_backend, dynamic=True)(m)(torch.randn(10))

