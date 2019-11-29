# procs-plugin.md
⊕ [从Ant到Gradle - 主干版本 - OFBiz项目开放维基 - Apache软件基金会](https://cwiki.apache.org/confluence/display/OFBIZ/From+Ant+to+Gradle+-+trunk+version)
⊕ [OFBiz Tutorial - A Beginners Development Guide - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+A+Beginners+Development+Guide#OFBizTutorial-ABeginnersDevelopmentGuide-Createtheplugin/component)

## start (ok)
+ Create Your First Application (Hello World...)

```sh
$ ./gradlew createPlugin -PpluginId=ofbizDemo
```

- Simply open $OFBIZ_HOME/plugins/ofbizDemo/widget/OfbizDemoScreens.xml file from ofbizDemo plugin (you just created) (直接替换这个文件的全部内容)

```xml
<?xmlversion="1.0"encoding="UTF-8"?>
<screens xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://ofbiz.apache.org/Widget-Screen" xsi:schemaLocation="http://ofbiz.apache.org/Widget-Screen http://ofbiz.apache.org/dtds/widget-screen.xsd">
    <screen name="main">
        <section>
            <actions>
                <set field="headerItem" value="main"/><!-- this highlights the selected menu-item with name "main" -->
            </actions>
            <widgets>
                <decorator-screen name="OfbizDemoCommonDecorator" location="${parameters.mainDecoratorLocation}">
                    <decorator-section name="body">
                        <label text="Hello World!! :)"/>
                    </decorator-section>
                </decorator-screen>
            </widgets>
        </section>
    </screen>
</screens>
```

- Now you will need to restart OFBiz by reloading data($ ./gradlew loadDefault ofbiz). It's required as you have created a new component with some security data for you component (Setup by default in your component data directory as OfbizDemoSecurityGroupDemoData.xml) and as you will restart it, ofbizdemo component will also be loaded.

```sh
# 在目前的trunk中, 需要用loadAll
./gradlew loadAll ofbiz
open https://localhost:8443/ofbizDemo
# Login with user: admin password: ofbiz
# As you login you will see ofbizdemo application up with the hello world message you have put in screen as shown in below given image.
```

## pull plugins
```sh
./gradlew pullPluginSource -PpluginId=ecommerce
./gradlew pullPluginSource -PpluginId=example
./gradlew loadAll
```

## OFBiz插件系统
OFBiz通过插件提供扩展机制。插件是驻留在plugins目录中的标准OFBiz组件。插件可以手动添加，也可以从maven存储库中获取。下面列出了管理插件的标准任务。
注意：OFBiz插件版本遵循语义版本2.0.0 
⊕ [Semantic Versioning 2.0.0 | Semantic Versioning](https://semver.org/)

## 自动拉（下载并安装）插件
下载一个包含所有依赖项（插件）的插件，并从依赖项开始逐个安装它们，然后以插件本身结束。

gradlew pullPlugin -PdependencyId="org.apache.ofbiz.plugin:myplugin:0.1.0"

如果插件驻留在自定义maven存储库（而不是jcenter或localhost）中，则可以使用以下命令指定存储库：

gradlew pullPlugin -PrepoUrl="http://www.example.com/custom-maven" -PdependencyId="org.apache.ofbiz.plugin:myplugin:0.1.0"

如果您需要用户名和密码来访问自定义存储库：

gradlew pullPlugin -PrepoUrl="http://www.example.com/custom-maven" -PrepoUser=myuser -PrepoPassword=mypassword -PdependencyId="org.apache.ofbiz.plugin:myplugin:0.1.0"

## 从源代码管理中提取官方插件 (ok)
从源代码管理（当前是subversion）下载官方插件并将其放在plugins目录中。此外，如果为正在下载的插件定义了此任务，则还会执行“安装”任务。

这个任务在处理trunk分支时非常有用，因为它引入了最新版本的插件。

./gradlew pullPluginSource -PpluginId=ecommerce

注意：此插件将在插件目录中放置自己的.svn目录。

## 从源代码管理中提取所有官方插件
从源代码控制（当前是subversion）下载所有官方支持的插件，并将它们包含在/ plugins中的“.svn”目录中。警告！此任务删除/ plugins目录并将其替换为官方插件。

gradlew pullAllPluginsSource

此任务可以轻松下载和开发官方支持的插件。它主要由在主干分支上工作的开发人员或个人使用。我们不建议在OFBiz版本上使用此任务，而是考虑使用“pullPlugin”任务来获取与您的版本兼容的正确版本的插件。

注意：所有插件将共享插件目录中的.svn目录。

## 安装插件
如果您有一个名为mycustomplugin的插件并想在OFBiz中安装它，请按照以下说明操作：

如果插件被压缩，则解压缩插件
将解压缩的目录放入/ plugins
运行以下命令
./gradlew installPlugin -PpluginId=myplugin

上述命令在插件的build.gradle文件中执行任务“install”（如果存在）

## 卸载插件
如果您有一个名为mycustomplugin的现有插件，并且您希望卸载，请运行以下命令

./gradlew uninstallPlugin -PpluginId=myplugin

上面的命令在插件的build.gradle文件中执行任务“uninstall”（如果存在）

## 删除插件 (ok)
在现有插件上调用uninstallPlugin，然后从文件系统中删除它

./gradlew removePlugin -PpluginId=myplugin

## 创建一个新插件
创建一个新插件。传递以下项目参数：

	pluginId：必填
	pluginResourceName：optional，default是pluginId的Capitalized值
	webappName：可选，默认值是pluginId的值
	basePermission：optional，默认是pluginId的UPPERCASE值

```sh
./gradlew createPlugin -PpluginId=myplugin

./gradlew createPlugin -PpluginId=myplugin -PpluginResourceName=MyPlugin -PwebappName=mypluginweb -PbasePermission=MYSECURITY
```
上面的命令在/ plugins / myplugin中创建了一个新插件

## 将插件推送到存储库
此任务将OFBiz插件发布到maven包中，然后将其上载到maven存储库。目前，推送仅限于localhost maven存储库（正在进行中）。要推送插件，请传递以下参数：

	pluginId：必填
	groupId：可选，默认为org.apache.ofbiz.plugin
	pluginVersion：可选，默认为0.1.0-SNAPSHOT
	pluginDescription：可选，默认为“OFBiz插件$ {pluginId}的发布”

```sh
gradlew pushPlugin -PpluginId=myplugin

gradlew pushPlugin -PpluginId=mycompany -PpluginGroup=com.mycompany.ofbiz.plugin -PpluginVersion=1.2.3 -PpluginDescription="Introduce special functionality X"
```




