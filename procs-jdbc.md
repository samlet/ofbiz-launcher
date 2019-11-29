# procs-jdbc.md
⊕ [从Ant到Gradle - 主干版本 - OFBiz项目开放维基 - Apache软件基金会](https://cwiki.apache.org/confluence/display/OFBIZ/From+Ant+to+Gradle+-+trunk+version)
⊕ [Apache OFBiz Technical Production Setup Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Apache+OFBiz+Technical+Production+Setup+Guide)
⊕ [Setup OFBiz version 16.11.02 with PostgreSQL on Windows - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Setup+OFBiz+version+16.11.02+with+PostgreSQL+on+Windows)

## 设置MySQL，PostgreSQL等外部数据库
⊕ [Maven Repository: mysql » mysql-connector-java » 5.1.47](https://mvnrepository.com/artifact/mysql/mysql-connector-java/5.1.47)
    
```java
// https://mvnrepository.com/artifact/mysql/mysql-connector-java
compile group: 'mysql', name: 'mysql-connector-java', version: '5.1.47'
```

要设置外部数据库而不是默认的嵌入式Apache Derby，您需要按照以下说明操作：

使用以下选项之一查找适合您的数据库的JDBC驱动程序：
在jcenter中搜索JDBC驱动程序并将其放在build.gradle依赖项中，例如runtime 'mysql:mysql-connector-java:5.1.36'
要么下载JDBC驱动程序jar并将其放在$ OFBIZ_HOME / lib或任何组件的lib子目录中

修改位于$ OFBIZ_HOME / framework / entity / config中的entityengine.xml文件，将默认数据库切换为您选择的数据库。有关详细信息，请阅读技术设置指南中的相关章节

