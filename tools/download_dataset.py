import openxlab
from openxlab.dataset import info
from openxlab.dataset import get
from openxlab.dataset import download


def download_cityscapes():
    openxlab.login(ak="glm8d1rzrz9yplp1y9b0",
                   sk="aanxgexy1m6yl38wmlvr6xnbk5d9r07wpqpzovzb")  # 进行登录，输入对应的AK/SK，可在个人中心添加AK/SK
    info(dataset_repo='OpenDataLab/CityScapes')  # 数据集信息查看
    get(dataset_repo='OpenDataLab/CityScapes', target_path=r'E:\DateSet\CityScapes')  # 数据集下载
    # download(dataset_repo='OpenDataLab/CityScapes',source_path='/README.md', target_path=r'E:\DateSet\CityScapes') #数据集文件下载

if __name__ == "__main__":
    print("下载数据集")

