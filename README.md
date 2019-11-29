# procs.md
⊕ [Home - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Home)
⊕ [OFBiz Features - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Features)

⊕ [The Apache OFBiz® Project - Source Repository](http://ofbiz.apache.org/source-repositories.html)
	⊕ [apache/ofbiz-framework: Mirror of Apache OFBiz Framework](https://github.com/apache/ofbiz-framework)
	⊕ [apache/ofbiz-plugins: Mirror of Apache OFBiz Plugins](https://github.com/apache/ofbiz-plugins)
⊕ [The Apache OFBiz® Project - Developers](http://ofbiz.apache.org/developers.html)
⊕ [apache/ofbiz-framework: Mirror of Apache OFBiz Framework](https://github.com/apache/ofbiz-framework)
⊕ [Apache OFBiz技术生产设置指南 - OFBiz项目开放维基 - Apache软件基金会](https://cwiki.apache.org/confluence/display/OFBIZ/Apache+OFBiz+Technical+Production+Setup+Guide#ApacheOFBizTechnicalProductionSetupGuide-RunningOFBiz)
⊕ [OFBiz Tutorial - A Beginners Development Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+A+Beginners+Development+Guide)
	最终由Mathieu Lirzin修改于四月19,2018
	本教程适用于具有很少或没有OFBiz经验的初学者。它涵盖了OFBiz应用程序开发过程的基础知识。目标是使开发人员熟悉最佳实践，编码约定，基本控制流以及开发人员对OFBiz定制所需的所有其他方面。
	本教程将帮助您在OFBiz中构建您的第一个“演示应用程序”。

## notices
OFBiz分为两个存储库：
	ofbiz-framework：包含核心框架和系统中的主要应用程序，如会计，派对，订单等
	ofbiz-plugins：从“特殊用途”重命名，包含社区正式支持的可选组件

此外，删除了热部署目录，因为plugins目录可以替代“特殊用途”和“热部署”。
如果需要按特定顺序在plugins目录中加载组件，请在plugins目录中放置component-load.xml文件，列出顺序。
要从源代码管理中检出插件，请使用pullPluginSource Gradle任务。要从源代码管理中检出所有插件，请使用pullAllPluginsSource。注意这会删除以前存在的插件目录。

## start
- NOTE: The default user login is "admin" and password "ofbiz". All demo user logins such as DemoCustomer, DemoSupplier, DemoEmployee etc have the default password "ofbiz"

```sh
cd ofbiz-framework/
# OFBiz for the first time as it needs to download all dependencies
# ./gradlew cleanAll loadAll   # cleanAll会删除derby的数据库
./gradlew loadAll
# Start OFBiz
./gradlew ofbiz

# 有许多方法可以运行OFBiz，它们都归结为执行“build / libs / ofbiz.jar”可执行JAR文件的一些变体。
java -jar build/libs/ofbiz.jar

# 要仅运行一个组件的测试运行（对于实体组件）：
gradlew "ofbiz --test component=entity"
# or
java -jar build/libs/ofbiz.jar --test component=entity
```

- Visit OFBiz through your browser:

	https://localhost:8443/ordermgr [Order Back Office]
	https://localhost:8443/accounting [Accounting Back Office]
	https://localhost:8443/webtools [Administrator interface]

	You can log in with the user *admin* and password *ofbiz*.

## build commands
```sh
# OFBiz server commands require "quoting" the commands. For example: gradlew "ofbiz --help"
./gradlew "ofbiz --help"

# Shortcuts to task names can be used by writing the first letter of every word in a task name. However, you cannot use the shortcut form for OFBiz server tasks. Example: gradlew loadAdminUserLogin -PuserLoginId=myadmin = gradlew lAUL -PuserLoginId=myadmin
./gradlew loadAdminUserLogin -PuserLoginId=myadmin
./gradlew lAUL -PuserLoginId=myadmin

# Dependent tasks can be skipped with the -x switch. Example: gradlew build -x test does not run the tests within the build.
./gradlew build -x test
gradlew cleanAll loadAll testIntegration

# Example OFBiz server tasks
gradlew "ofbizDebug --test"
gradlew "ofbizBackground --start --portoffset 10000"
gradlew "ofbiz --shutdown --portoffset 10000"
# gradlew ofbiz (default is --start)
gradlew cleanAll loadAll "ofbiz --start --portoffset 10000"

##  List all available tasks from the build system
./gradlew tasks
## List all available projects in the build system
./gradlew projects

## Shutdown OFBiz
gradlew "ofbiz --shutdown"
## Get OFBiz status
./gradlew "ofbiz --status"

## Force OFBiz shutdown
# Terminate all running OFBiz server instances by calling the appropriate operating system kill command. Use this command to force OFBiz termination if the --shutdown command does not work. Usually this is needed when in the middle of data loading or testing in OFBiz.
# Warning: Be careful in using this command as force termination might lead to inconsistent state / data

./gradlew terminateOfbiz
```

## debug
```sh
# Starts OFBiz in remote debug mode and waits for debugger or IDEs to connect on port 5005
gradlew "ofbizDebug --start"
# OR
gradlew ofbizDebug

## Start OFBiz on a different port
# Start OFBiz of the network port offsetted by the range provided in the argument to --portoffset
gradlew "ofbiz --start --portoffset 10000"
```

## background
```sh
# Start OFBiz in the background by forking it to a new process and redirecting the output to runtime/logs/console.log

gradlew "ofbizBackground --start"
# OR
./gradlew ofbizBackground

# You can also offset the port, for example:
gradlew "ofbizBackground --start --portoffset 10000"
```

## runtime options
```sh
# You can pass JVM runtime options by specifying the project property -PjvmArgs.
gradlew ofbiz -PjvmArgs="-Xms1024M -Xmx2048M" -Dsome.parameter=hello

# If you do not specify jvmArgs, a default of -Xms128M -Xmx1024M is set.
```

## data loading
- https://github.com/apache/ofbiz-framework#data-loading-tasks


