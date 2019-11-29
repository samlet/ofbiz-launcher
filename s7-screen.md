# s7-screen.md
+ OfbizDemoScreens.xml
    * 将表单位置添加到主屏幕

```xml
 <?xml version="1.0" encoding="UTF-8"?>
<screens xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="http://ofbiz.apache.org/dtds/widget-screen.xsd">
  
    <screen name="main">
        <section>
            <actions>
                <set field="headerItem" value="main"/> <!-- this highlights the selected menu-item with name "main" -->
            </actions>
            <widgets>
                <decorator-screen name="main-decorator" location="${parameters.mainDecoratorLocation}">
                    <decorator-section name="body">
                        <screenlet title="Add Ofbiz Demo">
                            <include-form name="AddOfbizDemo" location="component://ofbizDemo/widget/OfbizDemoForms.xml"/>
                        </screenlet>
                    </decorator-section>
                </decorator-screen>
            </widgets>
        </section>
    </screen>
</screens>
```

+ $ OFBIZ_HOME / plugins / ofbizDemo / webapp / ofbizDemo / WEB-INF / controller.xml 
    * 在您转到表单并开始从添加表单创建OfbizDemo记录之前，您需要在$ OFBIZ_HOME / plugins / ofbizDemo / webapp / ofbizDemo / WEB-INF / controller.xml  文件中为目标服务创建一个条目，  该服务将在表格已提交。你可以在你的ofbizdemo apps控制器文件中的Request Mappings下面显示如下所示
    * 看看我们最近创建的表单  https：// localhost：8443 / ofbizDemo

```xml
<request-map uri="createOfbizDemo">
    <security https="true" auth="true"/>
    <event type="service" invoke="createOfbizDemo"/>
    <response name="success" type="view" value="main"/>
</request-map>
```

+ 在OfbizDemoScreens.xml中定义的FindOfbizDemo屏幕

```xml
 <!-- Find and list all ofbizdemos in a tabular format -->
<screen name="FindOfbizDemo">
    <section>
        <actions>
            <set field="headerItem" value="findOfbizDemo"/>
            <set field="titleProperty" value="PageTitleFindOfbizDemo"/>
            <set field="ofbizDemoCtx" from-field="parameters"/>
        </actions>
        <widgets>
            <decorator-screen name="main-decorator" location="${parameters.mainDecoratorLocation}">
                <decorator-section name="body">
                    <section>
                        <condition>
                            <if-has-permission permission="OFBIZDEMO" action="_VIEW"/>
                        </condition>
                        <widgets>
                            <decorator-screen name="FindScreenDecorator" location="component://common/widget/CommonScreens.xml">
                                <decorator-section name="search-options">
                                    <include-form name="FindOfbizDemo" location="component://ofbizDemo/widget/OfbizDemoForms.xml"/>
                                </decorator-section>
                                <decorator-section name="search-results">
                                    <include-form name="ListOfbizDemo" location="component://ofbizDemo/widget/OfbizDemoForms.xml"/>
                                </decorator-section>
                            </decorator-screen>
                        </widgets>
                        <fail-widgets>
                            <label style="h3">${uiLabelMap.OfbizDemoViewPermissionError}</label>
                       </fail-widgets>
                    </section>
                </decorator-section>
            </decorator-screen>
        </widgets>
    </section>
</screen>
```

+ 添加请求映射以访问controller.xml中的这个新的Find Ofbiz Demo页面

```xml
<!-- Request Mapping -->
<request-map uri="FindOfbizDemo"><security https="true" auth="true"/><response name="success" type="view" value="FindOfbizDemo"/></request-map>
   
<!-- View Mapping -->
<view-map name="FindOfbizDemo" type="screen" page="component://ofbizDemo/widget/OfbizDemoScreens.xml#FindOfbizDemo"/>
```

+ OfbizDemoMenus.xml
    * 添加一个新菜单来显示查找选项。 在OFBiz中创建菜单非常简单，所有菜单都定义为* menus.xml。 当我们从gradle创建一个组件时，我们得到一个名为OfbizDemoMenus.xml的文件, 在OfbizDemoMenus.xml文件中生成以下条目。
    * 只需重新启动服务器，在isbizdemo应用程序（https：// localhost：8443 / ofbizDemo / control / main）下，您将看到“查找”菜单选项。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<menus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://ofbiz.apache.org/dtds/widget-menu.xsd">
    <menu name="MainAppBar" title="${uiLabelMap.OfbizDemoApplication}" extends="CommonAppBarMenu" extends-resource="component://common/widget/CommonMenus.xml">
        <menu-item name="main" title="${uiLabelMap.CommonMain}"><link target="main"/></menu-item>
        <menu-item name="findOfbizDemo" title="${uiLabelMap.OfbizDemoFind}"><link target="FindOfbizDemo"/></menu-item>
    </menu>
</menus>
```

