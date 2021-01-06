# autobus
班车自动预约脚本
## 接口
### request headers
POST /dataForward HTTP/1.1
Host: 159.226.95.123
Connection: keep-alive
Content-Length: 87
DNT: 1
User-Agent: 
Content-Type: application/json
Accept: */*
Origin: http://bcyy.iie.ac.cn
Referer: http://bcyy.iie.ac.cn/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
X-Token: ****************
### 登录
Req: {"idserial":"你的用户名","password":"你的密码","method":"/mobile/login/userLoginCheck"}
Res: {"code":200,"data":{"token":"你的Tocken"},"msg":null}
    {"code":500,"data":null,"msg":"账号或密码输入错误，请重新输入"}
### 退出登录
Req: {"method":"/mobile/login/mobileLogout"}
Res: {"code":200,"data":null,"msg":"退出成功"}
### 查询开放预约时间
Req: {"method":"/mobile/home/queryGoodsAuxDate"}
Res: {"code":200,"data":{"selldatemin":"2020-11-21","selldatemax":"2020-11-23"},"msg":null}
### 查询某天（selldate）班车
Req: {selldate: "2020-11-21", enddate: "2020-11-23", method: "/mobile/home/queryHomeGoods"}
Res: {"code":200,"data":[{"goodspriceFen":"0","goodsdetail":"益园-总部基地","goodsprice":"0.00","alightposition":"总部基地","boardposition":"益园（其中17:00京香发车1辆）","terminus":"总部基地","selldate":"2020-11-21","endtime":"18:00","goodsname":"17:15益园-总部基地（周六）","id":24,"starttime":"17:15"},...],"msg":null}
    {"code":201,"data":null,"msg":"无发布路线"}
### 班车预约
Req: {"goodspriceFen":"0","goodsdetail":"益园-张仪村","goodsprice":"0.00","alightposition":"张仪村","boardposition":"益园（其中21:30京香发车1辆）","terminus":"张仪村","selldate":"2020-11-23","endtime":"22:00","goodsname":"21:45益园-张仪村","id":32,"starttime":"21:45","method":"/mobile/pay/toPaySelf"}
Res: {"code":200,"data":"20112115210763417171","msg":"success"}

### 订单查询
Req: {"pageNumber":1,"pageSize":10,"status":1,"method":"/goods/order/getBusOrderList"}
Res: {"code":200,"data":{"content":[{"departurestation":"益园","orderno":"20112110504835370836","goodsname":"20:30益园-张仪村","remark":null,"starttime":"20:30","bordrime":null,"verbordrime":null,"boardposition":"益园（其中20:15京香发车1辆）","paypriceyuan":0,"businessjourno":null,"id":18084,"goorderno":"20112110504835370836","gostatus":"1","alightposition":"张仪村","goodsid":"31","organcode":"0001","selldate":"2020-11-22T16:00:00.000+0000","endtime":"21:00","gotxdate":"2020-11-21T02:50:48.353+0000","goidserial":"5518","goodsdetail":"益园-张仪村","terminus":"张仪村","goodsorderid":18085,"payprice":0,"goodsnum":1},...}],"pageable":{"sort":{"unsorted":true,"sorted":false,"empty":true},"offset":0,"pageNumber":0,"pageSize":10,"unpaged":false,"paged":true},"totalPages":1,"totalElements":2,"last":true,"number":0,"size":10,"sort":{"unsorted":true,"sorted":false,"empty":true},"numberOfElements":2,"first":true,"empty":false},"msg":null}
