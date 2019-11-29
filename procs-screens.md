# procs-screens.md
+ https://localhost:8443/ofbizDemo/control/main
+ 使用xml渲染: view-source:https://localhost:8443/ofbizDemo/control/AddOfbizDemoXml
	+ request-map uri="AddOfbizDemoXml"
		+ view-map name="AddOfbizDemoXml" type="screenxml"
	+ screen name="AddOfbizDemoXml"
		+ screen name="XmlGlobalDecorator"
		+ includes/HtmlHeaderForAjax.ftl
		+ includes/HtmlFooterForAjax.ftl

		+ actions/crud/ListOfbizDemo.groovy
		+ crud/ListOfbizDemo.ftl
	+ ./visit/demo.py
	+ ./ofbiz-framework/task-rest.sh

