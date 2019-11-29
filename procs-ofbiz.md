# ofbiz.md
⊕ [OFBiz Tutorial - A Beginners Development Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+A+Beginners+Development+Guide#OFBizTutorial-ABeginnersDevelopmentGuide-CreateaFindForm)
    修改于 一月 21, 2019
    This tutorial is for trunk release. 
    
⊕ [The Apache OFBiz® Project - Source Repository](http://ofbiz.apache.org/source-repositories.html)
	⊕ [apache/ofbiz-framework: Mirror of Apache OFBiz Framework](https://github.com/apache/ofbiz-framework)
	⊕ [apache/ofbiz-plugins: Mirror of Apache OFBiz Plugins](https://github.com/apache/ofbiz-plugins)
⊕ [The Apache OFBiz® Project - Developers](http://ofbiz.apache.org/developers.html)

⊕ [Best Practices Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Best+Practices+Guide)

## start
```sh
./gradlew build
# load data
java -jar build/libs/ofbiz.jar --load-data
# start server
java -jar build/libs/ofbiz.jar
```

## projects
⊕ [快速查看Gradle项目包依赖情况 - sugaryaruan的博客 - CSDN博客](https://blog.csdn.net/sugaryaruan/article/details/79905339)

```sh
# 得到依赖组件树
$ ./gradlew dependencies
```
