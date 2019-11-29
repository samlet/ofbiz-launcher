# s4-service.md
+ $ OFBIZ_HOME/plugins/ofbizDemo/servicedef/services.xml
    * 编写一个服务, 来在服务定义xml文件中的OfbizDemo实体的数据库中创建记录
    * 服务“createOfbizDemo”使用engine =“entity-auto”，因此您不需要提供其实现，OFBiz负责创建操作。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<services xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="http://ofbiz.apache.org/dtds/services.xsd">
  
    <description>OfbizDemo Services</description>
    <vendor></vendor>
    <version>1.0</version>
  
    <service name="createOfbizDemo" default-entity-name="OfbizDemo" engine="entity-auto" invoke="create" auth="true">
        <description>Create an Ofbiz Demo record</description>
        <auto-attributes include="pk" mode="OUT" optional="false"/>
        <auto-attributes include="nonpk" mode="IN" optional="false"/>
        <override name="comments" optional="true"/>
    </service>
  
</services>
```

+ $ OFBIZ_HOME/plugins/ofbizDemo/ofbiz-component.xml文件
    * 您已经在其中创建了资源条目，用于加载此文件中定义的服务
    * 要加载此服务定义，您需要重新启动OFBiz。要测试此服务，请直接转到webtools - >运行服务选项： https：// localhost：8443/webtools/control/runService
    * 通过Web Tools运行服务：这是一个由框架提供的智能实用程序，用于运行您的服务。 提交上述表格后，您将提交一份表格，输入服务的IN参数。

```xml
<!-- service resources: model(s), eca(s) and group definitions -->
<service-resource type="model" loader="main" location="servicedef/services.xml"/>
```

+ Java服务: $ OFBIZ_HOME/plugins/ofbizDemo/servicedef/services.xml
    * 当您需要处理涉及构建数据库和自定义逻辑的多个实体的服务中的复杂操作时，您需要为您的服务提供自定义实现
    * 我们这次使用的是engine =“java”。

```xml
<service name="createOfbizDemoByJavaService" default-entity-name="OfbizDemo" engine="java"
        location="com.companyname.ofbizdemo.services.OfbizDemoServices" invoke="createOfbizDemo" auth="true">
    <description>Create an Ofbiz Demo record using a service in Java</description>
    <auto-attributes include="pk" mode="OUT" optional="false"/>
    <auto-attributes include="nonpk" mode="IN" optional="false"/>
    <override name="comments" optional="true"/>
</service>
```

+ src/main/java/com/companyname/ofbizdemo/services/OfbizDemoServices.java
    * 停止服务器并使用“./gradlew ofbiz”重新启动，它将编译您的类，并且当ofbiz重新启动更新的jar文件时将使其可用。
    * 使用webtools实现的测试服务 - >运行服务选项（https：// localhost：8443 / webtools / control / runService）或者只是更新控制器请求调用的服务名称以改为使用此服务并使用添加表单在您之前准备的应用中。通过这样做，您的Add OfbizDemo表单将调用此java服务。

```java
package com.companyname.ofbizdemo.services;
import java.util.Map;
  
import org.apache.ofbiz.base.util.Debug;
import org.apache.ofbiz.entity.Delegator;
import org.apache.ofbiz.entity.GenericEntityException;
import org.apache.ofbiz.entity.GenericValue;
import org.apache.ofbiz.service.DispatchContext;
import org.apache.ofbiz.service.ServiceUtil;
  
public class OfbizDemoServices {
  
    public static final String module = OfbizDemoServices.class.getName();
  
    public static Map<String, Object> createOfbizDemo(DispatchContext dctx, Map<String, ? extends Object> context) {
        Map<String, Object> result = ServiceUtil.returnSuccess();
        Delegator delegator = dctx.getDelegator();
        try {
            GenericValue ofbizDemo = delegator.makeValue("OfbizDemo");
            // Auto generating next sequence of ofbizDemoId primary key
            ofbizDemo.setNextSeqId();
            // Setting up all non primary key field values from context map
            ofbizDemo.setNonPKFields(context);
            // Creating record in database for OfbizDemo entity for prepared value
            ofbizDemo = delegator.create(ofbizDemo);
            result.put("ofbizDemoId", ofbizDemo.getString("ofbizDemoId"));
            Debug.log("==========This is my first Java Service implementation in Apache OFBiz. OfbizDemo record created successfully with ofbizDemoId:"+ofbizDemo.getString("ofbizDemoId"));
        } catch (GenericEntityException e) {
            Debug.logError(e, module);
            return ServiceUtil.returnError("Error in creating record in OfbizDemo entity ........" +module);
        }
        return result;
    }
}
```


