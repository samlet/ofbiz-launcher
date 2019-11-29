# s9-ui.md
+ https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+A+Beginners+Development+Guide#OFBizTutorial-ABeginnersDevelopmentGuide-CustomizingUserInterface
    * 使用FreeMarker模板和Groovy脚本: 好的，所以我们在OFBiz教程的最后部分。在这一部分中，我们将专注于为业务管理应用程序（即后端应用程序和esp）定制Apache OFBiz的UI层。大多数时候你会发现OFBiz Widgets就足够了。但有时重要的是开发应用程序，因为用户确实需要它。
    * 因此，要首先自定义应用程序的UI部分以使其变得简单，我们将使用Freemarker模板而不是内置的Form Widgets。首先，我们将看到如何在Apache OFBiz中使用Freemarker和Groovy脚本，然后我们将看到如何通过定义自己的装饰器来对其进行自定义样式。最初我们将使用OFBiz默认装饰器。


+ https://cwiki.apache.org/confluence/display/OFBIZ/OFBiz+Tutorial+-+A+Beginners+Development+Guide#OFBizTutorial-ABeginnersDevelopmentGuide-CreatingCustomDecorator
    * 创建自定义装饰器: 在Freemarker中使用您的UI可让您自由地进行实验，进行CSS调整并按照用户需要的方式制作应用程序。在本节中，我们将看到我们如何做到这一点。

    * 我们将通过为您的应用程序视图定义自定义装饰器来实现它。OFBiz中的装饰器只是一个屏幕，您可以通过将其包含在其他应用程序屏幕中来定义和重用。您已经使用OFBiz附带的默认装饰器（main-decorator - > ApplicationDecorator）来完成它。只要观察你到目前为止准备好的屏幕，你会发现，你使用的是这个主装饰器，请参考下面的OfbizDemoScreens.xml行。

    