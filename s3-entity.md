# s3-entity.md
+ $ OFBIZ_HOME / plugins / ofbizDemo / entitydef / entitymodel.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
  
<entitymodel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="http://ofbiz.apache.org/dtds/entitymodel.xsd">
  
    <title>Entity of an Open For Business Project Component</title>
    <description>None</description>
    <version>1.0</version>
  
    <entity entity-name="OfbizDemoType" package-name="org.apache.ofbiz.ofbizdemo" title="OfbizDemo Type Entity">
        <field name="ofbizDemoTypeId" type="id"><description>primary sequenced ID</description></field>
        <field name="description" type="description"></field>
        <prim-key field="ofbizDemoTypeId"/>
    </entity>
  
    <entity entity-name="OfbizDemo" package-name="org.apache.ofbiz.ofbizdemo" title="OfbizDemo Entity">
        <field name="ofbizDemoId" type="id"><description>primary sequenced ID</description></field>
        <field name="ofbizDemoTypeId" type="id"></field>
        <field name="firstName" type="name"></field>
        <field name="lastName" type="name"></field>
        <field name="comments" type="comment"></field>
        <prim-key field="ofbizDemoId"/>
        <relation type="one" fk-name="ODEM_OD_TYPE_ID" rel-entity-name="OfbizDemoType">
            <key-map field-name="ofbizDemoTypeId"/>
        </relation>
    </entity>
  
</entitymodel>
```

+ $ OFBIZ_HOME / plugins / ofbizDemo / ofbiz-component.xml文件
    * 已经在其中创建了资源条目，用于在组件加载时将这些实体从其定义加载到数据库。
    * 要检查只需重新启动OFBiz（Ctrl + C后跟“./gradlew ofbiz”）并将浏览器指向实体数据维护工具：  https：// localhost：8443 / webtools / control / entitymaint  并搜索实体OfbizDemoType和OfbizDemo。

```xml
<entity-resource type="model" reader-name="main" loader="main" location="entitydef/entitymodel.xml"/>
```

+ 为实体准备数据
    * 在设置自定义实体后，现在是时候为它准备一些示例数据了。您可以在已在组件的数据目录下设置的数据XML文件中执行此操作，如$ OFBIZ_HOME / plugins / ofbizDemo / data / OfbizDemoTypeData.xml  和$ OFBIZ_HOME / plugins / ofbizDemo / data / OfbizDemoDemoData.xml。

OfbizDemoTypeData.xml

```xml
 <?xml version="1.0" encoding="UTF-8"?>
<entity-engine-xml>
    <OfbizDemoType ofbizDemoTypeId="INTERNAL" description="Internal Demo - Office"/>
    <OfbizDemoType ofbizDemoTypeId="EXTERNAL" description="External Demo - On Site"/>
</entity-engine-xml>
```

OfbizDemoDemoData.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<entity-engine-xml>
    <OfbizDemo ofbizDemoId="SAMPLE_DEMO_1" ofbizDemoTypeId="INTERNAL" firstName="Sample First 1" lastName="Sample Last 1" comments="This is test comment for first record."/>
    <OfbizDemo ofbizDemoId="SAMPLE_DEMO_2" ofbizDemoTypeId="INTERNAL" firstName="Sample First 2" lastName="Sample last 2" comments="This is test comment for second record."/>
    <OfbizDemo ofbizDemoId="SAMPLE_DEMO_3" ofbizDemoTypeId="EXTERNAL" firstName="Sample First 3" lastName="Sample last 3" comments="This is test comment for third record."/>
    <OfbizDemo ofbizDemoId="SAMPLE_DEMO_4" ofbizDemoTypeId="EXTERNAL" firstName="Sample First 4" lastName="Sample last 4" comments="This is test comment for fourth record."/>
</entity-engine-xml>
```

+ $ OFBIZ_HOME / plugins / ofbizDemo / ofbiz-component.xml  文件
    * 已经在其中创建了资源条目，用于加载在这些文件中准备的数据.
    * 此时要将此示例数据加载到已定义的实体/表中，您可以./gradlew loadAll在控制台上运行，也可以直接在webtools中加载实体xml  https：// localhost：8443 / webtools / control / EntityImport。只需将您的xml数据放入“完整XML文档（根标签：entity-engine-xml）：”文本区域并点击“导入文本”
    * 再次完成数据加载过程后，访问实体数据维护（https：// localhost：8443 / webtools / control / entitymaint）并检查您的实体，您将在此处找到刚刚加载的数据。

```xml
<entity-resource type="data" reader-name="seed" loader="main" location="data/OfbizDemoTypeData.xml"/>
<entity-resource type="data" reader-name="demo" loader="main" location="data/OfbizDemoDemoData.xml"/>
```


