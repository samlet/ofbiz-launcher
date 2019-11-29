# procs-minilang.md
⊕ [Mini Language - minilang - simple-method - Reference - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/Mini+Language+-+minilang+-+simple-method+-+Reference)

⊕ [[OFBIZ-9381]将RateServices.xml mini-lang转换为groovyDSL - ASF JIRA](https://issues.apache.org/jira/browse/OFBIZ-9381)
    为了弃用迷你版的OFBIZ-9350，我尝试将一些迷你服务转换为groovy脚本。
    我转换了updateRateAmount，deleteRateAmount，updatePartyRate和deleteRateAmount。
    对于使元素到期而不是删除if的服务，删除不是一个好的定义。所以我建议使用补丁将deleteRateAmount和deletePartyRate移动到expireRateAmount和expirePartyRate。
⊕ [[OFBIZ-9350]弃用Mini Lang - ASF JIRA](https://issues.apache.org/jira/browse/OFBIZ-9350)
    根据[1]中的提案主题，我们决定弃用迷你语言。

    此问题跟踪前述线程中提出的后续步骤，即：
    1.为迁移过程的文档和描述创建一个Wiki页面，以及如何替换mini lang。
    2.在Wiki中突出显示minilang将被弃用，例如[2]
    3.将弃用标记放在相应的代码中
    4.请用贡献者用迷你语言写的开放补丁来用Java代码替换它们[3]
    5.开始主动用适当的Java代码替换现有的迷你代码。这需要更多的计划和讨论，我们将用Java代码替换哪些部分，哪些部分最好由某种DSL替代。一个好的起点可以是[4] [5] [6]。

    [1] https://lists.apache.org/thread.html/253b41060a295b8ab68bc78763cc129fc74b712cf776f8716022097f@%3Cdev.ofbiz.apache.org%3E
    [2] https://cwiki.apache.org/confluence/display/OFBADMIN/Mini+语言+ - + minilang + - +简单方法+ - +参考文献
    [3]有没有人知道批量评论Jira问题的方法，就像在Redmine中可能的那样？
    [4] https://cwiki.apache.org/confluence/display/OFBIZ/Groovy+DSL+for+OFBiz+business+logic 
    [5] https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz +教程+ - + A +初学者+开发+指南
    [6] https://cwiki.apache.org/confluence/display/OFBADMIN/Coding+Conventions    

⊕ [OFBiz Tutorial - From Mini Language to Groovy - OFBiz Project Open Wiki - Apache Software Foundation](https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+From+Mini+Language+to+Groovy)
    
⊕ [[PROPOSAL]弃用迷你语言 - Apache Mail Archives](https://lists.apache.org/thread.html/253b41060a295b8ab68bc78763cc129fc74b712cf776f8716022097f@%3Cdev.ofbiz.apache.org%3E)
    在迷你lang中，我看到我们项目的另一部分需要一个重构/更改。以下是一些原因：
    - 在重构方面，XML编程很难处理。
    - “代码”无法调试，难以查看和维护。
    - 由于解析和处理XML的开销，它速度较慢
    - 它非常冗长，甚至比Java还要多！
    - 很难推理，因为一切都显示为字符串 （变量，地图，对象等......）这使得它变得非常困难
    知道什么东西被宣布或修改
    - 它非常容易出错并且很脆弱（再次由于字符串声明）
    - 它不是一种完整的编程语言（与groovy或其他任何语言不同） 
    支持DSL的语言）。因此，它有许多限制力量
    开发人员要编写更多代码行来实现相同的结果。
    - 代码不可重用（限制DSL）
    - 代码不可组合（DSL的限制）
    - Minilang依赖于很多Java构造（实现，而不是 接口）需要重构，对其进行任何改进核心API更具挑战性
    - Minilang使用不一致（小部件，服务中的DSL不同） 
    和实体）。因此，我们需要保留一个最小的DSL来声明
    事情只有。
    我们已经有了基于Java的服务和事件实现有想法实现Groovy DSL，可以轻松使用（或
    更容易）作为迷你郎并没有上述缺陷。


