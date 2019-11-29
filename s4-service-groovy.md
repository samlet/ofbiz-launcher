# s4-service-groovy.md
## Groovy中的服务
为了利用即时编译功能和更少的代码行，您可以使用Groovy DSL实现在OFBiz中构建业务逻辑的服务。 要使用Groovy实现服务，您可以按照以下给定步骤操作：

+ 将新服务定义添加到services / services.xml文件中：

```xml
<service name="createOfbizDemoByGroovyService" default-entity-name="OfbizDemo" engine="groovy"
        location="component://ofbizDemo/script/com/companyname/ofbizdemo/OfbizDemoServices.groovy" invoke="createOfbizDemo" auth="true">
    <description>Create an Ofbiz Demo record using a service in Groovy</description>
    <auto-attributes include="pk" mode="OUT" optional="false"/>
    <auto-attributes include="nonpk" mode="IN" optional="false"/>
    <override name="comments" optional="true"/>
</service>
```

+ 添加新的groovy服务文件 组件：//ofbizDemo/script/com/companyname/ofbizdemo/OfbizDemoServices.groovy
    * 停止服务器并使用“./ gradlew ofbiz”重新启动，这次我们只需要加载新的服务定义，不需要显式编译作为Groovy中的服务实现。
    * 使用webtools实现的测试服务 - >运行服务选项（https：// localhost：8443 / webtools / control / runService）或者只是更新控制器请求调用的服务名称以改为使用此服务并使用添加表单在您之前准备进行测试的应用中。通过这样做，您的Add OfbizDemo表单将调用此groovy服务。
    * 要获得有关在Apache OFBiz中使用Groovy DSL进行服务和事件实现的更多详细信息，您可以在此处参考由OFOP Wiki中的Jacopo Cappellato创建的文档: http://cwiki.apache.org/confluence/x/_M_oAQ

```java
import org.apache.ofbiz.entity.GenericEntityException;
 
def createOfbizDemo() {
    result = [:];
    try {
        ofbizDemo = delegator.makeValue("OfbizDemo");
        // Auto generating next sequence of ofbizDemoId primary key
        ofbizDemo.setNextSeqId();
        // Setting up all non primary key field values from context map
        ofbizDemo.setNonPKFields(context);
        // Creating record in database for OfbizDemo entity for prepared value
        ofbizDemo = delegator.create(ofbizDemo);
        result.ofbizDemoId = ofbizDemo.ofbizDemoId;
        logInfo("==========This is my first Groovy Service implementation in Apache OFBiz. OfbizDemo record "
                  +"created successfully with ofbizDemoId: "+ofbizDemo.getString("ofbizDemoId"));
      } catch (GenericEntityException e) {
          logError(e.getMessage());
          return error("Error in creating record in OfbizDemo entity ........");
      }
      return result;
}
```


