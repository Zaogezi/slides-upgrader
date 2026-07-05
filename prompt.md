| 方法 | 需要的环境配置 | 主要负责导出 | 最适合的内容 | 不建议承担 |
|---|---|---|---|---|
| MathJax / KaTeX / LaTeX 公式渲染 | Node.js + `mathjax-full` / `katex`；或 TeX Live / MiKTeX；可选 `sharp` / `dvisvgm` 转图 | 数学公式图片或 SVG | 矩阵、分式、积分、求和、极限、分段函数、推导链、优化目标、概率公式 | 复杂结构图、流程图、数据图 |
| Graphviz / Mermaid 图结构渲染 | Graphviz `dot`；或 Node.js + `@viz-js/viz`；Mermaid 可用 `@mermaid-js/mermaid-cli`，通常需要 Chromium | 结构图 SVG/PNG | 树状图、语法树、状态机、自动机、流程图、依赖图、DAG、知识图谱局部结构 | 高精度数学公式、复杂几何图 |
| 手写 SVG / 程序化 SVG | 基础 SVG 生成能力；可用 Node.js / Python；可选 `sharp`、CairoSVG、Inkscape、浏览器转 PNG | 数学示意图、几何/关系图 | 交换图、坐标示意、向量空间映射、集合关系、简单几何图、箭头关系图、概念示意图 | 大量数据图、复杂公式排版 |
| Python / JS 绘图 | Python + Pillow / matplotlib / networkx；或 Node.js + Canvas / SVG / D3；可选 `reportlab`、`python-pptx`、`sharp` | 数据图、批量生成图、算法可视化 | 函数图、热力图、矩阵可视化、统计图、算法过程图、批量题目配图、实验结果图 | 单个纯公式、Office 可编辑公式 |