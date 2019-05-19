# Redis数据库地址
REDIS_HOST = '192.168.43.68'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 're123456'

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
# Key  为Redis数据库的表名
# Value为生成cookies的类名。用于调度器动态实例化对象
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
# Key  为Redis数据库的表名
# Value为验证cookies的类名。用于调度器动态实例化对象
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 检测器检测接口
# test_url = TEST_URL_MAP[self.website]
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
# 分布式爬虫时使用可公网访问的服务器ip
API_HOST = '192.168.43.212'
# API_HOST = '127.0.0.1'
API_PORT = 5000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = False
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
