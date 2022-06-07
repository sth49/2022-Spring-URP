import os


path = "/media/data1/donghee/VFP290K"
result_dir = "/media/data1/donghee/winter_VFP290K"
dir_list = os.listdir(path)
# print(dir_list)
for dir in dir_list:
    save_dir = os.path.join(result_dir,dir)
    if os.path.isdir(save_dir):
        pass
    else:
        os.makedirs(save_dir)
        print(save_dir)
        dataroot = os.path.join(path,dir)
        dataroot = os.path.join(dataroot, 'images')
        os.system(f'python test.py --dataroot {dataroot} --results_dir {save_dir} --name snowy --epoch 20 --model test --no_dropout --preprocess none')


