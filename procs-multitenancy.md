# procs-multitenancy.md
⊕ [多租户支持 - OFBiz项目开放维基 - 阿帕奇软件基金会](https://cwiki.apache.org/confluence/display/OFBIZ/Multitenancy+support)
⊕ [从Ant到Gradle - 主干版本 - OFBiz项目开放维基 - Apache软件基金会](https://cwiki.apache.org/confluence/display/OFBIZ/From+Ant+to+Gradle+-+trunk+version)

## 创造一个新的租户
在您的环境中创建新租户，创建委托人，使用admin-user和password加载初始数据（一般需要multitenant = Y.properties）。传递以下项目参数：

	tenantId：强制性的
	tenantName：可选，默认值为tenantId
	domainName：可选，默认为org.apache.ofbiz
	tenantReaders：可选，默认值是seed，seed-initial，demo
	dbPlatform：可选，D（Derby），M（MySQL），O（Oracle），P（PostgreSQL）（默认D）
	dbIp：数据库的可选，ip地址
	dbUser：数据库的可选用户名
	dbPassword：可选，数据库的密码

```sh
gradlew createTenant -PtenantId=mytenant

gradlew createTenant -PtenantId=mytenant -PtenantName="My Name" -PdomainName=com.example -PtenantReaders=seed,seed-initial,ext -PdbPlatform=M -PdbIp=127.0.0.1 -PdbUser=mydbuser -PdbPassword=mydbpass
```
如果成功运行，系统将创建一个新租户：

	委托人：默认＃$ {tenandId}（例如默认#mytenant）
	admin用户：$ {tenantId} -admin（例如mytenant-admin）
	管理员用户密码：ofbiz

## 加载特定租户的数据
在多租户环境中加载一个特定租户的数据。请注意，您必须在general.properties中设置multitenant = Y，并传递以下项目参数：

	tenantId（强制性）
	tenantReaders（可选）
	tenantComponent（可选）

```sh	
gradlew loadTenant -PtenantId=mytenant

gradlew loadTenant -PtenantId=mytenant -PtenantReaders=seed,seed-initial,demo -PtenantComponent=base
```

## 介绍
OF租赁已在转927271引入多租户。多租户是指从OFBiz的单一副本运行单独的数据实例（租户）的能力。每个数据实例都保存在一个单独的数据库中。用户通过在登录表单中指定租户ID来登录数据实例（或租户）。请注意，仍然使用默认数据库。

如果您只想将OFBiz与一个数据库一起使用（即您不想使用多租户），那么您之前所做的事情就无法改变。

多租户的优势在于租户不需要使用“ant run-install ...”或命令行上的任何其他内容来访问加载数据。您可能有数百人在其他租户实例中处于活动状态，因此您不希望停止并启动服务器执行此类操作，并希望您可以避免管理员与租户一起工作以获取自定义数据。您希望事物是自助服务的，这是使数据库驱动的重点（使用UI，以便用户可以将内容输入数据库的相关部分）。

## 租户数据库
数据源（=数据库引用）在TenantDataSouces实体中定义，而不是在entityengine.xml中（参见下面的描述）。

当然，如果您使用的DBMS不支持使用带有Derby的OOTB的“; create = true”语法（例如Postgres，MySql等），则需要先创建租户数据库和凭据。运行租户数据安装。
.....
