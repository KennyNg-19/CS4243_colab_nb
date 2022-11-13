# CS4243 How to run code

## Load data

### Images data

Make sure 3 folders, `nomral`, `carrying` and `threat` folders with images are place **in the current directory**.

### Video data



## Run with Loaded model weights

### Image Classfication models

#### LeNet5(inlcuding baseline & improved)

Open the `Lenet5.ipynb` and run all cells, it will read weights from according `LeNet5_XXX` directories. 

Among **top lines of code** in `Lenet5.ipynb,` You can:

![Customeized lines of code](https://tva1.sinaimg.cn/large/008vxvgGgy1h83lnnrnbzj31d80e075w.jpg)

- specify the the baseline or improved LeNet by change the Boolean variable `use_improved_model`;
- **retrain** the model by set the Boolean variable `train_mode` which is `False` in the **Test mode** by defualt **to be True.**

#### VGG



#### ResNet



### Video Classfication

