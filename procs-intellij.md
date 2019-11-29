# procs-intellij.md
⊕ [Running and Debugging OFBiz in Intellij IDEA - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Running+and+Debugging+OFBiz+in+Intellij+IDEA)

## Running and Debugging OFBiz in Intellij IDEA
Navigate to Run -> Edit Configurations…
Click + to add new configuration, and choose Gradle.
Fill in the following fields:
	Name: My OFBiz
	Gradle project: <path to build.gradle>
	Tasks: ofbiz
Click OK.
Navigate to Run -> Debug…, choose My OFBiz.
Click Stop ‘My OFBiz’ when done with debugging.

- 在Gradle project栏选取最上层的ofbiz, 将会显示为ofbiz-framework; 在tasks栏输入ofbiz
- 再创建一个新的Gradle configuration, 用顶层ofbiz, tasks栏使用terminateOfbiz

