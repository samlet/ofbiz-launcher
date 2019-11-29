# s8-event.md
Apache OFBiz中的事件只是用于处理HttpServletRequest和HttpServletResponse对象的方法。您不需要像使用服务那样提供这些的定义。这些是从控制器直接调用的。如果要将自定义服务器端验证添加到输入参数，事件也很有用。对于执行数据库操作，您仍然可以从事件中调用预构建的服务。

+ OfbizDemoEvents.java
    * 添加一个新的事件目录到package和一个新的Events类文件

```java
package com.companyname.ofbizdemo.events;
  
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
  
import org.apache.ofbiz.base.util.Debug;
import org.apache.ofbiz.base.util.UtilMisc;
import org.apache.ofbiz.base.util.UtilValidate;
import org.apache.ofbiz.entity.Delegator;
import org.apache.ofbiz.entity.GenericValue;
import org.apache.ofbiz.service.GenericServiceException;
import org.apache.ofbiz.service.LocalDispatcher;
  
public class OfbizDemoEvents {
  
 public static final String module = OfbizDemoEvents.class.getName();
  
    public static String createOfbizDemoEvent(HttpServletRequest request, HttpServletResponse response) {
        Delegator delegator = (Delegator) request.getAttribute("delegator");
        LocalDispatcher dispatcher = (LocalDispatcher) request.getAttribute("dispatcher");
        GenericValue userLogin = (GenericValue) request.getSession().getAttribute("userLogin");
  
        String ofbizDemoTypeId = request.getParameter("ofbizDemoTypeId");
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
  
        if (UtilValidate.isEmpty(firstName) || UtilValidate.isEmpty(lastName)) {
            String errMsg = "First Name and Last Name are required fields on the form and can't be empty.";
            request.setAttribute("_ERROR_MESSAGE_", errMsg);
            return "error";
        }
        String comments = request.getParameter("comments");
  
        try {
            Debug.logInfo("=======Creating OfbizDemo record in event using service createOfbizDemoByGroovyService=========", module);
            dispatcher.runSync("createOfbizDemoByGroovyService", UtilMisc.toMap("ofbizDemoTypeId", ofbizDemoTypeId,
                    "firstName", firstName, "lastName", lastName, "comments", comments, "userLogin", userLogin));
        } catch (GenericServiceException e) {
            String errMsg = "Unable to create new records in OfbizDemo entity: " + e.toString();
            request.setAttribute("_ERROR_MESSAGE_", errMsg);
            return "error";
        }
        request.setAttribute("_EVENT_MESSAGE_", "OFBiz Demo created succesfully.");
        return "success";
    }
}
```

+ controller.xml
    * 通过重建来停止和启动服务器，因为我们需要编译我们在＃1中添加的Java事件类。
    * 现在要测试事件，您只需将AddOfbizDemo表单目标更改为“createOfbizDemoEvent”，并且现在提交它将调用您的事件。

```xml
<request-map uri="createOfbizDemoEvent">
    <security https="true" auth="true"/>
    <event type="java" path="com.companyname.ofbizdemo.events.OfbizDemoEvents" invoke="createOfbizDemoEvent"/>
    <response name="success" type="view" value="main"/>
    <response name="error" type="view" value="main"/>
</request-map>
```



