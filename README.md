# 揭开Gradle的神秘面纱
![gradle｜center](https://jackwaylong.github.io/silentor/img/xmind/gradle.jpg)

> gradle前言
 
在解开gradle神秘面纱前,我想说一下gradle是如此的强大,在我看来在目前互联网爆炸的时代,构建工具也不少,比如以前我接触的Ant,maven等,在这里只想说我接触gradle并且去研究之后,从此我就爱上了gradle的强大，灵活，高效，并且可以让我们android开发者上手快，这是因为我们android开发的主要语言是java，java是基于虚拟的一种语言，而gradle的最终产物也是java子节码，所以我认为我们写gadle代码就是写业务代码，当然也有不同，那就是dsl特性，后面会慢慢展开讲解，让大家真正的去理解gradle的强大，并且能够真正的在as的强大能力下，能够将gardle真正运用好，提高开发效率。这里我并不是吐槽其他构件工具不好,没有最好，只有更好，更适合，从客户端构件角度来看，我个人觉得gradle非常适合，下面将解开gradle一层一层的面纱。

> gradle大纲

- gradle是什么
- gradle的好处
- gradle内部构建原理
- 如何使用gradle提高工作效率
- gradle工程构建流
- gradle实战

## gradle是什么
> gradle其实是一套构件工具机,使用groovy语言的DSL特性以及java的灵活特性进行构建,还有很多特性大家可以去[gradle.org](https://gradle.org/)官网进行深入的学习或者`google`找相关资料了解

## gradle的好处
> 其实我们学习一门技术肯定是有对应的好处我们才去学习对吧,不管好处多大,起码能帮助我们工作,毕竟我们都是上班的码农,我个人认为gradle最大的好处就是能够让我们更关注我们最关注的，不需要关注那些与我们关系不大的，毕竟我们不需要关注，然而这样就让我们失去了很多的深入学习的机会，导致我们养成了只要能用就行的思维，在我看来懒惰使人进步，为了想懒惰我一定要去思考如何自动化的去解决问题，gradle满足了我的目标，非常强大。

## gradle的内部构建原理
> 在讲解内部构件原理之前，我想讲解下我是如何去理解gradle这玩意的，gradle按照一般写业务代码的思维还是有点区别的，毕竟领域不同，gradle写的是脚本，却运行的java子节码，所以我这么思考，我用写java运行时的思维去写gradle脚本，然后学习gradle dsl特性，这样以来，理解这个构建工具就非常流畅了，不然我是理解不好的，每个人都有自己的理解方式，找自己最好的理解方式就好。gradle构建内部运行机制是这样的，首先初始化构建引擎，然后将脚本转换成java代码,然后就是我们最熟悉的构建过程了,将java代码转换成子节码,然后交给虚拟机加载执行

## 如何使用gradle提高工作效率
> 我个人认为构建工具毕竟是一种工具特性,那么就一套完善的高效特性让我去挖掘,我目前挖掘的有利用as的工程特性，结合gradle的强大构建特性，自动化分析文件，自动化打包，模版构建，后面不断有新的挖掘，我相信只要是工具类的东西然后结合我们的技术手段那么肯定会提高我们的工作效率，可能需要手动10分钟的事情，而用gradle处理只要1分钟，甚至更短，错误几率也大大减低，减除人工干预，毕竟现在是人工智能时代，感觉我们会被计算机征服，真可怕，我们唯一能做的就是提升自己。

## gradle工程构建流
> as gradle工程构建流图示

![gradle](https://jackwaylong.github.io/silentor/img/xmind/gradle.png)

![aar](https://jackwaylong.github.io/silentor/img/xmind/aar.png)

## gradle实战
> 构建脚本集

1. [settings.gradle]
2. [root build.gradle]
3. [init.gradle]
4. [utils.gradle]
5. [tasks.gradle]
6. [submodle build.gradle]
7. [common.properties]
8. [template/project.properties]
9. [publish.bat/publish.sh]
10. [properties]

## 总结
> 到此gradle基本构建流已经说完了,这些只是构建的开始,后面我还会继续深入gradle在组件化开发中的作用以及强大支撑，只有明白了gradle的基本工作原理，我们才能更好的去灵活运用gradle来拆分我们的工程，很好的解耦我们的工程，目前比较的多的开发模式有组件化，插件化，我个人理解gradle就是开发模式的驱动者，学好gradle才是根本，才能很好的进行模式开发，gradle网上的指导资料很少，基本都是一些用法，没有分析原理的，对于技术者我强烈建议学习一门技术还是去对应的官网，这样不仅仅能系统的学习，并且还能更为深入的理解语言的本质。

## 建议
> 工程构建一般是跨界的，也就是说可能会涉及到很多种技术的融合，我目前接触到的有python，groovy，bash，bat 等脚本语言，希望大家不要仅仅停留在android业务开发中，技术融合才能让自己强大，多学习不同技术提高自己的维度，深度，广度。


## 后续gradle学习计划
1. 继续深入gradle构建流
2. gradle源码分析
3. 发现gradle中好玩的东西，灵活运用到实际项目中
4. 基于gradle构建项目到产品输出闭环


## 下载
- [下载](https://github.com/jackwaylong/Gradle/archive/master.zip)




















