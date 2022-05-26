from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType


words = [
    ("粗糙集", 10),
    ("维度约简", 10),
    ("可解释", 10),
    ("粒度", 10),
    ("医疗诊断", 10),
]
c = (
    WordCloud()
    .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
    .render("关键词.html")
)

from pyecharts import options as opts
from pyecharts.charts import WordCloud

words = [
    ("一阶逻辑", 30),
    ("集合", 40),
    ("集合的计数", 10),
    ("二元关系", 10),
    ("等价关系", 30),
    ("划分", 20),
    ("划分块", 20),
    ("商集", 30),
]

c = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 100],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义文字样式"))
    .render("用到的知识.html")
)

