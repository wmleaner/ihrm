import jsonschema
data={"message":"操作成功！","mobile":"13800000002"}
schema={"type":"object",
        "properties":{
            "message":{"pattern":"操作成功"},
            "mobile":{"pattern":"^[0-9]{11}$"}
        }}
res=jsonschema.validate(instance=data,schema=schema)
print(res)
