完毕文件76mb，只能上传小于25mb，这是20240527-20190828   爬取完整大概四个小时

感觉被骗了，问他们结果，已读不回，建议不要投这家公司

苏州卓立创智科技有限公司
武汉武昌区阳光大厦（珞狮路）5层
Python工程师笔试题
以下为笔试题，请以邮件形式回复每个题目的答案，一并发送到 hr@zholywise.com

涉及到代码的题目，请提交到自己的git仓库，请将仓库设置为公开状态，然后对应题目的答案填写为对应仓库地址。 

邮件内容中，请务必注意：
A.以下每道笔试题，请按序号写回复，无法回答可写“无”。请务必认真做答，因为我们会对答案做评分，按照评分排序，排名靠前的应聘者才能获得面试机会；
B.请务必在邮件结尾，写上自己简历中的姓名和手机号码，以免我们把你给漏掉了。


题目一：基础题
    技术项：linux，Request，Selenium，Docker，Fastapi，k8s，Langchain,关系型数据库，非关系型数据库
    当我们进行技术使用的选型时，需要你来提供意见，帮助决策。
    对于以上每项技术项，按照自己的理解，分项来简述该技术项的常用场景
    要求：
    描述场景，该场景会用到的命令（方法），使用对应技术解决了什么问题。
    涉及K8s，Langchain的技术应用，为加分项


题目二：爬虫方向
请编写一段可独立运行的程序，访问 https://www.gd.gov.cn/gkmlpt/policy，获取在特定时间区间内的广东省人民政府办公厅的政策数据。

    要求:
        1.收集索引号、发布机构、发布日期、政策标题、政策正文文本、政策正文附件链接，以上六项信息
        2.可以收集特定时间区间内的全部政策信息
    注明：
        可以使用lxml库做页面解析。
        尽量保证程序的健壮性，尽量提高程序的执行效率。
程序输入输出要求：
        输入：日期范围                例：(20220101-20230601)
        输出：指定时间范围内的全部政策信息



题目三：后端方向
请编写一段可独立运行的程序，实现一个post的http请求，入参示例为《题目三素料》的json文件中的数据，基于提供的word文档（模板.docx），填入模板，存入本地文件夹。
要求：
1、与示例结果一致
2、单个文件，尽可能低的时间复杂度
3、考虑并发场景（100）的处理速度
