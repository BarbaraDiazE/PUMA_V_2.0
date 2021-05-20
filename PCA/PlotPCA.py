"""
provide help to visualice PCA results 
and explore chemical space
"""
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
from bokeh.plotting import figure
from bokeh.core.enums import LegendLocation

"""
column source, to allow bokeh plot
"""
import bokeh
from bokeh.models import ColumnDataSource


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
        print(a, b)
        source1 = column_source(result, "APEXBIO")
        source2 = column_source(result, "Asinex")
        source3 = column_source(result, "ChemDiv")
        source4 = column_source(result, "Enamine")
        source5 = column_source(result, "Life_Chemicals")
        source6 = column_source(result, "MedChemExpress")
        source7 = column_source(result, "OTAVA_DNMT1")
        source8 = column_source(result, "OTAVA_DNMT3b")
        source9 = column_source(result, "SelleckChem")
        source10 = column_source(result, "Targetmol")
        source11 = column_source(result, "Tocris")
        hover = HoverTool(tooltips=[("PCA 1", "$x"), ("PCA 2", "$y"), ("ID", "@N"),])
        p = figure(
            # title="PCA based on: " + parameter,
            x_axis_label="PC 1 " + str(a) + "%",
            y_axis_label="PC 2 " + str(b) + "%",
            x_range=(-5, 10),
            y_range=(-5, 8),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        APEXBIO_plot = p.circle(x="x", y="y", source=source1, color="mediumvioletred", size=5)
        Asinex_plot = p.circle(x="x", y="y", source=source2, color="mediumslateblue", size=5)
        ChemDiv_plot = p.circle(x="x", y="y", source=source3, color="lightsalmon", size=5)
        Enamine_plot = p.circle(x="x", y="y", source=source4, color="gold", size=5)
        Life_Chemicals_plot = p.circle(x="x", y="y", source=source5, color="violet", size=5)
        MedChemExpress_plot = p.circle(x="x", y="y", source=source6, color="mediumaquamarine", size=5)
        OTAVA_DNMT1_plot = p.circle(x="x", y="y", source=source7, color="steelblue", size=5)
        OTAVA_DNMT3b_plot = p.circle(x="x", y="y", source=source8, color="navy", size=5)
        SelleckChem_plot = p.circle(x="x", y="y", source=source9, color="darkred", size=5)
        Targetmol_plot = p.circle(x="x", y="y", source=source10, color="indigo", size=5)
        Tocris_plot = p.circle(x="x", y="y", source=source11, color="pink", size=5)

        legend = Legend(
            items=[
                ("APEXBIO", [APEXBIO_plot]),
                ("Asinex", [Asinex_plot]),
                ("ChemDiv", [ChemDiv_plot]),
                ("Enamine", [Enamine_plot]),
                ("Life_Chemicals", [Life_Chemicals_plot]),
                ("MedChemExpress", [MedChemExpress_plot]),
                ("OTAVA_DNMT1", [OTAVA_DNMT1_plot]),
                ("OTAVA_DNMT3b", [OTAVA_DNMT3b_plot]),
                ("SelleckChem", [SelleckChem_plot]),
                ("Targetmol", [Targetmol_plot]),
                ("Tocris", [Tocris_plot]),
            ],
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"
        #
        show(p)
        # save
        p.output_backend = "svg"
        export_svgs(
            p,
            filename="/Users/eurijuarez/Desktop/Alexis/Plots/SVG_files/"
            + "ChemSpace_PCA"
            + ".svg",
        )

    def plot_pca_apexbio_asinex(self, parameter, a, b):
        result = self.result
        print(a, b)
        source1 = column_source(result, "APEXBIO")
        source2 = column_source(result, "Asinex")
        hover = HoverTool(tooltips=[("PCA 1", "$x"), ("PCA 2", "$y"), ("ID", "@N"),])
        p = figure(
            # title="PCA based on: " + parameter,
            x_axis_label="PC 1 " + str(a) + "%",
            y_axis_label="PC 2 " + str(b) + "%",
            x_range=(-2, 6),
            y_range=(-4, 4.1),
            tools=[hover],
            plot_width=1000,
            plot_height=800,
        )
        p.add_tools(
            LassoSelectTool(), ZoomInTool(), ZoomOutTool(), SaveTool(), PanTool()
        )
        APEXBIO_plot = p.circle(x="x", y="y", source=source1, color="mediumvioletred", size=5)
        Asinex_plot = p.circle(x="x", y="y", source=source2, color="mediumslateblue", size=5)

        legend = Legend(
            items=[("APEXBIO", [APEXBIO_plot]), ("Asinex", [Asinex_plot]),],
            location="center",
            orientation="vertical",
            click_policy="hide",
        )
        p.add_layout(legend, place="right")
        p.xaxis.axis_label_text_font_size = "20pt"
        p.yaxis.axis_label_text_font_size = "20pt"
        p.xaxis.axis_label_text_color = "black"
        p.yaxis.axis_label_text_color = "black"
        p.xaxis.major_label_text_font_size = "18pt"
        p.yaxis.major_label_text_font_size = "18pt"
        p.title.text_font_size = "22pt"
        #
        show(p)
        # save
        p.output_backend = "svg"
        export_svgs(
            p,
            filename="/Users/eurijuarez/Desktop/Alexis/Plots/SVG_files/"
            + "ChemSpace_PCA_APEXBIO_Asinex"
            + ".svg",
        )

