目录<a NAME="目录">0 目录</a>
====
[1 基本技巧](#基本技巧)  
[代码](#代码)  
[标题](#标题)  
[段落](#段落)  
[粗斜体](#粗斜体)  
[列表](#列表)  
[分割线](#分割线)  
[链接](#链接)  
[图片](#图片)  

[2 高级技巧](#高级技巧)  

[3 参考](#参考)

类似JSON之于XML，Markdown可看作简化版的HTML


<a NAME="基本技巧">1 基本技巧</a>
=====

代码
-----
需要和普通段落之间存在空行

```javascript
$(document).ready(function () {
    alert('hello world');
});
```

    def g(x):
        print('hello world')

-

    void main()
    {
        printf("Hello, world.");
    }



标题
-----

# H1 #
## H2 ##
### H3 ###
#### H4 ####
##### H5 #####
###### H6 ######

段落
----

段落的前后要有空行，所谓的空行是指没有文字内容。  
若想在段内*强制*换行的方式是使用两个以上空格加上回车


粗斜体
----
*斜体文本*    _斜体文本_  
**粗体文本**    __粗体文本__  
***粗斜体文本***    ___粗斜体文本___


列表
----
普通无序列表
在文字开头添加(*, +, and -)实现无序列表。注意在(*, +, and -)和文字之间需要添加一个或以上空格
- 列表文本1
+ 列表文本2
* 列表文本3

普通有序列表
数字后面跟上.号+空格，序号自动增加
1. 列表文本1
2. 列表文本2
7. 列表文本3

列表嵌套

1. 列出所有元素：
    - 无序列表元素 A
        1. 元素 A 的有序子列表
    - 前面加四个空格
2. 列表里的多段换行：
    前面必须加四个空格，
    这样换行，整体的格式不会乱
3. 列表里引用：

    > 前面空一行
    > 仍然需要在 >  前面加四个空格

4. 列表里代码段：

    ```
    前面四个空格，之后按代码语法 ``` 书写
    ```

        或者直接空八个，引入代码块


列表的使用(非traditonal markdown)
----
用|表示表格纵向边界，表头和表内容用-隔开，并可用:进行对齐设置，两边都有:则表示居中，若不加:则默认左对齐。

| head1 | head2| head3 | head4 |
|---|:---|:---:|---:|
|row1text1|row1text3|row1text3|row1text4|
|r2text1|r2text3|r2text3|r2text4|



分割线
----
***
---
___
分割线最常使用就是三个或以上*，还可以使用-和_  
当前后都有段落时，请空出一行


引用
----
普通引用

> 引用文本前使用 [大于号+空格]
> 折行可以不加，新起一行都要加上哦

引用里嵌套引用

> 最外层引用
> > 多一个 > 嵌套一层引用
> > > 可以嵌套很多层

引用里嵌套列表

> - 这是引用里嵌套的一个列表
> - 还可以有子列表
>     * 子列表需要从 - 之后延后四个空格开始

引用里嵌套代码块

>     同样的，在前面加四个空格形成代码块
>  
> ```
> 或者使用 ``` 形成代码块
> ```

区块引用  

在段落的每行或者只在第一行使用符号>,还可使用多个嵌套引用，如：

> 区块引用
>> 嵌套引用
>>> 嵌套引用2

链接
----
文字链接 [链接名称](http://链接网址)
网址链接 <http://链接网址>


  [1]: http://www.google.com/
  [yahoo]: http://www.yahoo.com/
网址链接 [1]
网址链接 [yahoo]  

<address@example.com>

<http://example.com>

图片
----
跟链接的方法区别在于前面加了个感叹号 !  
![图片名称](http://图片网址)

也可以像网址那样对图片网址使用变量  
这个链接用 1 作为网址变量 [Google][1].
然后在文档的结尾位变量赋值（网址）

 [1]: http://www.google.com/logo.png

也可以使用 HTML 的图片语法来自定义图片的宽高大小
<img src="htt://example.com/sample.png" width="400" height="100">


如果比较喜欢 HTML 的 \<a> 或 \<img> 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图片标示语法



反斜杠\
----
取消转义。使符号成为普通符号

符号'`'
---
起到标记作用。如：

`ctrl+a`  

``foo()`` is used.


<a NAME="高级技巧">2 高级技巧</a>
======
### 行内HTML元素 ###

目前只支持部分段内 HTML 元素效果，包括`<kdb> <b> <i> <em> <sup> <sub> <br>` ，如

键位显示

使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑

代码块

使用 \<pre>\</pre> 元素同样可以形成代码块
<pre>
something
</pre>


粗斜体

\<b> Markdown 在此处同样适用，如 <b>加粗</b>

符号转义
----
如果你的描述中需要用到 markdown 的符号，比如 _ # * 等，但又不想它被转义，这时候可以在这些符号前加反斜杠，如 \_ \# \* 进行避免。

\_不想这里的文本变斜体\_
\*\*不想这里的文本被加粗\*\*

扩展
----
支持 jsfiddle、gist、runjs、优酷视频，直接填写 url，在其之后会自动添加预览点击会展开相关内容。

http://{url_of_the_fiddle}/embedded/[{tabs}/[{style}]]/
https://gist.github.com/{gist_id}
http://runjs.cn/detail/{id}
http://v.youku.com/v_show/id_{video_id}.html

公式
----
当你需要在编辑器中插入数学公式时，可以使用两个美元符 $$ 包裹 TeX 或 LaTeX 格式的数学公式来实现。提交后，问答和文章页会根据需要加载 Mathjax 对数学公式进行渲染。如：

$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a}. $$

$$
x \href{why-equal.html}{=} y^2 + 1
$$

同时也支持 HTML 属性，如：

$$ (x+1)^2 = \class{hidden}{(x+1)(x+1)} $$

$$
(x+1)^2 = \cssId{step1}{\style{visibility:hidden}{(x+1)(x+1)}}
$$

<blockquote>Godspeed, my lord
</blockquote>

锚点
---
文中使用锚点

相当于html语法

    <A HREF="#ROP_ARM">ROP_ARM</A>

markdown语法
    当点击\[ROP_ARM](#ROP_ARM)对应位置的文本时，就能跳到\<a NAME="ROP_ARM">内容</a>的位置


例子参本文目录


<a NAME="参考">参考</a>
====

    https://daringfireball.net/projects/markdown/
    https://github.com/younghz/Markdown
    https://havee.me/internet/2013-10/use-table-with-redcarpet-and-markdown-in-jekyll.html
    http://www.ituring.com.cn/article/504
    http://www.jianshu.com/p/1e402922ee32
    http://www.cnblogs.com/rainduck/p/3593870.html
    

[回目录](#目录)
