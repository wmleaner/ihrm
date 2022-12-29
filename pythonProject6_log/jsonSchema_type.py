import jsonschema
'''

'''
# schema={
#     "type":"object",
#     "poperties":{
#         "success":{"":"boolean"},
#         "code":{"type":"integer"},
#         "message":{"type":"string"},
#         "address":{"type":"null"},
#          "lucky":{"type":"array"}},
#          "required":["data","address"]
# }
schema={
    "type":"object",
    "poperties":{
        "success":{"const":True},
        "code":{"const":10000},
        "message":{"const":"操作成功！"},
        },
         "required":["code","message","success"]}
data={
"success":True,
         "code":10000,
          "message":"操作成功！",
    "address":None,

    "lucky":[6,9,0]
}
result=jsonschema.validate(instance=data,schema=schema)
print("result=",result)