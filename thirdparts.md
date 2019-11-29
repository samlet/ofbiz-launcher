# thirdparts.md
- https://gitlab.brainfood.com/brainfood/ofbiz-directcontrolservlet
	与ControlServlet一样，这已成为其自身的硬编码 功能，但具有不同的优先级。它有一些东西可以 自动将服务数据作为CSV返回并通过 LibreOffice 生成PDF 。亚当和我都认为重新启动 除了servlet之外的其他东西是个好主意，其中异步调用 在事后并未用螺栓固定，可能是Netty或Vert.x.

⊕ [bibryam/ofbiz-camel: Apache Ofbiz and Apache Camel integration](https://github.com/bibryam/ofbiz-camel)
	该组件允许Camel和OFBiz相互交互。
		它允许Ofbiz服务使用Camel连接器到达200多个外部系统。
		它还允许外部系统使用与OFBiz一起运行的Camel向OFBiz服务发送消息/事件。
	该项目包含一个DemoRoute，演示如何从plugins / ofbiz-camel / data目录轮询文件，并通过执行createNote服务在OFBiz中创建一个注释。它还有一个sendCamelMessage服务，可以从Ofbiz服务向外部系统发送消息。