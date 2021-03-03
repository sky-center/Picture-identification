# Picture-identification

该python程序主要功能为按模糊、清晰、损坏三个纬度识别海量图片,并存放在不同的文件夹,图片是否清晰的标准是由阀值threshold参数决定。

# 原理
在通常情况下，图片是否清晰是个感性认识，同一个图，有可能你觉得还过得去，而别人会觉得不清晰，缺乏一个统一的标准。然而有一些算法可以去量化图片的清晰度，做到有章可循。

如果之前了解过信号处理，就会知道最直接的方法是计算图片的快速傅里叶变换，然后查看高低频分布。如果图片有少量的高频成分，那么该图片就可以被认为是模糊的。然而，区分高频量多少的具体阈值却是十分困难的，不恰当的阈值将会导致极差的结果。

我们期望的是一个单一的浮点数就可以表示图片的清晰度。 Pech-Pacheco 在 2000 年模式识别国际会议提出将图片中某一通道（一般用灰度值）通过拉普拉斯掩模做卷积运算，然后计算标准差，出来的值就可以代表图片清晰度。

这种方法凑效的原因就在于拉普拉斯算子定义本身。它被用来测量图片的二阶导数，突出图片中强度快速变化的区域，和 Sobel 以及 Scharr 算子十分相似。并且，和以上算子一样，拉普拉斯算子也经常用于边缘检测。此外，此算法基于以下假设：如果图片具有较高方差，那么它就有较广的频响范围，代表着正常，聚焦准确的图片。但是如果图片具有有较小方差，那么它就有较窄的频响范围，意味着图片中的边缘数量很少。正如我们所知道的，图片越模糊，其边缘就越少。

有了代表清晰度的值，剩下的工作就是设定相应的阀值，如果某图片方差低于预先定义的阈值，那么该图片就可以被认为是模糊的，高于阈值，就不是模糊的。


