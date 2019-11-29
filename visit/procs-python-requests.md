# procs-python-requests.md
⊕ [高级用法 — Requests 2.18.1 文档](http://docs.python-requests.org/zh_CN/latest/user/advanced.html)

## start (with 'using bigdata')
```python
>>> requests.get('https://requestb.in')
>>> requests.get('https://github.com', verify=True)

requests.get('https://kennethreitz.org', verify=False)
requests.get('https://localhost:8443/webtools/control/ping', verify=False)
# 
r=requests.get('https://localhost:8443/workeffort/control/main/ajaxCheckLogin?USERNAME=admin&PASSWORD=ofbiz', verify=False)
print(r.cookies)
r.get('https://localhost:8443/workeffort/control/FindWorkEffort', verify=False)

r=requests.get('https://localhost:8443/humanres', verify=False)
if (r.status_code == requests.codes.ok):
	print(r.headers['content-type'])

r=requests.get('https://localhost:8443/webtools/control/login', verify=False)
```

## graphql
⊕ [使用Spring Boot构建GraphQL服务器| Pluralsight](https://www.pluralsight.com/guides/building-a-graphql-server-with-spring-boot)

- 可以通过HTTP POST作为JSON以这种方式发送：
{
	"query":"{findAllBooks { id title } }"
}

- 还可以发送编码的GET请求URL，因此查询如下：
http://localhost:8080/graphql?query={findAllBooks{id title}}
它必须像以下一样发送：
http://localhost:8080/graphql?query=%7BfindAllBooks%7Bid%20title%7D%7D

⊕ [URL encoding the space character: + or %20? - Stack Overflow](https://stackoverflow.com/questions/1634271/url-encoding-the-space-character-or-20)

	Here is a sample string in URL where the HTML specification allows encoding spaces as pluses: "http://example.com/over/there?name=foo+bar". So, only after "?", spaces can be replaced by pluses, according to the HTML specification. In other cases, spaces should be encoded to %20. But since it's hard to correctly determine the context, it's the best practice to never encode spaces as "+".

◐ graphql的查询输入是通过query参数, 输出的格式是xml+json的复合文档, 外层是xml元素, graphql的结果包含在cdata段
	⊕ [XML CDATA](http://www.w3school.com.cn/xml/xml_cdata.asp)

```xml
<grqphql>
<![CDATA[
function matchwo(a,b)
{
if (a < b && a < 0) then
  {
  return 1;
  }
else
  {
  return 0;
  }
}
]]>
</grqphql>
```

- 无response的request-map参考

```xml
    <request-map uri="xmlrpc" track-serverhit="false" track-visit="false">
        <security https="false"/>
        <event type="xmlrpc"/>
        <response name="error" type="none"/>
        <response name="success" type="none"/>
    </request-map>
```

