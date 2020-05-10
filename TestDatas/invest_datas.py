# -*- coding:utf-8 -*-
# @author:Fillico
# @date:2019/6/26 14:47

invest_success_data = {"invest_money": 100}

# 1）投资为10，提示投资为100的倍数
# 2）投资12，提示要为10的整数倍，按钮不可点击
# 3）投资为非数字， 提示 要为1-的整数倍
# 4）投资为0/负数/含空格/小数   提示

invest_fail_data = [{"invest_money": 10, "check": "投标金额必须为100的倍数"},
                    {"invest_money": 0, "check": "请正确填写投标金额"},
                    {"invest_money": -500, "check": "请正确填写投标金额"},
                    ]

invest_wrong_formater = [{"invest_money": "100@", "check": "请输入10的整数倍"},
                        {"invest_money": 123, "check": "请输入10的整数倍"},
                         {"invest_money": "一百元", "check": "请输入10的整数倍"},
                         {"invest_money": "10 0", "check": "请输入10的整数倍"},
                         {"invest_money": -1, "check": "请输入10的整数倍"}
                         ]


