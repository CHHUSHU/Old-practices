import requests
import json
import jsonpath
from pyecharts.chars import Map
from pyecharts import options as opts
from demo1 import nameMap

url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
resp = requests.post(url).text
print(resp)
data = json.loads(resp)
print(data)

name = jsonpath.jsonpath(data,"$..name")
print(name)
confirm = jsonpath.jsonpath(data,"$..confirm")
print(confirm)

a = list(zip(name,confirm))
print(a)

map_ = Map(opts.InitOpts(width='1200px', height='600')).add(series_name="世界各国病死率率"，
data_pair=a,
maptype="world",
name_map=nameMap)

map_.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

map_.set_global_opts(title_opts=opts.TitleOpts(title="国外疫情情况"),
visualmap_opts=opts.VisualMapOpts(max_2200000,is_piecewise=True))

map_.render("国外疫情情况.html")

