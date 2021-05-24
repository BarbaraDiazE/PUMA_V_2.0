"""
provide help to visualice PCA results and explore chemical space
"""
import pandas as pd
from bokeh.io import show, output_file, export, export_png, export_svgs
from bokeh.models import (
    ColumnDataSource,
    LassoSelectTool,
    ZoomInTool,
    ZoomOutTool,
    SaveTool,
    HoverTool,
    PanTool,
    Legend,
)
from bokeh.plotting import *
from bokeh.core.enums import LegendLocation

"""
column source, to allow bokeh plot
"""
import bokeh
from bokeh.models import ColumnDataSource
from bokeh.embed import components


def column_source(result, Library):
    X = list()
    Y = list()
    N = list()
    DF = result[result["Library"] == Library]
    X = list(DF["PC 1"])
    Y = list(DF["PC 2"])
    N = list(DF["ID"])

    return ColumnDataSource(dict(x=X, y=Y, N=N))


class Plot:
    def __init__(self, result):
        self.result = result

    def plot_pca(self, parameter, a, b):
        result = self.result
        print(result.Library.unique())
        hover = HoverTool(tooltips=[("PCA 1", "$x"), ("PCA 2", "$y"), ("ID", "@N"),])
        p = figure(
            title= "PCA based on: " + parameter,
            x_axis_label="PC 1 " + str(a) + "%",
            y_axis_label="PC 2 " + str(b) + "%",
            x_range=(-5, 10),
            y_range=(-5, 8),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        items = list()
        colors = ["mediumvioletred","mediumslateblue", "lightsalmon", "gold", "violet", "mediumaquamarine", "steelblue", "navy", "darkred", "indigo", "pink"]
        libraries = list(result.Library.unique())
        for i in range(len(libraries)):
            _source = column_source(result, libraries[i])
            _plot = p.circle(x="x", y="y", source=_source, color=colors[i], size=5)
            items.append((libraries[i], [_plot]))
        legend = Legend(
            items = items,   
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"
        # save
        # p.output_backend = "svg"
        # export_svgs(
        #     p,
        #     filename="/Users/eurijuarez/Desktop/Alexis/Plots/SVG_files/"
        #     + "ChemSpace_PCA"
        #     + ".svg",
        # )
        script, div = components(p)
        return script, div

    # def plot_pca_apexbio_asinex(self, parameter, a, b):
    #     result = self.result
    #     print(a, b)
    #     source1 = column_source(result, "a")
    #     source2 = column_source(result, "b")
    #     hover = HoverTool(tooltips=[("PCA 1", "$x"), ("PCA 2", "$y"), ("ID", "@N"),])
    #     p = figure(
    #         # title="PCA based on: " + parameter,
    #         x_axis_label="PC 1 " + str(a) + "%",
    #         y_axis_label="PC 2 " + str(b) + "%",
    #         x_range=(-2, 6),
    #         y_range=(-4, 4.1),
    #         tools=[hover],
    #         plot_width=1000,
    #         plot_height=800,
    #     )
    #     p.add_tools(
    #         LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
    #     )
    #     APEXBIO_plot = p.circle(x="x", y="y", source=source1, color="mediumvioletred", size=5)
    #     Asinex_plot = p.circle(x="x", y="y", source=source2, color="mediumslateblue", size=5)

    #     legend = Legend(
    #         items=[("APEXBIO", [APEXBIO_plot]), ("Asinex", [Asinex_plot]),],
    #         location="center",
    #         orientation="vertical",
    #         click_policy="hide",
    #     )
    #     p.add_layout(legend, place="right")
    #     p.xaxis.axis_label_text_font_size = "20pt"
    #     p.yaxis.axis_label_text_font_size = "20pt"
    #     p.xaxis.axis_label_text_color = "black"
    #     p.yaxis.axis_label_text_color = "black"
    #     p.xaxis.major_label_text_font_size = "18pt"
    #     p.yaxis.major_label_text_font_size = "18pt"
    #     p.title.text_font_size = "22pt"
    #     #
    #     show(p)
    #     # save
    #     p.output_backend = "svg"
    #     export_svgs(
    #         p,
    #         filename="/Users/eurijuarez/Desktop/Alexis/Plots/SVG_files/"
    #         + "ChemSpace_PCA_APEXBIO_Asinex"
    #         + ".svg",
    #     )
"""driver code"""
#Load result

# result =pd.read_csv("/home/babs/Desktop/test_puma/PCA_result_test_puma_2.csv")
# print(result.head(10))
# plot = Plot(result).plot_pca("pca", "50","50")
# show(plot)