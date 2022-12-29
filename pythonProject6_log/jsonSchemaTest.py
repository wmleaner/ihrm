import jsonschema
#创建校验规则
#调用方法validate方法，实现校验
schema={
    "type":"object",
    "properties":{
        "success":{"type":"boolean"},
         "code":{"type":"integer"},
          "message":{"type":"string"}
    },
      "required":["success","code","message"]
}
data={
	"success":True,
         "code":10000,
          "message":"操作成功！"
}
result=jsonschema.validate(instance=data,schema=schema)
print("result=",result)
'''
None表示已通过
sonschema.exceptions.ValidationError--数据与校验规则不符合
SchemaError表示规则不符合

'''