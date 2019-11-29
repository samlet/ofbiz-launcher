# procs-event.md
## 使用groovy event handler
```xml
    <request-map uri="checkAction">
        <security https="true" auth="true"/>
        <event type="groovy" path="component://product/groovyScripts/catalog/imagemanagement/CheckAction.groovy"/>
        <response name="frame" type="request" value="ImageFrames"/>
        <response name="crop" type="request" value="ImageCropping"/>
        <response name="rotate" type="request" value="ImageRotating"/>
        <response name="noAction" type="request-redirect" value="ListImageManage"/>
    </request-map>
```
```xml
    <request-map uri="graphqlScriptEvent">
        <security https="true" auth="true"/>
        <event type="groovy" path="component://ofbizDemo/webapp/ofbizDemo/WEB-INF/events/GraphQLHandler.groovy"/>
        <response name="error" type="none"/>
        <response name="success" type="none"/>
    </request-map>
```

    

