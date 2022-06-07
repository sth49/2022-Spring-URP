from torchvision.models.inception import inception_v3
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F
from scipy.stats import entropy

def inception_score(gene_imgs, N, bs, use_resize=False, splits=1):
    inception_model = inception_v3(pretrained=True, transform_input=False).cuda()
    inception_model.eval()
    up = nn.Upsample(size=(299, 299), mode="bilinear").cuda()
    preds = np.zeros((N, 1000))
    for i, gene_img in enumerate(gene_imgs):
        gene_img = gene_img.cuda()
        if use_resize: gene_img = up(gene_img)
        pred = F.softmax(inception_model(gene_img)).data.cpu().numpy()
        preds[i * bs : (i+1) * bs] = pred
    split_scores = []

    for k in range(splits):
        part = preds[k * (N // splits): (k + 1) * (N // splits), :]
        py = np.mean(part, axis=0)
        scores = []
        for i in range(part.shape[0]):
            pyx = part[i, :]
            scores.append(entropy(pyx, py))
        split_scores.append(np.exp(np.mean(scores)))
    return np.mean(split_scores), np.std(split_scores)

#### 사용법 ####
# n_IS_val = inception_score(torch_imgs, N, 1)

# torch_images는 N개의 torch.tensor가 담겨잇는 리스트, N은 총 이미지 갯수