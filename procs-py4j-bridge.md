# procs-py4j-bridge.md
## py4j-bridge的实现
+ ofbiz-framework/framework/service/src/main/java/org/apache/ofbiz/service/sagas/SagasBridge.java

+ ofbiz-framework/framework/service/ofbiz-component.xml

```xml
    <!-- sagas bridge -->
    <container name="sagas-bridge" loaders="main,rmi" class="org.apache.ofbiz.service.sagas.SagasBridge">
        <property name="bound-name" value="SagasBridge"/>
        <property name="bound-host" value="0.0.0.0"/>
        <property name="bound-port" value="25333"/>
        <property name="delegator-name" value="default"/>
    </container>
```

+ ofbiz-framework/build.gradle

```java
    // sagas libs
    compile group: 'net.sf.py4j', name: 'py4j', version: '0.10.8.1'
```

+ procs-py4j.ipynb, procs-py4j-ofbiz.ipynb

```python
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM

delegator = gateway.entry_point.getDelegator()
print(delegator)
disp = gateway.entry_point.getDispatcher()
print(disp)
print(delegator.getDelegatorName())

result=delegator.findAll("Person", False)
print(len(result))
```

- run in intellij: procs-intellij.md

## delegator and dispatcher testings
+ ofbiz-framework/framework/common/src/main/java/org/apache/ofbiz/common/test/PerformFindTests.java

