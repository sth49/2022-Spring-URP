# 2022-Spring-URP

인공지능 모델의 성능의 80%는 데이터의 품질에 달려있다는 말이 과언이 아닐 정도로 모델의 성능에 있어서 데이터는 매우 중요한 역할을 한다. 데이터셋이 부족한 경우 underfitting이나 overfitting과 같은 문제가 발생할 수 있다. 따라서, 이 연구의 목적은 GAN을 사용하여 다양한 데이터를 생성하는 것을 목적으로 한다. 먼저, CycleGAN을 활용한 Data Augmentation 기법을 통해 제한된 도메인의 데이터 셋을 기반으로 다른 도메인 영역의 데이터 셋을 생성하여 인공지능 모델의 성능을 향상시키고 일반화하는 연구를 진행하였다. 또한 다른 X-ray 데이터셋을 이용해 다양한 생성모델을 사용하여 X-ray 데이터를 생성한 후 결과를 분석하였다. 마지막으로, 첫 번째 연구에서 진행한 Snow CycleGAN에 생성을 무효화 시키는 nullifying attack을 적용해보았다.

# 1. Snow Data Augmentation
9000장의 VFP290K와 200장의 눈 데이터인 dawn를 사용해 CycleGAN을 학습시켰다. 학습된 모델을 이용해서 VFP290K의 전체 데이터를 추론하였고, 총 294713장의 데이터가 생성되었다.

```
bash train.sh
```

![1](https://user-images.githubusercontent.com/64757426/173103132-0c282f4c-fd17-4a68-aae5-20eed8def08e.png)

원본이미지:
![원본](https://user-images.githubusercontent.com/64757426/173103978-efaae16c-8987-4906-9bad-e52a46d2d45e.png)

잘 생성된 경우:
![잘생성](https://user-images.githubusercontent.com/64757426/173104086-41b23ed4-1116-4885-91ac-ab04527ab532.png)

못 생성된 경우:
![못생성](https://user-images.githubusercontent.com/64757426/173104131-93bf7d65-959a-4c7a-9ffc-0fedd387deeb.png)


